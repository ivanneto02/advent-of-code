import sys
import time
from tqdm import tqdm

def timing(func):
    def wrapper(*arg, **kw):
        t1 = time.time()
        result = func(*arg, **kw)
        t2 = time.time()
        return (t2 - t1), result, func.__name__
    return wrapper

'''Keeps track of each Point object on a grid'''
class Grid:
    def __init__(self, grid):
        self.points = []

        # add each Point to self.points
        for j in range(len(grid)):
            self.points.append([])
            for i in range(len(grid[0])):
                self.points[j].append(Point(i, j, grid[j][i]))

        self.sum = 0

    def print(self, end="\n"):
        for j in range(len(self.points)):
            for i in range(len(self.points[0])):
                print(self.points[j][i].val, end=" ")
            print("")
        print("", end=end)
    
    def val(self, i, j): return self.points[j][i].val

'''Keeps track of i, j, val, and whether it has been explored'''
class Point:
    def __init__(self, i, j, val):
        self.i = i
        self.j = j
        self.val = val
        self.explored = False

    def explore(self): self.explored = True
    def print(self, end="\n"): print(f"({self.i}, {self.j})", end=end)

'''Start at a point and move in a Depth-First way until we run out of points of the same character'''
def dfs(grid, i, j):

    h = len(grid.points)
    w = len(grid.points[0])
    
    stack = [grid.points[j][i]]
    points = [grid.points[j][i]]
    grid.points[j][i].explore()

    while len(stack):
        point = stack.pop()

        # visit node (find if it's part of the group, or stop. Explore if it is part, or continue if it's not)

        # left adjacent
        if (point.i - 1 >= 0):
            next_pt = grid.points[point.j][point.i - 1]
            if next_pt.val == point.val and not next_pt.explored:
                next_pt.explore(); stack.append(next_pt); points.append(next_pt)

        # right adjacent
        if (point.i + 1 < w):
            next_pt = grid.points[point.j][point.i + 1]
            if next_pt.val == point.val and not next_pt.explored:
                next_pt.explore(); stack.append(next_pt); points.append(next_pt)

        # up adjacent
        if (point.j - 1 >= 0):
            next_pt = grid.points[point.j - 1][point.i]
            if next_pt.val == point.val and not next_pt.explored:
                next_pt.explore(); stack.append(next_pt); points.append(next_pt)
            
        # down adjacent
        if (point.j + 1 < h):
            next_pt = grid.points[point.j + 1][point.i]
            if next_pt.val == point.val and not next_pt.explored:
                next_pt.explore(); stack.append(next_pt); points.append(next_pt)

    return points

def main():
    n = len(sys.argv)

    fname = "test.txt"
    if n > 1: fname = sys.argv[1]

    p1 = part1(fname)
    p2 = part2(fname)

    print(f"Part1: {p1[1]} ({p1[0]*1000}ms)")
    print(f"Part1: {p2[1]} ({p2[0]*1000}ms)")

# Look at all 4 possible spots, 
def neighbors(grid, point, h, w):

    left  = None
    up    = None
    right = None
    down  = None

    i = point.i
    j = point.j

    if (i - 1 >= 0): left  = grid.points[j][i - 1]
    if (j - 1 >= 0): up    = grid.points[j - 1][i]
    if (i + 1 < w ): right = grid.points[j][i + 1]
    if (j + 1 < h ): down  = grid.points[j + 1][i]

    return [left, up, right, down]

# iterate through every point, add 1 to perimeter
# if the letter in the neighbors of each point is
# not equal to A.
def calculate_perimeter(grid, group, h, w):
    perimeter = 0
    for point in group:
        for neighbor in neighbors(grid, point, h, w):
            if neighbor == None: perimeter += 1
            elif neighbor.val != point.val: perimeter += 1
    return perimeter

@timing
def part1(fname):

    # create a grid with the points
    f = open(fname).read()
    grid = f.split("\n")
    grid = [ list(x) for x in grid ]
    height = len(grid)
    width = len(grid[0])
    grid = Grid(grid)

    groups = []

    # Run BFS for every point, find all the known points and add them all to each group if it hasn't been explored
    for j in tqdm(range(len(grid.points))):
        for i in range(len(grid.points[0])):
            if not grid.points[j][i].explored:
                group_points = dfs(grid, i, j)
                groups.append(group_points)

    areas = []
    for group in groups:
        areas.append(len(group))

    perimeters = []
    for group in groups:
        perimeters.append(calculate_perimeter(grid, group, height, width))

    return sum([s*m for s,m in zip(areas, perimeters)])

