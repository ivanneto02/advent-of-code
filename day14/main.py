import sys
import time
import re
import unittest

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
    steps = 0
    width = 11
    height = 7
    if n > 4:
        fname = sys.argv[1]
        steps = int(sys.argv[2])
        width = int(sys.argv[3])
        height = int(sys.argv[4])

    p1 = part1(fname, steps, width, height)
    p2 = part2(fname, steps, width, height)

    print(f"Part 1: {p1[1]} ({p1[0]*1000:.4f}ms)")
    print(f"Part 2: {p2[1]} ({p2[0]*1000:.4f}ms)")

    return 0

# Calculates in which quadrant each position is, and returns the product of all
# the counts of robots in each quadrant
def safety_factor(positions, width=11, height=7):

    quadrants = [0, 0, 0, 0]
    for pos in positions:

        if pos[0] > width//2 and pos[1] < height//2:
            quadrants[0] += 1
        elif pos[0] < width//2 and pos[1] < height//2:
            quadrants[1] += 1 
        elif pos[0] < width//2 and pos[1] > height//2:
            quadrants[2] += 1
        elif pos[0] > width//2 and pos[1] > height//2:
            quadrants[3] += 1

    return quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3]

# For debugging. It prints the state of the given set of positions, including the
# empty spaces. It will also be used for part 2 since we need to see where the
# tree is located!
def print_state(positions, width=11, height=7):
    counts = {}    
    for pos in positions:
        if pos not in counts:
            counts[pos] = 1
        else:
            counts[pos] += 1

    for j in range(0, height):
        for i in range(0, width):
            if (i, j) not in counts:
                print(".", end="")
            else:
                print(counts[(i, j)], end="")
        print("")
    print("")

@timing
def part1(fname, steps=100, width=11, height=7):

    f = open(fname).read().strip()

    robots = f.split("\n")
    ints_regex = r"-?\d+"
   
    positions = []

    for robot in robots:
        x, y, vx, vy = map(int, re.findall(ints_regex, robot))

        final_x = (x + (vx * steps) ) % width
        final_y = (y + (vy * steps) ) % height 

        positions.append((final_x, final_y))

    # # uncomment this section for debugging
    # print_state(positions, width, height)
    return safety_factor(positions, width, height)

@timing
def part2(fname, steps=100, width=11, height=7):

    f = open(fname).read().strip()

    robots = f.split("\n")
    ints_regex = r"-?\d+"

    # we'll look at every picture and display the seconds. We'll look through
    # the output to see if we can find anything
    for sec in range(39, 10000, 101):
        positions = []
        for robot in robots:
            x, y, vx, vy = map(int, re.findall(ints_regex, robot))

            final_x = (x + (vx * sec) ) % width
            final_y = (y + (vy * sec) ) % height 

            positions.append((final_x, final_y))

        # # uncomment and pipe main.py to output.txt ('command > output.txt')
        # print(f"t = {sec}s")
        # print_state(positions, width, height)
        # print("\n")
    return 0 

if __name__ == "__main__":
    main()
