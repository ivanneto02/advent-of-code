#ifndef __SHAPES_HPP__
#define __SHAPES_HPP__

#include <iostream>
#include <vector>

using namespace std;

struct Point {
    Point(int x, int y) : x(x), y(y) {}
    int x;
    int y;
};

struct Shape {
    Shape() : maxHeight(0) {}
    Shape(int maxHeight) : maxHeight(maxHeight) {
        // cout << "shape construc being called" << endl;
        // cout << this->coords.size() << endl;
    }
    std::vector<Point> coords;
    virtual void fillCoords() = 0;
    void initY();
    int maxHeight;
};

struct HBar : public Shape {
    HBar(int maxHeight) : Shape(maxHeight) {
        // cout << "HBar construc being called" << endl;
        // cout << this->coords.size() << endl;
    }
    void fillCoords() override;
};

struct Plus : public Shape {
    Plus(int maxHeight) : Shape(maxHeight) {
        // cout << "Plus construc being called" << endl;
        // cout << this->coords.size() << endl;
    }
    void fillCoords() override;
};

struct BackL : public Shape {
    BackL(int maxHeight) : Shape(maxHeight) {}
    void fillCoords() override;
};

struct VBar : public Shape {
    VBar(int maxHeight) : Shape(maxHeight) {}
    void fillCoords() override;
};

struct Square : public Shape {
    Square(int maxHeight) : Shape(maxHeight) {}
    void fillCoords() override;
};


#endif