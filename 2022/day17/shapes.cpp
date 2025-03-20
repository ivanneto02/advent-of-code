#include "shapes.hpp"

using namespace std;

void Shape::initY() {
    // cout << "being called" << endl;
    for (int i = 0; i < this->coords.size(); i++) {
        this->coords.at(i).y += this->maxHeight + 3;
    }
}

void HBar::fillCoords() {
    coords.push_back(Point(2, 0));
    coords.push_back(Point(3, 0));
    coords.push_back(Point(4, 0));
    coords.push_back(Point(5, 0));

    this->initY();
}


void Plus::fillCoords() {
    // cout << "plus init" << endl;
    coords.push_back(Point(2, 1));
    coords.push_back(Point(3, 0));
    coords.push_back(Point(3, 1));
    coords.push_back(Point(3, 2));
    coords.push_back(Point(4, 1));

    this->initY();
}

void BackL::fillCoords() {
    coords.push_back(Point(2, 0));
    coords.push_back(Point(3, 0));
    coords.push_back(Point(4, 0));
    coords.push_back(Point(4, 1));
    coords.push_back(Point(4, 2));

    this->initY();
}

void VBar::fillCoords() {
    coords.push_back(Point(2, 0));
    coords.push_back(Point(2, 1));
    coords.push_back(Point(2, 2));
    coords.push_back(Point(2, 3));

    this->initY();
}

void Square::fillCoords() {
    coords.push_back(Point(2, 0));
    coords.push_back(Point(3, 0));
    coords.push_back(Point(2, 1));
    coords.push_back(Point(3, 1));

    this->initY();
}