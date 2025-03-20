#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main() {

    // read file
    ifstream inFS;
    inFS.open("./input.txt");
    if (!inFS.is_open()) { exit(1); }

    // get characters
    string currLine;

    // iterate until end of file
    int currSum = 0; 
    int max = 0;
    while (!inFS.eof()) {

        // grab the line
        getline(inFS, currLine);

        // if currently at in between two lists or
        // end of the file
        if (currLine == "" || inFS.eof()) {
            if (currSum >= max) {
                max = currSum;
            }
            currSum = 0;
        }
        else {
            currSum += stoi(currLine);
        }
    }

    cout << "max: " << max << endl;

    return 0;
}