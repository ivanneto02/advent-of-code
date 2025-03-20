#include <iostream>
#include <fstream>
#include <string>
#include <map>

using namespace std;

int main() {

    ifstream inFS;

    inFS.open("./input.txt");

    if (!inFS.is_open()) { exit(1); }

    string line;

    // get initial state
    getline(inFS, line);

    // now perform algorithm

    int iter = 0;
    for (int i = 0; i < line.length() - 14; i++) {

        // will keep track of present values
        map<char, bool> pres;
        bool found = true;
        for (int j = 0; j < 14; j++) {

            // not found
            if ( pres.find(line.at(i + j)) == pres.end() ) {
                pres.insert({line.at(i + j), true});
            }
            else {
                found = false;
            }

        }

        if (found) {
            break;
        }
        else {
            iter++;
        }

        // remove old values
        pres.clear();
    }

    cout << "processed before signal: " << iter + 14 << endl;

    return 0;
}