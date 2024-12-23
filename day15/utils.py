
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
    return state, robot_pos
def wide_move_up(state, robot_pos):
    return state, robot_pos

def wide_move_right(state, robot_pos):
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
        # move until
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
