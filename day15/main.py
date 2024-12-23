import sys
import time
from utils import get_initial_robot_pos
from utils import make_robot_move
from utils import wide_make_robot_move
from utils import widen_state

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

@timing
def part1(fname):

    f = open(fname).read()

    inputs = f.split("\n\n")

    state = inputs[0]
    state = [ list(x) for x in state.split("\n") ] # griddy on the state

    width = len(state[0])
    height = len(state)

    moves = inputs[1].strip()

    robot_pos = get_initial_robot_pos(state, width, height)

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
    f = open(fname).read()

    inputs = f.split("\n\n")

    state = inputs[0]
    state = [ list(x) for x in state.split("\n") ] # griddy on the state

    width = len(state[0])
    height = len(state)

    state, width, height = widen_state(state, width, height)

    moves = inputs[1].strip()

    robot_pos = get_initial_robot_pos(state, width, height)

    for move in moves:
        state, robot_pos = wide_make_robot_move(state, move, robot_pos, width, height)

    sum = 0
    # count the coordinates
    for j in range(height):
        for i in range(width):
            if state[j][i] == "[":
                sum += 100 * (j) + i 

    return sum

if __name__ == "__main__":
    main()
