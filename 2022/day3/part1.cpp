#include <iostream>
#include <fstream>
#include <map>

using namespace std;

char getSameCharacter(string sack) {

    map<char, bool> myMap;

    // create the map with the first rucksack
    for (int i = 0; i < sack.size()/2; i++) {
        myMap.insert({sack.at(i), true});
    }

    // find the odd character out
    for (int i = sack.size() / 2; i < sack.size(); i++) {
        
        map<char, bool>::iterator it = myMap.find(sack.at(i));
        if (it != myMap.end()) { return it->first; }
    }

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

    string currRucksack;
    while (!inFS.eof()) {
        inFS >> currRucksack;
        if (inFS.fail()) { break; }
        char sameCharacter = getSameCharacter(currRucksack);
        sumPriorities += getPriority(sameCharacter);
    }

    cout << "total score: " << sumPriorities << endl; 

    return 0;
}