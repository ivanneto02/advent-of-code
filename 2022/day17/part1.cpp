#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>

#include "shapes.hpp"

using namespace std;

int getHighestY(vector<Point>);
int getLowestY(vector<Point>);
bool comeToRest(vector<Point>, vector<Point>);
void tick(Shape*, vector<Point>&, string&);
void performAction(vector<Point>&, const vector<Point>&, char);

void moveRight(vector<Point>&, const vector<Point>&);
void moveLeft(vector<Point>&, const vector<Point>&);
void moveDown(vector<Point>&, const vector<Point>&);
void testPrintVct(const vector<Point>&);

void printSimulation(const vector<Point>&, const vector<Point>&);

void tick(
        Shape* currShape,
        vector<Point>& surface,
        string& actions
    ) {

    // printing vector for testing

    // cout << "surface:" << endl;
    // testPrintVct(surface);

    // cout << "\nshape:" << endl;
    // testPrintVct(currShape->coords);

    // // int test = 0;

    // cout << "original state:" << endl;
    // printSimulation(currShape->coords, surface);

    int actionCounter = 0;

    while (true) {
        // cout << "ticking" << actionCounter << " - " << actions.at(actionCounter % actions.size()) <<  endl; // test actions
        // cout << "ticking" << actionCounter << " - " << comeToRest(currShape->coords, surface) <<  endl; // test comeToRest
        // first perform action
        // cout << actions << endl;
        performAction(currShape->coords, surface, actions.at(0));
        // add this action to the queue
        actions = actions.substr(1) + actions.substr(0, 1);

        // cout << actions << endl;

        // cout << "min: " << getLowestY(currShape->coords) << endl;

        if (comeToRest(currShape->coords, surface)) {
            break;
        }

        // printSimulation(currShape->coords, surface);

        // cout << "rock falls 1 unit:" << endl;
        // then move the block down
        moveDown(currShape->coords, surface);

        // printSimulation(currShape->coords, surface);

        actionCounter += 1;
    }

    // // one more action needs to happen before fully at rest
    // // cout << actions << endl;
    // performAction(currShape->coords, surface, actions.at(0));
    // actions = actions.substr(1) + actions.substr(0, 1);

    // printSimulation(currShape->coords, surface);

    // actions = actions.substr(0, actionCounter + 1) + actions.substr(actionCounter);

    // update the surface only if shape is at rest!
    for (int i = 0; i < currShape->coords.size(); i++) {
        surface.push_back(currShape->coords.at(i));
    }

    // done "ticking" :)
}

int main() {

    ifstream inFS;

    ofstream outFS;

    int maxShapes = 100000;

    inFS.open("./input.txt");

    if (!inFS.is_open()) { 
        cout << "could not open input file" << endl;    
        exit(1);
    }

    outFS.open("./output.txt");

    if (!inFS.is_open()) {
        cout << "could not open output file" << endl;
        exit(1);
    }

    vector<Point> surface;

    // initialize surface
    for (int i = 0; i < 7; i++) {
        surface.push_back(Point(i, -1));
    }

    // initialize current max height
    int currMax = -1;
    int currMin = 0;

    int shape_i = 0;

    char currMove;
    string moves;

    while (!inFS.eof()) {
        inFS >> currMove;
        if (inFS.fail()) { break; }
        moves += currMove;
    }
    
    cout << moves << endl;

    // get initial state
    while (shape_i < maxShapes) {
        outFS << shape_i << " " << currMax + 1 << "\n";

        // get shape, place it in simulation
        // and see how it affects the surface
        Shape* currShape;

        switch (shape_i % 5) {

            case 0:
                // cout << "creating HBar" << endl;
                currShape = new HBar(currMax + 1);
                break;
            case 1:
                // cout << "creating Plus" << endl;
                currShape = new Plus(currMax + 1);
                break;
            case 2:
                // cout << "creating BackL" << endl;
                currShape = new BackL(currMax + 1);
                break;
            case 3:
                // cout << "creating VBar" << endl;
                currShape = new VBar(currMax + 1);
                break;
            case 4:
                // cout << "creating Square" << endl;
                currShape = new Square(currMax + 1);
                break;
            default:
                break;
        }

        // fill up the shape's points
        currShape->fillCoords();

        tick(currShape, surface, moves);

        // print the simulation (visualize)
        // printSimulation(currShape->coords, surface);
        
        // get highest Y given current surface
        currMax = getHighestY(surface);
        currMin = getLowestY(surface);

        // testPrintVct(surface);
        // cout << "max: " << currMax+1 << endl;
        // cout << "min: " << currMin << endl;

        // testPrintVct(surface);

        // delete currShape;

        shape_i++;
    }

    cout << "maximum: " << currMax+1 << endl;

    return 0;
}

void performAction(vector<Point>& shapePts, const vector<Point>& surfacePts, char act) {

    if (act == '<') {
        // cout << "rock moves left";
        moveLeft(shapePts, surfacePts);
    }
    else if (act == '>') {
        // cout << "rock moves right";
        moveRight(shapePts, surfacePts);
    }

}

