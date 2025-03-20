#include <iostream>
#include <fstream>
#include <string>
#include <map>

using namespace std;

int main() {

    ifstream inFS;

    inFS.open("./test.txt");

    if (!inFS.is_open()) { exit(1); }

    string line;

    while (!inFS.eof()) {
        
    }

    return 0;
}