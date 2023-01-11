#include <iostream>
#include <cstdlib>

using namespace std;

int getRandomFromSeed (int seed)
{
    srand(seed);
    return rand();
}

int main(int argc, char const *argv[])
{
    int seed = 42;

    for (size_t round = 0; round < 10; round++)
    {
        int randResult = getRandomFromSeed(seed);
        cout << "Seed: " << seed << " Result: " << randResult << endl;
        seed = randResult;
    }

    return 0;
}
