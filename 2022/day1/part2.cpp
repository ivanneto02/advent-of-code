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

    int max1 = 0;
    int max2 = 0;
    int max3 = 0;

    int i = 1;
    while (!inFS.eof()) {

        // grab the line
        getline(inFS, currLine);

        // if currently at in between two lists or
        // end of the file
        if (currLine == "" || inFS.eof()) {
            // check all three maximums
            if (currSum >= max1) {
                max3 = max2;
                max2 = max1;
                max1 = currSum;
            }
            else if (currSum >= max2) {
                max3 = max2;
                max2 = currSum;
            }
            else if (currSum >= max3) {
                max3 = currSum;
            }

            currSum = 0;
            i++;
        }
        else {
            currSum += stoi(currLine);
        }
    }

    cout << "max1: " << max1 << endl;
    cout << "max2: " << max2 << endl;
    cout << "max3: " << max3 << endl;
    cout << "sum: " << max1 + max2 + max3 << endl;

    return 0;
}