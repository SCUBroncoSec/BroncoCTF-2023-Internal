targets = x86_64-linux

binaries: ${targets}

${targets}:
	zig cc -o ./infra/NMLKP-$@ -target $@ NMLKP.c

image:
	cd infra && docker build -t us-west2-docker.pkg.dev/broncoctf-2023/broncoctf-2023/nmlkp:latest . 
push:
	docker push us-west2-docker.pkg.dev/broncoctf-2023/broncoctf-2023/nmlkp:latest