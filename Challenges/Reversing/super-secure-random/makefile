targets = x86_64-linux x86_64-macos x86_64-windows

binaries: ${targets}

${targets}:
	zig c++ -o ./files/rng-$@ rng.cpp