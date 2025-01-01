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

# Modification of dijkstra to output ALL possible paths between two nodes
def dijkstra(state, start, end):
    dist = {}
    from_map = {}
    frontier = []
    explored = {}
    
    heapq.heappush(frontier, (0, (start, start)))
    dist[start] = 0

    # print("test")
    while frontier:

        # print(frontier)
        curr_list = pop_all_smallest(frontier) 
        # print("popping")
        # for c in curr_list:
        #     print(f"c: {c}")
        # # print("c: ", curr_list)
        # print("")

        for i, popped in enumerate(curr_list):
    
            curr = popped[1][1]
            last = popped[1][0]

            x, y = curr
            explored[last, curr] = True
            explored[curr, last] = True
            # print(f"exploring {last}->{curr}")

            # explore neighbors if possible
            explore_east  = state[y][x+1] != "#" and ((x+1, y), curr) not in explored# and (curr, (x+1, y)) not in explored
            explore_north = state[y-1][x] != "#" and ((x, y-1), curr) not in explored# and (curr, (x, y-1)) not in explored
            explore_west  = state[y][x-1] != "#" and ((x-1, y), curr) not in explored# and (curr, (x-1, y)) not in explored
            explore_south = state[y+1][x] != "#" and ((x, y+1), curr) not in explored# and (curr, (x, y+1)) not in explored
            
            # check direction based on where curr is coming from!
            if (curr == start):
                direction = "E"
            else:
                direction = get_direction(last, curr)

            if explore_east:
                toScore = dist[curr] + 1
                if direction == "N" or direction == "S":
                    toScore += 1000
                if (x+1, y) not in dist or toScore <= dist[(x+1, y)]: # found more optimal path
                    if (x+1, y) not in from_map:
                        from_map[(x+1, y)] = [curr]
                    else:
                        from_map[(x+1, y)].append(curr)
                    dist[(x+1, y)] = toScore
                    if direction == "N" or direction == "S":
                        dist[(x, y)] = toScore - 1
                    heapq.heappush(frontier, (toScore, (curr, (x+1, y))))

            if explore_north:
                toScore = dist[curr] + 1
                if direction == "E" or direction == "W":
                    toScore += 1000
                if (x, y-1) not in dist or toScore <= dist[(x, y-1)]: # found more optimal path
                    if (x, y-1) not in from_map:
                        from_map[(x, y-1)] = [curr]
                    else:
                        from_map[(x, y-1)].append(curr)
                    dist[(x, y-1)] = toScore
                    if direction == "E" or direction == "W":
                        dist[(x, y)] = toScore - 1
                    heapq.heappush(frontier, (toScore, (curr, (x, y-1))))

            if explore_west:
                toScore = dist[curr] + 1                
                if direction == "N" or direction == "S":
                    toScore += 1000
                if (x-1, y) not in dist or toScore <= dist[(x-1, y)]: # found more optimal path
                    if (x-1, y) not in from_map:
                        from_map[(x-1, y)] = [curr]
                    else:
                        from_map[(x-1, y)].append(curr)
                    dist[(x-1, y)] = toScore
                    if direction == "N" or direction == "S":
                        dist[(x, y)] = toScore - 1
                    heapq.heappush(frontier, (toScore, (curr, (x-1, y))))

            if explore_south:
                toScore = dist[curr] + 1
                if direction == "E" or direction == "W":
                    toScore += 1000
                if (x, y+1) not in dist or toScore <= dist[(x, y+1)]: # found more optimal path
                    if (x, y+1) not in from_map:
                        from_map[(x, y+1)] = [curr]
                    else:
                        from_map[(x, y+1)].append(curr)
                    dist[(x, y+1)] = toScore
                    if direction == "E" or direction == "W":
                        dist[(x, y)] = toScore - 1
                    heapq.heappush(frontier, (toScore, (curr, (x, y+1))))

    return from_map 


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

# breadth-first-search my acyclic graph to count the nodes!
def count_spots(from_map, start):

    frontier = []
    explored = {}
    frontier.insert(0, start)
    count = 0
    spots = []
    
    while frontier:
        # grab last element, pop it out
        curr = frontier.pop()
        count += 1
        spots += [curr]
       
        if curr not in from_map:
            break

        # all the neighbors
        for neighbor in from_map[curr]:

            # only will visit if it hasn't been explored already
            if neighbor not in explored:
                explored[neighbor] = True
                frontier.insert(0, neighbor)

    return count, spots

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
@timing
def part2(fname):
    f = open(fname).read().strip()

    state = [ list(x) for x in f.split("\n") ]
    width = len(state[0])
    height = len(state)

    start, goal = get_start_end_pos(state, width, height)
    
    print(start, goal)
    
    from_map = dijkstra(state, start, goal)

    # traversed = traversed_state(state, count_spots(from_map, start, goal))
    
    # print("   " + "".join([str(i) for i in range(10)]))
    # for i, s in enumerate(traversed):
    #     print(f"{i:<2} " + "".join(s))
    # print("   " + "".join([str(i) for i in range(10)]))
    
    count, spots = count_spots(from_map, goal)

    traversed = traversed_state(state, spots)

    for i, s in enumerate(traversed):
        print("".join(s))

    print(len(set(spots)))
 
    return count

if __name__ == "__main__":
    main()
