import re

def main():
    print("Part1: ", part1())
    print("Part2: ", part2(), "\n")

def part1():
    return calcSum(open("main.txt").read())

def calcSum(text):
    rex = r'(mul\([^\(]*?\))'
    matches = re.findall(rex, text)
    sum = 0
    for m in matches:
        rex1 = r'\d+'
        m1 = re.findall(rex1, m)
        if (len(m1) == 1):
            continue
        sum += int(m1[0])*int(m1[1])
    return sum

def part2():
    x = open("main.txt").read()
    res = re.sub(r"\n|\t|\r\n", " ", x)
    res = re.sub(r"don't\(\).*?(?:do\(\)|$)", "BUFF", res)
    return calcSum(res)

if __name__ == "__main__":
    main()