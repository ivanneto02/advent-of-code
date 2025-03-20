#include <iostream>
#include <fstream>

using namespace std;

int play_score(char l, char r) {
    if ( // win, ret 6
        l == 'A' && r == 'Y' ||
        l == 'B' && r == 'Z' ||
        l == 'C' && r == 'X') {
            return 6;
    }
    else if ( // draw, ret 3
        l == 'A' && r == 'X' ||
        l == 'B' && r == 'Y' ||
        l == 'C' && r == 'Z') {
            return 3;
    }

    // loss, return 0
    return 0;
}

int choice_score(char r) {
    if (r == 'X') {
        return 1;
    }
    else if (r == 'Y') {
        return 2;
    }
    else if (r == 'Z'){
        return 3;
    }
    else {
        // should not go in here
        return 0;
    }
}

int main() {

    ifstream inFS;

    inFS.open("./input.txt");

    if (!inFS.is_open()) {
        exit(1);
    }
    
    int sum_score = 0;
    char l;
    char r;
    while (!inFS.eof()) {
        inFS >> l;
        if (inFS.fail()) { break; }
        inFS >> r;

        sum_score += choice_score(r);
        sum_score += play_score(l, r);
    }

    cout << "total score: " << sum_score << endl; 

    return 0;
}