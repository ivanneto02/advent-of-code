import sys
import time
import re
import heapq

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

    return 0

@timing
def part1(fname):
    f = open(fname).read()

    number_regex = r"\d+"

    # separate machines
    machines = []
    for line in f.split("\n\n"):
        machines.append(line)
   
    # clean up the input, get just the [ (A-X-Step, A-Y-Step), (B-X-Step, B-Y-Step), (X-Goal, Y-Goal) ] for each machine
    machines_clean = []
    for machine in machines:
        Ax, Ay = map(int, re.findall(number_regex, machine.split("\n")[0]))
        Bx, By = map(int, re.findall(number_regex, machine.split("\n")[1]))
        Px, Py = map(int, re.findall(number_regex, machine.split("\n")[2]))   

        machines_clean.append( ( (Ax, Ay), (Bx, By), (Px, Py) ) )

    machines = machines_clean.copy()

    tokens = []
    for machine in machines:
       
        # Abbreviated variables for equation solution
        AXS = machine[0][0] 
        AYS = machine[0][1]
        
        BXS = machine[1][0]
        BYS = machine[1][1]

        GX = machine[2][0]
        GY = machine[2][1]

        # Result of solving system of equations a * AXS + b * BXS = GX
        #                                   and a * AYS + b * BYS = GY
        b = (GY - GX * AYS / AXS) / (((-1 * BXS) * (AYS / AXS)) + BYS)
        a = (GX - b * BXS) / (AXS)

        # Check if result of a and b are close enough to integers
        if round(a, 3).is_integer() and round(b, 3).is_integer():
            tokens.append(a * 3 + b * 1)

    return int(sum(tokens))

@timing
def part2(fname):
    f = open(fname).read()

    number_regex = r"\d+"

    # separate machines
    machines = []
    for line in f.split("\n\n"):
        machines.append(line)
   
    # clean up the input, get just the [ (A-X-Step, A-Y-Step), (B-X-Step, B-Y-Step), (X-Goal, Y-Goal) ] for each machine
    machines_clean = []
    for machine in machines:
        Ax, Ay = map(int, re.findall(number_regex, machine.split("\n")[0]))
        Bx, By = map(int, re.findall(number_regex, machine.split("\n")[1]))
        Px, Py = map(int, re.findall(number_regex, machine.split("\n")[2]))   

        machines_clean.append( ( (Ax, Ay), (Bx, By), (Px + 10000000000000, Py + 10000000000000) ) )

    machines = machines_clean.copy()

    tokens = []
    for machine in machines:
       
        # Abbreviated variables for equation solution
        AXS = machine[0][0] 
        AYS = machine[0][1]
        
        BXS = machine[1][0]
        BYS = machine[1][1]

        GX = machine[2][0]
        GY = machine[2][1]

        # Result of solving system of equations a * AXS + b * BXS = GX
        #                                   and a * AYS + b * BYS = GY
        b = (GY - GX * AYS / AXS) / (((-1 * BXS) * (AYS / AXS)) + BYS)
        a = (GX - b * BXS) / (AXS)

        # Check if result of a and b are close enough to integers
        if round(a, 3).is_integer() and round(b, 3).is_integer():
            tokens.append(a * 3 + b * 1)

    return int(sum(tokens))

if __name__ == "__main__":
    main()
