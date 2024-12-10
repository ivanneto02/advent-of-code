# Day 10

Final answer in Python:

## Utilities:

```python
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

def diff(grid, i, j, k, l):
    return int(grid.val(i, j)) - int(grid.val(k, l))

'''Special Depth-First Search: only explore 9's because we want to count multiple
paths leading to a single 1 as a score of 1.'''
def DFSpart1(grid, p, h, w):

    # Found a 9, we should explore and add 1 to the sum of 0-to-9 possibilities
    if p.val == "9":
        p.explore()
        grid.sum += 1

    curri = p.i
    currj = p.j

    # add each possible node adjacent to the current node
    if currj > 0 and diff(grid, p.i, p.j - 1, p.i, p.j) == 1:
        edge = grid.points[p.j - 1][p.i]
        if not edge.explored: # In case we've already found the 9
            DFSpart1(grid, edge, h, w)

    if currj < h - 1 and diff(grid, p.i, p.j + 1, p.i, p.j) == 1:
        edge = grid.points[p.j + 1][p.i]
        if not edge.explored: # In case we've already found the 9
            DFSpart1(grid, edge, h, w)

    if curri > 0 and diff(grid, p.i - 1, p.j, p.i, p.j) == 1:
        edge = grid.points[p.j][p.i - 1]
        if not edge.explored: # In case we've already found the 9
            DFSpart1(grid, edge, h, w)

    if curri < w - 1 and diff(grid, p.i + 1, p.j, p.i, p.j) == 1:
        edge = grid.points[p.j][p.i + 1]

        if not edge.explored: # In case we've already found the 9
            DFSpart1(grid, edge, h, w)

'''Special Depth-First Search: no need to explore because the bounds will keep
track of when to end, and since we want to count each possible path as a score
of 1, we do not stop once we have found a 9.'''
def DFSpart2(grid, p, h, w):

    # Found a 9. Do not call p.explore() because we want to account for all
    # the possible paths.
    if p.val == "9":
        grid.sum += 1

    curri = p.i
    currj = p.j

    # add each possible node adjacent to the current node
    if currj > 0 and diff(grid, p.i, p.j - 1, p.i, p.j) == 1:
        edge = grid.points[p.j - 1][p.i]
        # if not edge.explored:
        DFSpart2(grid, edge, h, w)

    if currj < h - 1 and diff(grid, p.i, p.j + 1, p.i, p.j) == 1:
        edge = grid.points[p.j + 1][p.i]
        # if not edge.explored:
        # if not edge.explored:
        DFSpart2(grid, edge, h, w)

    if curri > 0 and diff(grid, p.i - 1, p.j, p.i, p.j) == 1:
        edge = grid.points[p.j][p.i - 1]
        # if not edge.explored:
        # if not edge.explored:
        DFSpart2(grid, edge, h, w)

    if curri < w - 1 and diff(grid, p.i + 1, p.j, p.i, p.j) == 1:
        edge = grid.points[p.j][p.i + 1]
        # if not edge.explored:
        # if not edge.explored:
        DFSpart2(grid, edge, h, w)
```

## Part 1:

```python
def part1(fname):

    f = open(fname).read()

    # make grid - now every point can be expressed as (x, y)
    grid = [ list(line) for line in f.split("\n") ]
    height = len(grid)
    width = len(grid[0])

    score = 0
    for j in range(0, height): # iterate through rows
        for i in range(0, width): # iterate through columns
            # find 0's to start Depth First Search
            if grid[j][i] == "0":
                
                point_grid = Grid(grid)

                # Perform Depth-First Search to locate all the paths to a 9.
                # Explore once we reach a 9 because we do not want to
                # count the multiple 9's
                DFSpart1(point_grid, point_grid.points[j][i], height, width)
                score += point_grid.sum

    return score
```

## Part 2:

```python
def part2(fname):

    f = open(fname).read()

    # make grid - now every point can be expressed as (x, y)
    grid = [ list(line) for line in f.split("\n") ]
    height = len(grid)
    width = len(grid[0])

    score = 0
    for j in range(0, height): # iterate through rows
        for i in range(0, width): # iterate through columns
            # find 0's to start Depth First Search
            if grid[j][i] == "0":
                
                point_grid = Grid(grid)

                # Perform Depth-First Search to locate all the paths to a 9.
                # This time we DO want to count as many 9's as the number
                # of paths.
                DFSpart2(point_grid, point_grid.points[j][i], height, width)
                score += point_grid.sum

    return score
```