
import sys
import time
import re
from tqdm import tqdm
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

# Heuristic is Euclidean distance
def h(curr, goal):
    Cx, Cy = curr[0], curr[1]
    Gx, Gy = goal[0], goal[1]
    return pow( (Cx - Gx)**2 + (Cy - Gy)**2, 1/2 )

def g(curr, gmap):
    return gmap[curr]

def f(curr, goal, gmap):
    return g(curr, gmap) + h(curr, goal)

# Credit: wikipedia
def AStar(start, goal, A, B):

    # Set of explored points so far
    explored = {} # will contain points (x, y)

    frontier_minh = []
    frontier_minhl = []
    
    gmap = {}
    gmap[start] = 0


    heapq.heappush(frontier_minh, (0, start))
    heapq.heappush(frontier_minhl, (0, ''))

    pressA = 0
    pressB = 0

    while (frontier_minh and pressA <= 100 or pressB <= 100):
       
        # find the lowest f score value in the frontier
        
        curr = heapq.heappop(frontier_minh)[1]
        button = heapq.heappop(frontier_minhl)[1]

        if button == "A":
            pressA += 1
        elif button == "B":
            pressB += 1

        # found the lowest score, now add to explored
        explored[curr] = True
        
        # found the goal in the lowest node of the frontier!
        if curr == goal:
            return gmap[curr]

        # now add neighbors to the frontier
        AState = ( curr[0] + A[0], curr[1] + A[1] )
        BState = ( curr[0] + B[0], curr[1] + B[1] )

        toAGScore = gmap[curr] + 3
        toBGScore = gmap[curr] + 1
    
        # If we haven't seen AState or the alternative path is better
        if AState not in gmap or toAGScore < gmap[AState]:
            gmap[AState] = toAGScore
            if AState not in explored:
                heapq.heappush(frontier_minh, (f(AState, goal, gmap), AState))
                heapq.heappush(frontier_minhl, (f(AState, goal, gmap), "A"))

        # If we haven't seen BState or the alternative path is better
        if BState not in gmap or toBGScore < gmap[BState]:
            gmap[BState] = toBGScore
            if BState not in explored:
                heapq.heappush(frontier_minh, (f(BState, goal, gmap), BState))
                heapq.heappush(frontier_minhl, (f(BState, goal, gmap), "B"))

    return 0

@timing
def part1(fname):
    f = open(fname).read()

    # WRONG - 28735
    # WRONG - 21009

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
       

        # Adding the cleaned up version to machines_clean
        machines_clean.append( ( (Ax, Ay), (Bx, By), (Px, Py) ) )
    
    machines = machines_clean.copy()
    
    # Run AStar with each machine
    costs = []
    for machine in tqdm(machines):

        goal = (machine[2][0], machine[2][1])
        A, B = machine[0], machine[1]
        costs.append(AStar((0, 0), goal, A, B))

    return sum(costs)



@timing
def part2(fname):

    return 0

if __name__ == "__main__":
    main()
