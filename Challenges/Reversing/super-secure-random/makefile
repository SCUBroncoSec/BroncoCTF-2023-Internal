targets = x86_64-linux x86_64-macos x86_64-windows aarch64-macos

binaries: ${targets}

${targets}:
	zig c++ -o ./files/rng-$@ -target $@ rng.cpp

docker:
	cp ./files/rng-x86_64-linux ./infra/rng-x86_64-linux
	cd infra && docker build -t us-west2-docker.pkg.dev/broncoctf-2023/broncoctf-2023/super-secure-random:latest . && docker push us-west2-docker.pkg.dev/broncoctf-2023/broncoctf-2023/super-secure-random:latest