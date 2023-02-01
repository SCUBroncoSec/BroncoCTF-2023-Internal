#Config vars
variable "project_id" {
  default = "broncoctf-2023"
}

variable "dns-project-id" {
  default = "broncoctf-dns"
}

variable "location" {
  default = "us-west1"
}

variable "node_type" {
  default = "e2-small"
}

variable "node_count" {
  default = 1
}

variable "dns-service-account-id" {
  default = "external-dns-sa"
}

#Providers
provider "google" {
  project = var.project_id
  region = var.location
}
data "google_client_config" "default" {}

provider "kubernetes" {
  host = google_container_cluster.primaryCluster.endpoint

  token = data.google_client_config.default.access_token
  cluster_ca_certificate = base64decode(google_container_cluster.primaryCluster.master_auth[0].cluster_ca_certificate)
}

#Service accounts
resource "google_service_account" "cluster-sa" {
  account_id = "${var.project_id}-cluster-sa"
  display_name = "SA for GKE cluster ${var.project_id}-cluster"
}

resource "google_service_account" "externaldns-sa" {
  account_id = var.dns-service-account-id
  display_name = var.dns-service-account-id
}

#IAM bindings
resource "google_project_iam_binding" "external-dns-sa-binding" {
  depends_on = [
    google_service_account.externaldns-sa
  ]
  
  project = var.dns-project-id
  role = "roles/dns.admin"

  members = [ "serviceAccount:${google_service_account.externaldns-sa.email}" ]
}

#Cluster
resource "google_container_cluster" "primaryCluster" {
  name = "${var.project_id}-cluster"
  location = "${var.location}-a"

  #Default node pool, is deleted immedietly and replaced with custom defined node pool
  remove_default_node_pool = true
  initial_node_count = 1
}

#Node pool
resource "google_container_node_pool" "primaryCluster-nodePool" {
  name = "${google_container_cluster.primaryCluster.name}-nodepool"
  location = "${var.location}-a"
  cluster = google_container_cluster.primaryCluster.name

  node_count = var.node_count

  node_config {
    preemptible = true
    machine_type = var.node_type

    service_account = google_service_account.cluster-sa.email
    oauth_scopes = [
        "https://www.googleapis.com/auth/cloud-platform"
    ]
  }
}

#external-dns secret
resource "google_service_account_key" "externaldns-sa-key" {
  service_account_id = google_service_account.externaldns-sa.account_id 
}

resource "kubernetes_secret" "externaldns-secret" {
  depends_on = [
    google_service_account_key.externaldns-sa-key
  ]

  metadata {
    name = "external-dns"
    namespace = "external-dns"
  }

  data = {
    "credentials.json" = base64decode(google_service_account_key.externaldns-sa-key.private_key)
  }
}