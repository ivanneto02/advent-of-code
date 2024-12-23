
# Takes the regular state and makes a widened version of it,
# by extending every character by its defined wide version. Then,
# re-grid the state by combining all the characters and splitting them
# into a list
def widen_state(state, width, height):

    # replace each character with its widened form
    for j in range(height):
        for i in range(width):
            char = state[j][i]
            if char == "@":
                state[j][i] = "@."
            elif char == "O":
                state[j][i] = "[]"
            elif char == "#":
                state[j][i] = "##"
            elif char == ".":
                state[j][i] = ".."

    # now re-split each string to make grid of characters
    return [ list("".join(x)) for x in state ], width*2, height*2

"""
All wide_ utilities apply for part 2 of day 15. It is used for when
we widen the grid.
"""
def wide_move_left(state, robot_pos):    

    x, y = robot_pos

    # check if we have a simple move
    if state[y][x-1] == ".":
        state[y][x] = "."
        state[y][x-1] = "@"
        return state, (x-1, y)

    # complex move, we may stay in place or move boxes
    if state[y][x-1] == "]":
        curr = x - 1
        # move until we reach . or #
        while(state[y][curr] != "."):
            # if we reach a # we have a #[][][] section, robot cannot move
            if state[y][curr] == "#":
                return state, robot_pos
            curr -= 1

        # If we never found a #[][][]@ section, it means we found a #[].[]@ section
        # curr holds the position of the implicitly found .
        for i in range(curr, x):
            state[y][i] = state[y][i+1]
        state[y][x] = "."
        return state, (x-1, y)

    # case where we have #@
    return state, robot_pos

# Causes each push to recursively propagate to each box on each
# side of the main box being pushed. It will be called on the
# box that is being pushed by the robot. The movement function
# is in charge of moving the robot itself.
def propagate_push_up(state, box_pos):
    x, y = box_pos

    # base case, there is ONLY space above the box, could move section
    # we must return a 1 for this particular branch
    if (state[y-1][x] == ".") and (state[y-1][x+1] == "."):
        return 1

    # base case, there is a # above the box, cannot move this box, must
    # propagate return value down to intial box
    if (state[y-1][x] == "#" or state[y-1][x+1] == "#"):
        return 0

    # recursive case where we have two boxes
    if state[y-1][x] == "]" and state[y-1][x+1] == "[":
        return int(propagate_push_up(state, (x-1, y-1)) 
            and propagate_push_up(state, (x+1, y-1)))
    
    # recursive case where we only have one box on left side
    if (state[y-1][x] == "]"):
        # if next propagation doesn't return a state we are safe
        return propagate_push_up(state, (x-1, y-1))

    # recursive case where we only have one box exactly in the middle
    if (state[y-1][x] == "["):
        return propagate_push_up(state, (x, y-1))

    # recursive case where we only have one box on the right side
    if (state[y-1][x+1] == "["):
        return propagate_push_up(state, (x+1, y-1))

    print("case not caught")
    # we should not get here
    return state, box_pos

def wide_move_up(state, robot_pos):
    x, y = robot_pos

    # check if we have a simple move
    if state[y+1][x] == ".":
        state[y+1][x] = "@"
        state[y][x] = "."
        return state, (x, y-1)

    # complex move, we may stay in place or move boxes!
    if state[y-1][x] == "[" or state[y-1][x] == "]":
        
        box_pos = (0,0)
        if state[y-1][x] == "[":
            box_pos = (y-1, x)
        elif state[y-1][x] == "]":
            box_pos = (y-1, x-1)
            
        # we were not able to move the boxes up because of a boundary in the way
        if (propagate_push_up(state, box_pos) == -1):
            return state, (x, y)
        
        # propagating would either return -1 when unable to propagate and do nothing, OR
        # return 0 and be able to propagate. It does the work for us.
        state[x][y-1] = "@"
        return state, (x, y-1)

    return state, robot_pos

def wide_move_right(state, robot_pos):

    x, y = robot_pos

    # check if we have a simple move
    if state[y][x+1] == ".":
        state[y][x] = "."
        state[y][x+1] = "@"
        return state, (x+1, y)

    # complex move, we may stay in place or move boxes
    if state[y][x+1] == "[":
        curr = x + 1
        # move until we reach . or #
        while(state[y][curr] != "."):
            # if we reach a # we have a #[][][] section, robot cannot move
            if state[y][curr] == "#":
                return state, robot_pos
            curr += 1

        # If we never found a #[][][]@ section, it means we found a #[].[]@ section
        # curr holds the position of the implicitly found .
        for i in range(curr, x, -1):
            state[y][i] = state[y][i-1]
        state[y][x] = "."
        return state, (x+1, y)

    # case where we have #@
    return state, robot_pos
