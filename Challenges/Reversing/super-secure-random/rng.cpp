#include <iostream>
#include <string>
#include <fstream>
#include <cstdlib>

using namespace std;

string readFlagFromFile()
{
    string returnValue = "This is the default flag value. If you see this while solving over netcat, please contact an admin!";
    
    //Try to read flag from ./flag.txt
    ifstream flagFile("flag.txt");
    
    if (flagFile)
    {
        //flag.txt was sucessfully opened
        //Read flag.txt into return string
        getline(flagFile, returnValue);
    }
    else
    {
        //flag.txt could not be opened
        cout << "flag.txt could not be read, using default flag instead" << endl;
    }

    return returnValue;
}

bool validateRandomGuess(int seed, int guess)
{
    srand(seed);

    if (guess == rand())
    {
        cout << "Wow, you're good!" << endl;
        return true;
    }
    //Else
    cout << "*Buzzer noise* WRONG!" << endl;
    return false;
}

int main()
{
    string flag = readFlagFromFile();

    int previousRandomNumber = 42; //~The~ universal constant
    int userGuess;
    size_t currentRound;

    cout << "Welcome to my Super Secure Random Number Generator" << endl;
    cout << "The challenge is simple: guess the correct number 10 times, with no mistakes, and I'll give you the flag" << endl;

    for (currentRound = 0; currentRound < 10; currentRound++)
    {
        cout << "Enter your guess: ";
        cin >> userGuess;

        if (!validateRandomGuess(previousRandomNumber, userGuess))
            break;
        
        previousRandomNumber = userGuess;
    }
    
    if (currentRound != 10)
    {
        cout << "*Trapdoor opens*" << endl;
        return 0;
    }
    
    //else
    cout << "Wow, I can't believe you actually did it!" << endl;
    cout << "The flag is: " << flag << endl;
    
    return 0;
}