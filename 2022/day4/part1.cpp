#include <iostream>
#include <fstream>
#include <string>

using namespace std;

bool determineOverlap(int a0, int a1, int b0, int b1) {

    if (a0 <= b0 && a1 <= b1) {
        return true;
    } 
    else if (b0 <= a0 && b1 <= a1) {
        return true;
    }
    
    return false;
}

int main() {

    ifstream inFS;

    inFS.open("./input.txt");

    if (!inFS.is_open()) { exit(1); }
    
    string range1;
    string range2;

    int a0;
    int a1;
    int b0;
    int b1;
    int count = 0;
    while (!inFS.eof()) {
        getline(inFS, range1, ',');
        if (inFS.fail()) { break; }
        getline(inFS, range2);
    
        // get each individual range
        a0 = stoi(range1.substr(0, range1.find('-')));
        a1 = stoi(range1.substr(range1.find('-')+1));
        b0 = stoi(range2.substr(0, range2.find('-')));
        b1 = stoi(range2.substr(range2.find('-')+1));

        if (determineOverlap(a0, a1, b0, b1)) {
            count++;
        }
    }

    cout << "total counts: " << count << endl; 

    return 0;
}