def wide_move_down(state, robot_pos):
    return state, robot_pos

def wide_make_robot_move(state, move, robot_pos, width, height):
    if move == "<":
        return wide_move_left(state, robot_pos)
    
    if move == "^":
        return wide_move_up(state, robot_pos)

    if move == ">":
        return wide_move_right(state, robot_pos)

    if move == "v":
        return wide_move_right(state, robot_pos)

    # should not get here
    return state, robot_pos

# Use state to find the robot
# Also applies for wide part 2
def get_initial_robot_pos(state, width, height):
    for j in range(0, height):
        for i in range(0, width):
            if state[j][i] == "@":
                return (i, j)
    return (-1, -1)

# defines left movement 
def move_left(state, robot_pos):
    x, y = robot_pos
    
    # check if we have a simple move
    if state[y][x-1] == ".":
        state[y][x] = "."
        state[y][x-1] = "@"

        return state, (x-1, y)

    # complex move, we may stay in place or move boxes
    if state[y][x-1] == "O":
        # move until we reach . or #
        curr = x - 1
        while (state[y][curr] != "."):
            # if we reach a # we have a #OOOO section, robot cannot move
            if state[y][curr] == "#":
                return state, robot_pos
            curr -= 1
        # If we never found a #OOOO@ section, it means we found a #O.OOO@ section, we are able to move the robot
        # curr holds the position of the implicitly found .
        for i in range(curr, x):
            state[y][i] = state[y][i+1]
        state[y][x] = "."
        return state, (x-1, y)

    # case where we have #@
    return state, robot_pos

# defines left movement 
def move_right(state, robot_pos):
    x, y = robot_pos

    # check if we have a simple move
    if state[y][x+1] == ".":
        state[y][x] = "."
        state[y][x+1] = "@"

        return state, (x+1, y)

    # complex move, we may stay in place or move boxes
    if state[y][x+1] == "O":
        # move until
        curr = x + 1
        while (state[y][curr] != "."):
            # if we reach a # we have a #OOOO section, robot cannot move
            if state[y][curr] == "#":
                return state, robot_pos
            curr += 1
        # If we never found a #OOOO@ section, it means we found a #O.OOO@ section, we are able to move the robot
        # curr holds the position of the implicitly found .
        for i in range(curr, x, -1):
            state[y][i] = state[y][i-1]
        state[y][x] = "."
        return state, (x+1, y)

    # case where we have #@
    return state, robot_pos

# defines left movement 
def move_down(state, robot_pos):
    x, y = robot_pos

    # check if we have a simple move
    if state[y+1][x] == ".":
        state[y][x] = "."
        state[y+1][x] = "@"

        return state, (x, y+1)

    # complex move, we may stay in place or move boxes
    if state[y+1][x] == "O":
        # move until
        curr = y + 1
        while (state[curr][x] != "."):
            # if we reach a # we have a #OOOO section, robot cannot move
            if state[curr][x] == "#":
                return state, robot_pos
            curr += 1
        # If we never found a #OOOO@ section, it means we found a #O.OOO@ section, we are able to move the robot
        # curr holds the position of the implicitly found .
        for j in range(curr, y, -1):
            state[j][x] = state[j-1][x]
        state[y][x] = "."
        return state, (x, y+1)

    # case where we have #@
    return state, robot_pos

# defines upward movement
def move_up(state, robot_pos):
    x, y = robot_pos

    # check if we have a simple move
    if state[y-1][x] == ".":
        state[y][x] = "."
        state[y-1][x] = "@"

        return state, (x, y-1)

    # complex move, we may stay in place or move boxes
    if state[y-1][x] == "O":
        # move until
        curr = y - 1
        while (state[curr][x] != "."):
            # if we reach a # we have a #OOOO section, robot cannot move
            if state[curr][x] == "#":
                return state, robot_pos
            curr -= 1
        # If we never found a #OOOO@ section, it means we found a #O.OOO@ section, we are able to move the robot
        # curr holds the position of the implicitly found .
        for j in range(curr, y):
            state[j][x] = state[j+1][x]
        state[y][x] = "."
        return state, (x, y-1)

    # case where we have #@
    return state, robot_pos

# Uses all state variables to modify the state and robot_pos
def make_robot_move(state, move, robot_pos, width, height):
  
    if move == "<":
        return move_left(state, robot_pos)

    if move == "^":
        return move_up(state, robot_pos)

    if move == ">":
        return move_right(state, robot_pos)

    if move == "v":
        return move_down(state, robot_pos)

    # should not get here
    return (state, robot_pos)
