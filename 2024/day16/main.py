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
    return pow((xc - xe) ** 2 + (yc - ye) ** 2, 1 / 2)


# f_score, f(n) = g(n) + h(n). We will minimize this with a min heap
def f(gmap, curr, end):
    return g(gmap, curr) + h(curr, end)


def make_path(from_map, curr, start):
    path = []
    while curr != start:
        path.append(curr)
        curr = from_map[curr]
    path.append(start)
    return path[::-1]  # reverse


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
        explore_east = state[y][x + 1] != "#" and (x + 1, y) not in explored
        explore_north = state[y - 1][x] != "#" and (x, y - 1) not in explored
        explore_west = state[y][x - 1] != "#" and (x - 1, y) not in explored
        explore_south = state[y + 1][x] != "#" and (x, y + 1) not in explored

        # check direction based on where curr is coming from!
        if curr == start:
            direction = "E"
        else:
            direction = get_direction(from_map[curr], curr)

        if explore_east:
            toScore = gmap[curr] + 1
            if direction == "N" or direction == "S":
                toScore += 1000
            if (x + 1, y) not in gmap or toScore < gmap[
                (x + 1, y)
            ]:  # found more optimal path
                from_map[(x + 1, y)] = curr
                gmap[(x + 1, y)] = toScore
                heapq.heappush(frontier, (f(gmap, (x + 1, y), goal), (x + 1, y)))

        if explore_north:
            toScore = gmap[curr] + 1
            if direction == "E" or direction == "W":
                toScore += 1000
            if (x, y - 1) not in gmap or toScore < gmap[
                (x, y - 1)
            ]:  # found more optimal path
                from_map[(x, y - 1)] = curr
                gmap[(x, y - 1)] = toScore
                heapq.heappush(frontier, (f(gmap, (x, y - 1), goal), (x, y - 1)))

        if explore_west:
            toScore = gmap[curr] + 1
            if direction == "N" or direction == "S":
                toScore += 1000
            if (x - 1, y) not in gmap or toScore < gmap[
                (x - 1, y)
            ]:  # found more optimal path
                from_map[(x - 1, y)] = curr
                gmap[(x - 1, y)] = toScore
                heapq.heappush(frontier, (f(gmap, (x - 1, y), goal), (x - 1, y)))

        if explore_south:
            toScore = gmap[curr] + 1
            if direction == "E" or direction == "W":
                toScore += 1000
            if (x, y + 1) not in gmap or toScore < gmap[
                (x, y + 1)
            ]:  # found more optimal path
                from_map[(x, y + 1)] = curr
                gmap[(x, y + 1)] = toScore
                heapq.heappush(frontier, (f(gmap, (x, y + 1), goal), (x, y + 1)))


def detect_turn(direction, move):
    if direction == "S" or direction == "N":
        return move == "W" or move == "E"
    else:
        return move == "S" or move == "N"


# Modification of dijkstra to output ALL possible paths between two nodes
def dijkstra(state, start, end):
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

        for direction, next in zip(
            ["E", "N", "W", "S"], [(x + 1, y), (x, y - 1), (x - 1, y), (x, y + 1)]
        ):
            if (u, next) in explored or (next, u) in explored:
                continue

            nx, ny = next
            if state[ny][nx] == "#":
                continue

            cost = 1
            if detect_turn(direction, move):
                cost += 1000

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


def opposite_dir(dir):
    opps = {"S": "N", "W": "E", "N": "S", "E": "W"}
    return opps[dir]


def bfs(state, start, goal, dist):
    frontier = []  # queue

    points = []
    explored = {}

    frontier = [(goal, goal)] + frontier

    points.append(goal)

    while frontier:
        l, u = frontier.pop()

        direction = "none"
        if l != u:
            direction = get_direction(l, u)

        x, y = u

        if u in explored:
            continue

        explored[u] = True

        # record neighboring distances
        neighbors = []
        for move, next in zip(
            ["E", "N", "W", "S"], [(x + 1, y), (x, y - 1), (x - 1, y), (x, y + 1)]
        ):
            nx, ny = next
            if state[ny][nx] == "#":
                continue

            neighbors.append((dist[next], move))

        # find lowest neighboring distances
        lowest = neighbors[0]
        for neigh in neighbors:
            if neigh[0] < lowest[0]:  # its distance
                lowest = neigh

        if u != l:
            if lowest[1] != direction:
                dist[u] = dist[l] - 1

        for move, next in zip(
            ["E", "N", "W", "S"], [(x + 1, y), (x, y - 1), (x - 1, y), (x, y + 1)]
        ):
            if next in explored:
                continue

            nx, ny = next
            if state[ny][nx] == "#":
                continue

            nextdist = dist[next]
            if u != l:
                if detect_turn(direction, move):
                    nextdist += 1000

            if nextdist < dist[u] and move != opposite_dir(lowest[1]) and u != start:
                points.append(next)
                frontier = [(u, next)] + frontier

    return points


"""
Strategy: use AStar for lowest cost path finding, then use the reconstructed path to calculate the score by using the equation
number_of_moves + 1000*number_of_turns
"""


@timing
def part1(fname):
    f = open(fname).read().strip()

    state = [list(x) for x in f.split("\n")]
    width = len(state[0])
    height = len(state)

    start, goal = get_start_end_pos(state, width, height)

    _, score = AStar(state, start, goal)

    return score


@timing
def part2(fname):
    f = open(fname).read().strip()

    state = [list(x) for x in f.split("\n")]
    width = len(state[0])
    height = len(state)

    start, goal = get_start_end_pos(state, width, height)

    _, dist = dijkstra(state, start, goal)

    # after running dijkstra we now have a map dist[node] = distance
    # we can traverse the state backwards and only add points if the distance to the next
    # node is <= the current distance. We begin with the distance at the goal and traverse
    # all the way until start.
    points = bfs(state, start, goal, dist)

    return len(set(points))


if __name__ == "__main__":
    main()
