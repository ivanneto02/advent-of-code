#include <iostream>
#include <fstream>
#include <map>
#include <cmath>
#include <vector>
#include <algorithm>

using namespace std;

int part1();
int part2();

int main() {
    std::cout << "Part1: " << part1() << std::endl;
    std::cout << "Part2: " << part2() << std::endl;
}

int part1() {

    std::fstream inFS;

    inFS.open("./main.txt");

    if (!inFS.is_open()) {
        cout << "Error reading..." << endl;
        return -1;
    }

    std::vector<int> leftVec;
    std::vector<int> rightVec;

    int left;
    int right;

    while(inFS) {
        inFS >> left >> right;
        leftVec.push_back(left);
        rightVec.push_back(right);
    }

    std::sort(leftVec.begin(), leftVec.end());
    std::sort(rightVec.begin(), rightVec.end());

    int sum = 0;
    for (int i = 0; i < leftVec.size(); i++) {
        sum += std::fabs(leftVec.at(i) - rightVec.at(i));
    }
    
    return sum;
}

int part2() {

    std::fstream inFS;

    inFS.open("./main.txt");

    if (!inFS.is_open()) {
        cout << "Error reading..." << endl;
        return -1;
    }

    std::vector<int> leftVec;
    std::vector<int> rightVec;

    int left;
    int right;

    while(inFS) {
        inFS >> left >> right;
        leftVec.push_back(left);
        rightVec.push_back(right);
    }

    std::map<int, int> list2map;
    for (int i = 0; i < rightVec.size(); i++) {
        if (list2map.find(rightVec.at(i)) != list2map.end()) {
            list2map[rightVec.at(i)]++;
        }
        else {
            list2map[rightVec.at(i)] = 1;
        }
    }

    int sum = 0;
    for (int i = 0; i < leftVec.size(); i++) {
        if (list2map.find(leftVec.at(i)) != list2map.end())
        sum += leftVec.at(i) * list2map[leftVec.at(i)];
    }

    return sum;
}