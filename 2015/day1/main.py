
def main():
    print("Part1: ", part1())
    print("Part2: ", part2())
    return

def part1():
    f = open("main.txt").read()
    tot = 0
    for c in f:
        if c == "(": tot += 1
        elif c == ")": tot -= 1
    return tot

def part2():
    f = open("main.txt").read()
    tot = 0
    for i, c in enumerate(f):
        if c == "(": tot += 1
        elif c == ")": tot -= 1
        if tot == -1:
            return i + 1
    return 0

if __name__ == "__main__":
    main()