from os import altsep
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
        state[y][x] = "O"
    return state

# based on two points, decide which direction we are moving
def get_direction(last, curr):
    lx, ly = last
    cx, cy = curr
    # Note: y increases going down, so cy > ly means we are moving south
    if lx == cx and cy > ly:
        return "S"
    if lx == cx and ly > cy: 
        return "N"
    if ly == cy and cx > lx:
        return "E"
    if ly == cy and lx > cx:
        return "W"

def AStar(state, start, goal):

    gmap = {}
    explored = {}
    from_map = {}
    frontier = []

    heapq.heappush(frontier, (0, start))

    gmap[start] = 0
    direction = "E"

    while frontier:

        # get lowest cost node, remove from frontier
        popped = heapq.heappop(frontier) 
       
        curr = popped[1]

        explored[curr] = True

        if curr == goal:
            # reconstruct the path
            return make_path(from_map, curr, start), gmap[curr]

        x, y = curr

        # explore neighbors if possible
        explore_east  = state[y][x+1] != "#" and (x+1, y) not in explored
        explore_north = state[y-1][x] != "#" and (x, y-1) not in explored
        explore_west  = state[y][x-1] != "#" and (x-1, y) not in explored
        explore_south = state[y+1][x] != "#" and (x, y+1) not in explored
   
        # check direction based on where curr is coming from!
        if (curr == start):
            direction = "E"
        else:
            direction = get_direction(from_map[curr], curr)
       
        if explore_east:
            toScore = gmap[curr] + 1
            if direction == "N" or direction == "S":
                toScore += 1000
            if (x+1, y) not in gmap or toScore < gmap[(x+1, y)]: # found more optimal path
                from_map[(x+1, y)] = curr
                gmap[(x+1, y)] = toScore
                heapq.heappush(frontier, (f(gmap, (x+1, y), goal) , (x+1, y)))

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
            if (x-1, y) not in gmap or toScore < gmap[(x-1, y)]: # found more optimal path
                from_map[(x-1, y)] = curr
                gmap[(x-1, y)] = toScore
                heapq.heappush(frontier, (f(gmap, (x-1, y), goal) , (x-1, y)))

        if explore_south:
            toScore = gmap[curr] + 1
            if direction == "E" or direction == "W":
                toScore += 1000
            if (x, y+1) not in gmap or toScore < gmap[(x, y+1)]: # found more optimal path
                from_map[(x, y+1)] = curr
                gmap[(x, y+1)] = toScore
                heapq.heappush(frontier, (f(gmap, (x, y+1), goal) , (x, y+1)))

# given a frontier min heap, pop all the smallest values in the heap
def pop_all_smallest(frontier):
    smallest_list = []
    popped = heapq.heappop(frontier)
    val = popped[0] # insert actual smallest value into list
    smallest_list.append(popped)

    # iterate while frontier has elements or until the popped
    # value doesn't match the actual smallest element
    while frontier:
        popped = heapq.heappop(frontier)
        if popped[0] != val:
            heapq.heappush(frontier, (popped[0], popped[1]))
            break
        smallest_list.append(popped)

    return smallest_list

def opposite_direction(direction):
    if direction == "W":
        return "E"
    elif direction == "E":
        return "W"
    elif direction == "N":
        return "S"
    else:
        return "N"

def detect_turn(direction, move):
    if direction == "S" or direction == "N":
        return move == "W" or move == "E"
    else:
        return move == "S" or move == "N"

# Modification of dijkstra to output ALL possible paths between two nodes
def bfs(state, start, end):

    dist = {}
    prev = {}
    frontier = []
    explored = {}
    
    dist[start] = 0

    heapq.heappush(frontier, (0, start, start))
    
    while frontier:

        d, l, u = heapq.heappop(frontier)
        x, y = u

        if l == u:
            move = "E"
        else:
            move = get_direction(l, u)

        if (l, u) in explored:
            continue

        explored[l, u] = True
        explored[u, l] = True

        for direction, next in zip(["E", "N", "W", "S"], [(x+1, y), (x, y-1), (x-1, y), (x, y+1)]):
            
            if (u, next) in explored or (next, u) in explored:
                continue
            
            nx, ny = next
            if state[ny][nx] == "#":
                continue

            cost = 1

            alt = dist[u] + cost

            if next not in dist or alt <= dist[next]:
                heapq.heappush(frontier, (alt, u, next))
                dist[next] = alt
                if next not in prev:
                    prev[next] = [u]
                else:
                    prev[next].append(u)

    return prev, dist

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

def get_smallest_neighbors(curr, from_map, dist):
    distances = []
    for direction in ["E", "N", "W", "S"]:
        if (curr, direction) in dist:
            distances += [dist[(curr, direction)]]

    min_dist = min(distances)

    neighbors = []
    for direction in ["E", "N", "W", "S"]:
        if (curr, direction) in from_map:
            neighbors += [from_map[(curr, direction)]]

    return neighbors

# breadth-first-search my acyclic graph to count the nodes!
def find_all_paths(start, curr, from_map):
    if start == curr:
        return [start]
    else:
        path = [curr]
        for parent in from_map[curr]:
            path += find_all_paths(start, parent, from_map)
        return path

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

    path, score = AStar(state, start, goal)
    
    return score

# TOO LOW - 428
# TOO LOW - 433
# TOO HIGH - 871
# TOO HIGH - 883
@timing
def part2(fname):
    f = open(fname).read().strip()

    state = [ list(x) for x in f.split("\n") ]
    width = len(state[0])
    height = len(state)

    start, goal = get_start_end_pos(state, width, height)
    
    print(start, goal)
    
    prev, dist = bfs(state, start, goal)
  

    # print(dist[((5, 7), "N")])

    # print(from_map)
    # print(dist)

    total_paths = find_all_paths(start, goal, prev)

    for path in total_paths:
        print(path)

    # spots2 = [start]
    # curr = goal
    # while curr != start:
    #     spots2 += [curr]
    #     curr = prev[curr]

    for path in total_paths:
        traversed = traversed_state(state, list(set(path)))
        
        print("   " + "".join([str(i) for i in range(10)])*2)
        for i, s in enumerate(traversed):
            print(f"{i:<2} " + "".join(s))
        print("   " + "".join([str(i) for i in range(10)])*2)
     
    # traversed = traversed_state(state, spots)

    # for i, s in enumerate(traversed):
    #     print("".join(s))

    # print(len(set(spots)))

    return 0

if __name__ == "__main__":
    main()
