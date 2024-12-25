import sys
import time
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

# Cost from beginning of path to the current node
def g(gmap, curr):
    return gmap[curr]

# Euclidean distance heuristic
def h(curr, end):
    xc, yc = curr
    xe, ye = end
    return pow((xc - xe)**2 + (yc - ye)**2, 1/2)

# f_score, f(n) = g(n) + h(n). We will minimize this with a min heap
def f(gmap, curr, end):
    return g(gmap, curr) + h(curr, end)

def make_path(from_map, curr, start):
    path = []
    while curr != start:
        path.append(curr)
        curr = from_map[curr]
    path.append(start)
    return path[::-1] # reverse

# For debugging, returns a state with every point in the path replaced with +
def traversed_state(state, path):
    for point in path:
        x, y = point
        state[y][x] = "+"
    return state

def AStar(state, start, goal):

    gmap = {}
    explored = {}
    from_map = {}
    frontier = []

    heapq.heappush(frontier, (0, start))

    gmap[start] = 0
    direction = "E"
    last = start

    while frontier:

        # get lowest cost node, remove from frontier
        curr = heapq.heappop(frontier)[1]
    
        explored[curr] = True

        if curr == goal:
            # reconstruct the path
            return make_path(from_map, curr, start)

        x, y = curr

        # explore neighbors if possible
        explore_east  = state[y][x-1] != "#" and (x-1, y) not in explored
        explore_north = state[y-1][x] != "#" and (x, y-1) not in explored
        explore_west  = state[y][x+1] != "#" and (x+1, y) not in explored
        explore_south = state[y-1][x] != "#" and (x, y-1) not in explored
    
        # check direction based on where curr is coming from!
       
        if explore_east:
            toScore = gmap[curr] + 1
            if direction == "N" or direction == "S":
                toScore += 1000
            if (x-1, y) not in gmap or toScore < gmap[(x-1, y)]: # found more optimal path
                from_map[(x-1, y)] = curr
                gmap[(x-1, y)] = toScore
                heapq.heappush(frontier, (f(gmap, (x-1,y), goal) , (x-1, y)))

        if explore_north:
            toScore = gmap[curr] + 1
            if direction == "E" or direction == "W":
                toScore += 1000
            if (x, y-1) not in gmap or toScore < gmap[(x, y-1)]: # found more optimal path
                from_map[(x, y-1)] = curr
                gmap[(x, y-1)] = toScore
                heapq.heappush(frontier, (f(gmap, (x, y-1), goal) , (x, y-1)))

        if explore_west:
            toScore = gmap[curr] + 1
            if direction == "N" or direction == "S":
                toScore += 1000
            if (x+1, y) not in gmap or toScore < gmap[(x+1, y)]: # found more optimal path
                from_map[(x+1, y)] = curr
                gmap[(x+1, y)] = toScore
                heapq.heappush(frontier, (f(gmap, (x+1, y), goal) , (x+1, y)))

        if explore_south:
            toScore = gmap[curr] + 1
            if direction == "E" or direction == "W":
                toScore += 1000
            if (x, y+1) not in gmap or toScore < gmap[(x, y+1)]: # found more optimal path
                from_map[(x, y+1)] = curr
                gmap[(x, y+1)] = toScore
                heapq.heappush(frontier, (f(gmap, (x, y+1), goal) , (x, y+1)))
    
def get_start_end_pos(state, width, height):
    spos = (0, 0)
    epos = (0, 0)
    for j in range(height):
        for i in range(width):
            if state[j][i] == "S":
                spos = (i, j)
            elif state[j][i] == "E":
                epos = (i, j)
    return spos, epos

"""
Strategy: use AStar for lowest cost path finding, then use the reconstructed path to calculate the score by using the equation
number_of_moves + 1000*number_of_turns
"""
@timing
def part1(fname):
    
    f = open(fname).read().strip()

    state = [ list(x) for x in f.split("\n") ]
    width = len(state[0])
    height = len(state)

    start, goal = get_start_end_pos(state, width, height)

    path = AStar(state, start, goal)
    
    traversed = traversed_state(state, path)
    
    print("\n")
    for s in state:
        print("".join(s))

    return 0

@timing
def part2(fname):

    return 0

if __name__ == "__main__":
    main()
