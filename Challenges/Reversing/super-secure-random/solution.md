# Solution

The main goal of this challenge is the actual process of reversing a binary (decompiling, looking through funcations, and annotating). The actual algorithm that needs to be reversed is pretty simple.

## The Algorithim

1. The random number generator is initialized with `seed`. The starting value for `seed` is always 42.
2. A random number is generated, `seed` is overwritten with this number.
3. The process repeats.

There are two important things that you should notice about the algorithim.

1. The random number generator always starts with the same seed.
2. Each subsiquent generation uses the previous output as the seed.

## Breaking the algorithim

Using these observations (and a vague understanding of how random number generators work), we can say the following about the algorithim.

1. Because the starting seed is constant, we can predict the first number we have to guess by running a random number generator with the same seed.
2. Because each subsiquent number is based on the previous result, we can feed the previous result into our random number generator to predict the next number.

An example program that employs this method can be found in this folder under `solveRng.cpp`.
