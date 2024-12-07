# Day 7

Final answer in Python:

## Utilities:

```python
# keeps track of the current left-most operated expression
# all internal nodes will have multiple values in self.exp. Only
# leaf nodes should contain a single value. This corresponds to
# the left-to-right evaluated expression.
class State:
    def __init__(self, exp):
        self.exp = exp
        self.parent = None
        self.children = []
        self.explored = False

    # will expand the state to populate self.children
    def expand(self, flag = 0):
        if self.isLeaf(): return -1 # If we are a leaf, we cannot expand!
        # expand +
        self.children.append(State([ self.exp[0]+self.exp[1] ] + self.exp[2:]))
        # expand *
        self.children.append(State([ self.exp[0]*self.exp[1] ] + self.exp[2:]))
        # expand || if needed
        if flag: self.children.append(State([ int(str(self.exp[0]) + str(self.exp[1])) ] + self.exp[2:]))

    def isLeaf(self): return len(self.exp) == 1

# Debugging utility - it will show you the path from the successful leaf to the parent!
# Be sure to turn off word wrap
def print_path(test, node):
    print(f"[{test:30}] - ", end="")
    while node:
        print(f"{node.exp}({node.explored})", end="->")
        node = node.parent
    print("")
```

## Part 1:

```python
# Breadth-first search of all the states of an expression, until
# we reach a leaf node where the evaluated expression contains
# the value that we should compare against the test. If it is not
# equal to the test, we just keep looking.
def part1():

    f = open("input.txt").read()
    equations = f.split("\n")

    sum = 0
    for eq in tqdm(equations):
        test = int(eq.split(":")[0])
        values = list(map(int, eq.split(":")[1].strip().split(" ")))
        initState = State(values)

        success = False

        # breadth first search :D
        queue = [initState]
        initState.explored = True
        while len(queue):
            # dequeue
            state = queue[len(queue) - 1]
            queue = queue[:len(queue) - 1]
            if (state.isLeaf() != -1) and (len(state.exp) == 1) and (state.exp[0] == test):
                # print_path(test, state) # Debugging utility - uncomment if needed
                success = True; break
            state.expand() # expand the state
            for cstate in state.children:
                if not cstate.explored:
                    cstate.explored = True
                    cstate.parent = state
                    queue = [cstate] + queue # enqueue children state

        if success:
            sum += test

    return sum
```

## Part 2:

```python
# Depth-first search of all the states of an expression, until
# we reach a leaf node where the evaluated expression contains
# the value that we should compare against the test. If it is not
# equal to the test, we just keep looking.
def part2():

    f = open("input.txt").read()
    equations = f.split("\n")

    sum = 0
    for eq in tqdm(equations):
        test = int(eq.split(":")[0])
        values = list(map(int, eq.split(":")[1].strip().split(" ")))
        initState = State(values)

        success = False

        # depth first search :D
        stack = [initState]
        initState.explored = True
        while len(stack):
            # pop from stack
            state = stack[len(stack) - 1]; stack.pop()
            if (state.isLeaf() != -1) and (len(state.exp) == 1) and (state.exp[0] == test):
                # print_path(test, state) # Debugging utility - uncomment if needed
                success = True; break
            if not state.explored: state.explored = True
            state.expand(flag=1) # expand the state
            for cstate in state.children:
                cstate.parent = state
                stack.append(cstate) # push children state

        if success:
            sum += test

    return sum
```

## Extra - Breadth-First Search

It was really slow so I opted for depth-first instead

```python
# Breadth-first search of all the states of an expression, until
# we reach a leaf node where the evaluated expression contains
# the value that we should compare against the test. If it is not
# equal to the test, we just keep looking.
def part2():

    f = open("input.txt").read()
    equations = f.split("\n")

    sum = 0
    for eq in tqdm(equations):
        test = int(eq.split(":")[0])
        values = list(map(int, eq.split(":")[1].strip().split(" ")))
        initState = State(values)

        success = False

        # breadth first search :D
        queue = [initState]
        initState.explored = True
        while len(queue):
            # dequeue
            state = queue[len(queue) - 1]
            queue = queue[:len(queue) - 1]
            if (state.isLeaf() != -1) and (len(state.exp) == 1) and (state.exp[0] == test):
                # print_path(test, state) # Debugging utility - uncomment if needed
                success = True; break
            state.expand(flag=1) # expand the state
            for cstate in state.children:
                if not cstate.explored:
                    cstate.explored = True
                    cstate.parent = state
                    queue = [cstate] + queue # enqueue children state

        if success:
            sum += test

    return sum
```