void moveRight(vector<Point>& shapePts, const vector<Point>& surfacePts) {

    // check if hitting the wall
    for (int i = 0; i < shapePts.size(); i++) {
        if ((shapePts.at(i).x + 1) > 6) {
            // cout << ", but nothing happens1:" << endl;
            return; // do nothing if we're hitting the wall
        }
    }

    // check if hitting the stopped rocks
    for (int i = 0; i < shapePts.size(); i++) {
        for (int j = 0; j < surfacePts.size(); j++) {
            if ( (shapePts.at(i).x + 1) == surfacePts.at(j).x &&
                 (shapePts.at(i).y == surfacePts.at(j).y)
            ) {
                // cout << ", but nothing happens2:" << endl;
                return; // do nothing if we're hitting a rock
            }
        }
    }

    // now actually move
    for (int i = 0; i < shapePts.size(); i++) {
        shapePts.at(i).x += 1;
    }
    // cout << ":" << endl;
}

void moveLeft(vector<Point>& shapePts, const vector<Point>& surfacePts) {

    // check if hitting the wall
    for (int i = 0; i < shapePts.size(); i++) {
        if ((shapePts.at(i).x - 1) < 0) {
            // cout << ", but nothing happens1:" << endl;
            return; // do nothing if we're hitting the wall
        }
    }

    // check if hitting the stopped rocks
    for (int i = 0; i < shapePts.size(); i++) {
        for (int j = 0; j < surfacePts.size(); j++) {
            if ( (shapePts.at(i).x - 1) == surfacePts.at(j).x &&
                (shapePts.at(i).y == surfacePts.at(j).y)
                ) {
                // cout << ", but nothing happens2:" << endl;
                return; // do nothing if we're hitting a rock
            }
        }
    }

    // now actually move
    for (int i = 0; i < shapePts.size(); i++) {
        shapePts.at(i).x -= 1;
    }
    // cout << ":" << endl;
}

void moveDown(vector<Point>& shapePts, const vector<Point>& surfacePts) {
    // no need to check the walls for this one because action has been performed
    // check if we will hit a rock
    for (int i = 0; i < shapePts.size(); i++) {
        for (int j = 0; j < surfacePts.size(); j++) {
            // check if collision is happening right now
            if ((shapePts.at(i).y - 1) == surfacePts.at(j).y
                && (shapePts.at(i).x == surfacePts.at(j).x)
            ) {
                return; // collision detected, do nothing
            }
        }
    }

    // actually move down
    for (int i = 0; i < shapePts.size(); i++) {
        shapePts.at(i).y -= 1;
    }
}

bool comeToRest(vector<Point> shapePts, vector<Point> surfacePts) {

    for (int i = 0; i < shapePts.size(); i++) {

        for (int j = 0; j < surfacePts.size(); j++) {

            if (
                ((shapePts.at(i).y - 1) == surfacePts.at(j).y)
                && ((shapePts.at(i).x) == surfacePts.at(j).x)
            ) { // collision found, should come to rest
                return true;
            }
        }
    }

    // no collision found, good to move :)
    return false;
}

int getHighestY(vector<Point> surface) {
    // cout << "getting called" << endl;
    int max = surface.at(0).y;
    for (int i = 1; i < surface.size(); i++) {
        if (surface.at(i).y >= max) {
            max = surface.at(i).y;
        }
    }
    // cout << "max is " << max << endl; 
    return max;
}

int getLowestY(vector<Point> surface) {
    // cout << "getting called" << endl;
    int min = surface.at(0).y;
    for (int i = 1; i < surface.size(); i++) {
        if (surface.at(i).y <= min) {
            min = surface.at(i).y;
        }
    }
    return min;
}

void testPrintVct(const vector<Point>& vctr) {

    for (int i = 0; i < vctr.size(); i++) {
        cout << "(" << vctr.at(i).x << ", " << vctr.at(i).y << ") ";
    }
    cout << endl;
}

void printSimulation(
    const vector<Point>& shapePts,
    const vector<Point>& surfacePts) {

    // iterate through every possible value of Y, assume first it's 20
    for (int i = 30; i >= 0; i--) {

        // print wall
        cout << "|";

        // iterate through every X
        for (int j = 0; j < 7; j++) {

            bool found_sur = false;
            // find whether this is part of the surface
            for (int k = 0; k < surfacePts.size(); k++) {
                if (surfacePts.at(k).y == i && surfacePts.at(k).x == j) {
                    found_sur = true;
                    break;
                }
            }

            bool found_sha = false;
            // find whether this is part of the shape
            for (int k = 0; k < shapePts.size(); k++) {
                if (shapePts.at(k).y == i && shapePts.at(k).x == j) {
                    found_sha = true;
                    break;
                }
            }

            if (found_sur) {
                cout << "#";
            }
            else {
                if (found_sha) {
                    cout << "@";
                }
                else {
                    cout << ".";
                }
            }

        }

        cout << "|" << endl;

    }

    // print floor
    cout << "+";
    for (int i = 0; i < 7; i++) {
        cout << "-";
    }
    cout << "+" << endl;

    return;

}