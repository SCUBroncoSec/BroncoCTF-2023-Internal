#Config vars
variable "project_id" {
  default = "broncosec-2023"
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

#Providers
provider "google" {
  project = var.project_id
  region = var.location
}

#Service accounts
resource "google_service_account" "cluster-sa" {
  account_id = "${var.project_id}-cluster-sa"
  display_name = "SA for GKE cluster ${var.project_id}-cluster"
}

#Cluster
resource "google_container_cluster" "primaryCluster" {
  name = "${var.project_id}-cluster"
  location = var.location

  #Default node pool, is deleted immedietly and replaced with custom defined node pool
  remove_default_node_pool = true
  initial_node_count = 1
}

#Node pool
resource "google_container_node_pool" "primaryCluster-nodePool" {
  name = "${google_container_cluster.primaryCluster.name}-nodePool"
  location = var.location
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