#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <stack>
#include <cstdlib>

using namespace std;

void populateStacks(vector<stack<char>>&, string, int, int);
int getNumberOfStacks(const string&);
int getNumberOfLines(string);
void printStack(stack<char>);
void modifyStacks(vector<stack<char>>&, int, int, int);

int parseSize(string);
int parseFrom(string);
int parseTo(string);

int main() {

    ifstream inFS;

    inFS.open("./input.txt");

    if (!inFS.is_open()) { exit(1); }
    
    ostringstream outSS;

    string line;
    // get initial state
    while (!inFS.eof()) {
        getline(inFS, line);
        if (line == "") {
            break;
        }
        outSS << line << "\n";
    }

    // cout << "test\n" << outSS.str() << endl;

    int numStacks = getNumberOfStacks(outSS.str());
    int numLines  = getNumberOfLines(outSS.str());

    cout << numStacks << endl;
    cout << numLines << endl;

    vector<stack<char>> stacks;

    // populates the stacks appropriately. Stacks should now have
    // stacks.size() number of stacks within it that represent each
    // existing stack given at the beginning.
    populateStacks(stacks, outSS.str(), numStacks, numLines);

    // continue until no more operations
    int size;
    int from;
    int to;
    // cout << endl << endl;
    while (!inFS.eof()) {
        getline(inFS, line);
        if (inFS.fail()) { break; }
        

        size = parseSize(line);
        from = parseFrom(line);
        to   = parseTo(line);

        // cout << size << endl;
        // cout << from << endl;
        // cout << to << endl;

        modifyStacks(stacks, size, from, to);

        // cout << endl;

        // for (int i = 0; i < stacks.size(); i++) {
        //     printStack(stacks.at(i));
        // }
    }

    // print out top crates
    cout << "stacks at the top: ";
    for (int i = 0; i < stacks.size(); i++) {
        cout << stacks.at(i).top();
    }
    cout << endl;

    return 0;
}

void populateStacks(
        vector<stack<char>>& stacks,
        string items,
        int numStacks,
        int numLines
    ) {

        for ( int i : vector<int>(numStacks) ) {
            stacks.push_back(stack<char>());
        }

        // iterate num times
        for ( int i = 0; i < numLines; i++ ) {
            
            string line = items.substr(0, items.find('\n'));

            // iterate through every stack
            for (int j = 0; j < numStacks; j++) {

                if (line.at(j*4 + 1) != ' ') {

                    stacks.at(j).push(line.at( j*4 + 1 ));
                } 

            }

            items = items.substr(items.find('\n') + 1);
        }

        // now reverse the stack
        for (int i = 0; i < numStacks; i++) {

            // place items into vector to reverse
            vector<char> tmp;
            stack<char> curr = stacks.at(i);
            while (!curr.empty()) {
                tmp.push_back(curr.top());
                curr.pop();
            }

            for (int j = 0; j < tmp.size(); j++) {
                curr.push(tmp.at(j));
            }

            stacks.at(i) = curr;
        } 

    return;
}

int getNumberOfStacks(const string& startState) {
    string firstLine = startState.substr(0, startState.find("\n"));
    return (firstLine.size() / 4) + 1;
}

int getNumberOfLines(string state) {
    int count = 0;
    while ( state.find('\n') != string::npos ) {
        state = state.substr(state.find('\n') + 1);
        count++;
    }
    return count - 1;
}

void printStack(stack<char> s) {
    cout << ": ";
    for ( int i : vector<int>(s.size()) ) {
        cout << s.top() << " ";
        s.pop();
    }
    cout << endl;
}

int parseSize(string line) {
    string sizeMarker = "move ";
    int markerIdx = line.find(sizeMarker) + sizeMarker.length();
    string num = line.substr(markerIdx, line.find(" ", markerIdx) - markerIdx + 1);
    return stoi(num);
}

int parseFrom(string line) {
    string sizeMarker = "from ";
    int markerIdx = line.find(sizeMarker) + sizeMarker.length();
    string num = line.substr(markerIdx, line.find(" ", markerIdx) - markerIdx + 1);
    return stoi(num);
}

int parseTo(string line) {
    string sizeMarker = "to ";
    int markerIdx = line.find(sizeMarker) + sizeMarker.length();
    string num = line.substr(markerIdx, line.find(" ", markerIdx) - markerIdx + 1);
    return stoi(num);
}

/*
stacks : vector of stacks of char type
s : size to move
f : from which stack
t : to which stack
*/
void modifyStacks(vector<stack<char>>& stacks, int s, int f, int t) {

    // cout << "moving " << s << " creates from " << f << " to " << t << endl;

    int fromIdx = f - 1;
    int toIdx = t - 1;

    // store temporary values
    vector<char> tmp; // stores tmp characters
    for (int i = 0; i < s; i++) {
        tmp.push_back(stacks.at(fromIdx).top());
        stacks.at(fromIdx).pop();
    }

    // move temporary values back to intended stack
    for (int i = 0; i < s; i++) {
        stacks.at(toIdx).push(tmp.at(i));
    }

    // done :)
}