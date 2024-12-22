import sys
import time
from utils import *

def timing(func):
    def wrapper(*arg, **kw):
        t1 = time.time()
        result = func(*arg, **kw)
        t2 = time.time()
        return (t2 - t1), result, func.__name__
    return wrapper

def main():

    n = len(sys.argv)

    fname = "test.txt"
    if n > 1:
        fname = sys.argv[1]

    p1 = part1(fname)
    p2 = part2(fname)

    print(f"Part 1: {p1[1]} ({p1[0]*1000:.4f}ms)")
    print(f"Part 2: {p2[1]} ({p2[0]*1000:.4f}ms)")

# Use state to find the robot
def get_initial_robot__pos(state, width, height):
    for j in range(0, height):
        for i in range(0, width):
            if state[j][i] == "@":
                return (i, j)
    return (-1, -1)

# defines left movement 
def move_left(state, robot_pos):
    x, y = robot_pos

    # check if we have a simple move
    if state[y][x-1] == ".":
        state[y][x] = "."
        state[y][x-1] = "@"

        return state, (x-1, y)

    # complex move, we may stay in place or move boxes
    if state[y][x-1] == "O":
        # move until
        curr = x - 1
        while (state[y][curr] != "."):
            # if we reach a # we have a #OOOO section, robot cannot move
            if state[y][curr] == "#":
                return state, robot_pos
            curr -= 1
        # If we never found a #OOOO@ section, it means we found a #O.OOO@ section, we are able to move the robot
        # curr holds the position of the implicitly found .
        for i in range(curr, x):
            state[y][i] = state[y][i+1]
        state[y][x] = "."
        return state, (x-1, y)

    # case where we have #@
    return state, robot_pos

# defines left movement 
def move_right(state, robot_pos):
    x, y = robot_pos

    # check if we have a simple move
    if state[y][x+1] == ".":
        state[y][x] = "."
        state[y][x+1] = "@"

        return state, (x+1, y)

    # complex move, we may stay in place or move boxes
    if state[y][x+1] == "O":
        # move until
        curr = x + 1
        while (state[y][curr] != "."):
            # if we reach a # we have a #OOOO section, robot cannot move
            if state[y][curr] == "#":
                return state, robot_pos
            curr += 1
        # If we never found a #OOOO@ section, it means we found a #O.OOO@ section, we are able to move the robot
        # curr holds the position of the implicitly found .
        for i in range(curr, x, -1):
            state[y][i] = state[y][i-1]
        state[y][x] = "."
        return state, (x+1, y)

    # case where we have #@
    return state, robot_pos

# defines left movement 
def move_down(state, robot_pos):
    x, y = robot_pos

    # check if we have a simple move
    if state[y+1][x] == ".":
        state[y][x] = "."
        state[y+1][x] = "@"

        return state, (x, y+1)

    # complex move, we may stay in place or move boxes
    if state[y+1][x] == "O":
        # move until
        curr = y + 1
        while (state[curr][x] != "."):
            # if we reach a # we have a #OOOO section, robot cannot move
            if state[curr][x] == "#":
                return state, robot_pos
            curr += 1
        # If we never found a #OOOO@ section, it means we found a #O.OOO@ section, we are able to move the robot
        # curr holds the position of the implicitly found .
        for j in range(curr, y, -1):
            state[j][x] = state[j-1][x]
        state[y][x] = "."
        return state, (x, y+1)

    # case where we have #@
    return state, robot_pos

# defines upward movement
def move_up(state, robot_pos):
    x, y = robot_pos

    # check if we have a simple move
    if state[y-1][x] == ".":
        state[y][x] = "."
        state[y-1][x] = "@"

        return state, (x, y-1)

    # complex move, we may stay in place or move boxes
    if state[y-1][x] == "O":
        # move until
        curr = y - 1
        while (state[curr][x] != "."):
            # if we reach a # we have a #OOOO section, robot cannot move
            if state[curr][x] == "#":
                return state, robot_pos
            curr -= 1
        # If we never found a #OOOO@ section, it means we found a #O.OOO@ section, we are able to move the robot
        # curr holds the position of the implicitly found .
        for j in range(curr, y):
            state[j][x] = state[j+1][x]
        state[y][x] = "."
        return state, (x, y-1)

    # case where we have #@
    return state, robot_pos

# Uses all state variables to modify the state and robot_pos
def make_robot_move(state, move, robot_pos, width, height):
  
    if move == "<":
        return move_left(state, robot_pos)

    if move == "^":
        return move_up(state, robot_pos)

    if move == ">":
        return move_right(state, robot_pos)

    if move == "v":
        return move_down(state, robot_pos)

    # should not get here
    return (state, robot_pos)

@timing
def part1(fname):

    f = open(fname).read()

    inputs = f.split("\n\n")

    state = inputs[0]
    state = [ list(x) for x in state.split("\n") ] # griddy on the state

    width = len(state[0])
    height = len(state)

    moves = inputs[1].strip()

    robot_pos = get_initial_robot__pos(state, width, height)

    for move in moves:
        state, robot_pos = make_robot_move(state, move, robot_pos, width, height)

    sum = 0
    # count the coordinates
    for j in range(height):
        for i in range(width):
            if state[j][i] == "O":
                sum += 100 * (j) + i 

    return sum

@timing
def part2(fname):
    return 0


if __name__ == "__main__":
    main()
