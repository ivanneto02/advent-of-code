def main():
    print("Part1:", part1())
    print("Part2:", part2())
    
def part2():
    f = open("main.txt")

    list1 = list()
    list2 = list()

    for line in f:
        list1.append(int(line.split("   ")[0]))
        list2.append(int(line.split("   ")[1]))

    list2map = {}
    for x in list2:
        if x in list2map:
            list2map[x] += 1
            continue
        list2map[x] = 1

    sum = 0
    for x in list1:
        if x not in list2map:
            continue
        sum += x * list2map[x]

    return sum

def part1():
    f = open("main.txt")

    list1 = list()
    list2 = list()

    for line in f:
        list1.append(int(line.split("   ")[0]))
        list2.append(int(line.split("   ")[1]))

    list1 = sorted(list1)
    list2 = sorted(list2)

    sum = 0
    for x,y in zip(list1, list2):
        sum = sum + abs(x - y)

    return sum

if __name__ == "__main__":
    main()