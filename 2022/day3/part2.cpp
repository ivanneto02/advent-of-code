#include <iostream>
#include <fstream>
#include <map>
#include <vector>

using namespace std;

char getSameCharacter(vector<string> group) {

    map<char, bool> myMap1;

    // iterate through first elf, create the map
    for (int i = 0; i < group.at(0).size(); i++) {
        myMap1.insert({group.at(0).at(i), true});
    } 

    // now get the same character between second and first group

    map<char, bool> myMap2;

    for (int i = 0; i < group.at(1).size(); i++) {

        map<char, bool>::iterator it = myMap1.find(group.at(1).at(i));
        // found the char, insert
        if (it != myMap1.end()) {
            myMap2.insert({it->first, true});
        }
    }

    // get same character between the third and myMap2
    for (int i = 0; i < group.at(2).size(); i++) {
        
        map<char, bool>::iterator it = myMap2.find(group.at(2).at(i));
        // found the char, return
        if (it != myMap2.end()) {
            return it->first;
        }
    }

    // default in case something went wrong
    return 'a';
}

int getPriority(char myChar) {
    if (myChar >= 97) {
        return (myChar - 96); 
    }
    else {
        return (myChar - 65 + 27);
    }
}

int main() {

    ifstream inFS;

    inFS.open("./input.txt");

    if (!inFS.is_open()) {
        exit(1);
    }
    
    int sumPriorities = 0;

    string elf1;
    string elf2;
    string elf3;
    while (!inFS.eof()) {
        inFS >> elf1;
        if (inFS.fail()) { break; }
        inFS >> elf2;
        inFS >> elf3;
        
        vector<string> group = {elf1, elf2, elf3};

        char sameCharacter = getSameCharacter(group);
        sumPriorities += getPriority(sameCharacter);
    }

    cout << "total score: " << sumPriorities << endl; 

    return 0;
}