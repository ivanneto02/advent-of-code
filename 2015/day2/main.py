
def main():
    print("Part1: ", part1())
    print("Part2: ", part2())
    return

def part1():

    f = open("main.txt").read()
    nums = list(map(int, f.split("\n")))

    return sum(2 * nums)

def part2():
    
    return 0

if __name__ == "__main__":
    main()