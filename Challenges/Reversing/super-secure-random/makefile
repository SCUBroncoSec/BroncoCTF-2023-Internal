targets = x86_64-linux x86_64-macos x86_64-windows aarch64-macos

binaries: ${targets}

${targets}:
	zig c++ -o ./files/rng-$@ rng.cpp