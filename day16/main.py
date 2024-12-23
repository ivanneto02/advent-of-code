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

def make_path(from_map, curr):
    path = []
    while curr != start:
        path.append(curr)
        curr = from_map[curr]
    path.append(start)
    return path[::-1] # reverse

"""
We are assuming a standard coordinate system, where we increase x and y as we move right and up
We also start at (1,1) because of the border.
"""
def AStar(state, start, goal):

    gmap = []
    explored = {}
    from_map = {}
    frontier = []

    heapq.heappush(frontier, (0, (1, 1)))

    gmap[start] = 0

    while frontier:

        # get lowest cost node, remove from frontier
        curr = heapq.heappop(frontier)

        explored[curr] = True

        if curr == goal:
            # reconstruct the path
            return make_path(from_map, curr, start)

        x, y = curr

        # explore neighbors if possible
        explore_east  = state[y][x-1] != "#" and (x-1, y) not in explored
        explore_north = state[y+1][x] != "#" and (x, y+1) not in explored
        explore_west  = state[y][x+1] != "#" and (x+1, y) not in explored
        explore_south = state[y-1][x] != "#" and (x, y-1) not in explored
       
        if explore_east:
            toScore = gmap[curr] + 1
            if (x-1, y) not in gmap or toScore < gmap[(x-1, y)]: # found more optimal path
                from_map[(x-1, y)] = curr
                gmap[(x-1, y)] = toScore
                heapq.heappush((f(gmap, curr, goal) , (x-1, y)))

        if explore_north:


        if explore_west:


        if explore_south:

"""
Strategy: use AStar for lowest cost path finding, then use the reconstructed path to calculate the score by using the equation
number_of_moves + 1000*number_of_turns
"""
@timing
def part1(fname):
    
    
    
    return 0

@timing
def part2(fname):

    return 0

if __name__ == "__main__":
    main()