def unrelated_neighbor(point, neighbor):
    return neighbor == None or point.val != neighbor.val

def calculate_sides(grid, group, height, width):

    sides = 0
    val = group[0].val

    for run in range(2):
        for i in range(width):
            count, found = 0, False
            for j in range(height):
                point, neighbor = grid.points[j][i], None
                if (i - 1 >= 0): neighbor = grid.points[j][i - 1]
                if not found:
                    if point.val == val and (point in group) and unrelated_neighbor(point, neighbor):
                        found = True; count += 1
                else:
                    if point.val == val and (point in group) and unrelated_neighbor(point, neighbor): continue
                    else: found = False
            sides += count
        
        # reverse the grid horizontally
        grid.points = [ x[::-1] for x in grid.points ]
    
    for run in range(2):
        for j in range(height):
            count, found = 0, False
            for i in range(width):
                point, neighbor = grid.points[j][i], None
                if (j - 1 >= 0): neighbor = grid.points[j - 1][i]
                if not found:
                    if point.val == val and (point in group) and unrelated_neighbor(point, neighbor):
                        found = True; count += 1
                else:
                    if point.val == val and (point in group) and unrelated_neighbor(point, neighbor): continue
                    else: found = False
            sides += count
        
        # reverse the grid vertically
        grid.points = grid.points[::-1]
    
    return sides

# def calculate_sides(grid, group, height, width):
#     sides = 0
#     val = group[0].val

#     for i in range(width):
#         count, found = 0, False
#         for j in range(height):
#             point, neighbor = grid.points[j][i], None
#             if (i - 1 >= 0): neighbor = grid.points[j][i - 1]
#             if not found:
#                 if point.val == val and (point in group) and unrelated_neighbor(point, neighbor):
#                     found = True; count += 1
#             else:
#                 if point.val == val and (point in group) and unrelated_neighbor(point, neighbor): continue
#                 else: found = False
#         sides += count

#     for i in range(width - 1, -1, -1):
#         count, found = 0, False
#         for j in range(height):
#             point, neighbor = grid.points[j][i], None
#             if (i + 1 < width): neighbor = grid.points[j][i + 1]
#             if not found:
#                 if point.val == val and (point in group) and unrelated_neighbor(point, neighbor):
#                     found = True; count += 1
#                 # else:
#                 #     found = False; count += 1
#             else:
#                 if point.val == val and (point in group) and unrelated_neighbor(point, neighbor): continue
#                 else: found = False
#         sides += count


#     for j in range(height):
#         count, found = 0, False
#         for i in range(width):
#             point, neighbor = grid.points[j][i], None
#             if (j - 1 >= 0): neighbor = grid.points[j - 1][i]
#             if not found:
#                 if point.val == val and (point in group) and unrelated_neighbor(point, neighbor):
#                     found = True; count += 1
#                 # else:
#                 #     found = False; count += 1
#             else:
#                 if point.val == val and (point in group) and unrelated_neighbor(point, neighbor): continue
#                 else: found = False
#         sides += count


#     for j in range(height - 1, -1, -1):
#         count, found = 0, False
#         for i in range(width):
#             point, neighbor = grid.points[j][i], None
#             if (j + 1 < height): neighbor = grid.points[j + 1][i]
#             if not found:
#                 if point.val == val and (point in group) and unrelated_neighbor(point, neighbor):
#                     found = True; count += 1
#                 # else:
#                 #     found = False; count += 1
#             else:
#                 if point.val == val and (point in group) and unrelated_neighbor(point, neighbor): continue
#                 else: found = False
#         sides += count

#     # we may have continued until the end, so we should add to sides one more time
#     return sides

@timing
def part2(fname):

    # create a grid with the points
    f = open(fname).read()
    grid = f.split("\n")
    grid = [ list(x) for x in grid ]
    height = len(grid)
    width = len(grid[0])
    grid = Grid(grid)

    groups = []

    # Run BFS for every point, find all the known points and add them all to each group if it hasn't been explored
    for j in tqdm(range(len(grid.points))):
        for i in range(len(grid.points[0])):
            if not grid.points[j][i].explored:
                group_points = dfs(grid, i, j)

                groups.append(group_points)

    areas = []
    for group in groups:
        areas.append(len(group))

    perimeters = []
    for group in tqdm(groups):
        perimeters.append(calculate_sides(grid, group, height, width))

    return sum([s*m for s,m in zip(areas, perimeters)])

if __name__ == "__main__":
    main()