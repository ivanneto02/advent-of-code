# Day 15

# Utilities

I included several utilities for both parts of the problem, and they would be extensive to show here. I include stubs from each, and a link to `utils.py`:

```python
# common
get_initial_robot_pos()

# part 1
make_robot_move()
move_left()
move_up()
move_right()
move_down()

# part 2
wide_make_robot_move()
widen_state()
wide_move_left()
wide_move_up()
wide_move_right()
wide_move_down()
move_boxes_up()
move_boxes_down()
propagate_boxes_up()
propagate_boxes_down()
```

To get more familar, please take a look at my [day 15 utilities](./utils.py)

# Part 1

```python
@timing
def part1(fname):

    f = open(fname).read()

    inputs = f.split("\n\n")

    state = inputs[0]
    state = [ list(x) for x in state.split("\n") ] # griddy on the state

    width = len(state[0])
    height = len(state)

    moves = inputs[1].strip()

    robot_pos = get_initial_robot_pos(state, width, height)

    for move in moves:
        state, robot_pos = make_robot_move(state, move, robot_pos, width, height)

    sum = 0
    # count the coordinates
    for j in range(height):
        for i in range(width):
            if state[j][i] == "O":
                sum += 100 * (j) + i 

    return sum
```

# Part 2

I also included several utilities for part 2, mainly because of the edge cases pre
Solution:

```python
@timing
def part2(fname):
    f = open(fname).read()

    inputs = f.split("\n\n")

    state = inputs[0]
    state = [ list(x) for x in state.split("\n") ] # griddy on the state

    width = len(state[0])
    height = len(state)

    state, width, height = widen_state(state, width, height)

    moves = inputs[1].strip()

    robot_pos = get_initial_robot_pos(state, width, height)

    for move in moves:
        state, robot_pos = wide_make_robot_move(state, move, robot_pos, width, height)

    sum = 0
    # count the coordinates
    for j in range(height):
        for i in range(width):
            if state[j][i] == "[":
                sum += 100 * (j) + i 

    return sum
```

# Testing Suite

I had to make an extensive testing suite for this to work well and handle edge cases:

```python
def main():

    suite = unittest.TestSuite()
    runner = unittest.TextTestRunner()

    # Part 1 movement
    suite.addTest(unittest.makeSuite(TestMoveLeft))
    suite.addTest(unittest.makeSuite(TestMoveUp))
    suite.addTest(unittest.makeSuite(TestMoveRight))
    suite.addTest(unittest.makeSuite(TestMoveDown))

    # Part 2 movement
    suite.addTest(unittest.makeSuite(TestWideMoveLeft))
    suite.addTest(unittest.makeSuite(TestWideMoveUp))
    suite.addTest(unittest.makeSuite(TestWideMoveRight))
    suite.addTest(unittest.makeSuite(TestWideMoveDown))

    # Part 2 utility
    suite.addTest(unittest.makeSuite(TestPropagation))
    suite.addTest(unittest.makeSuite(TestWidenState))

    # Common
    suite.addTest(unittest.makeSuite(TestGetInitialPosition))

    runner.run(suite)
```
Note: full code [here](./test.py)


1. [Part 1 Testing Suite](./test_thin.py)
2. [Part 2 Testing Suite](./test_wide.py)
3. [Common Utilities Testing Suite](./test_common.py)
