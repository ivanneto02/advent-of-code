# Day 12

Final answer in Python:

## Part 1:

```python
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
```

## Part 2:

```python
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
```
