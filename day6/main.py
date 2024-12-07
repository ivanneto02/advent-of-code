
def main():
    print("Part1: ", part1())
    print("Part2: ", part2())

# Moves up and leaves trace, also detects a right turn and adjusts the guard
def move_up(s, l, i):
    if i - l - 1 < 0: s[i] = "X"; return s, None, None      # Check if guard goes out of bounds
    elif s[i - l - 1] == "#": s[i] = ">"; return s, ">", i  # Check if object in path
    s[i - l - 1] = "^"; s[i] = "X"; return s, "^", i-l-1    # Normal movement

# Moves down and leaves trace, also detects a right turn and adjusts the guard
def move_down(s, l, i):
    if (i + l + 1) > (len(s) - 1): s[i] = "X"; return s, None, None # Check if guard goes out of bounds
    elif s[i + l + 1] == "#": s[i] = "<"; return s, "<", i          # Check if object in path
    s[i + l + 1] = "v"; s[i] = "X"; return s, "v", i + l + 1        # Normal movement

# Moves right and leaves trace, also detects a right turn and adjusts the guard
def move_right(s, i):
    if i+1 > len(s) - 1 or s[i+1] == "\n": s[i] = "X"; return s, None, None # Check if guard goes out of bounds
    elif s[i+1] == "#": s[i] = "v"; return s, "v", i                        # Check if object in path
    s[i+1] = ">"; s[i] = "X"; return s, ">", i+1                            # Normal movement

# Moves left and leaves trace, also detects a right turn and adjusts the guard
def move_left(s, i):
    if i-1 < 0 or s[i-1] == "\n":   s[i] = "X"; return s, None, None        # Check if guard goes out of bounds
    elif s[i-1] == "#": s[i] = "^"; return s, "^", i                        # Check if object in path
    s[i-1] = "<"; s[i] = "X"; return s, "<", i-1                            # Normal movement

# Determines if guard is in the game, and returns appropriate i (position), and s (guard state)
def found_guard(screen):
    for s, i in zip(screen, list(range(len(screen)))):
        if (s == "^" or s ==">" or s =="<" or s =="v"): return i, s
    return -1, -1

# Brute force: stride in the direction the guard is facing. Find where # appears (or len if not there). Fill all spots with X, regardless of
# what is there. Once the guard leaves, the input will have X's. Count the X's to get the number of distinct spots.
def part1():

    f = open("test.txt").read() # get input
    length = f.find("\n") # total length of row, including \n
    f = list(f) # list because I want to be able to assign single values within the string

    i, guard = found_guard(f) # initial guard position
    # iterate while we have found the guard so far
    while (guard):
        # determine which way to move, update f, guard, and string
        if   guard == "^": f, guard, i = move_up(f, length, i)
        elif guard == ">": f, guard, i = move_right(f, i)
        elif guard == "<": f, guard, i = move_left(f, i)
        elif guard == "v": f, guard, i = move_down(f, length, i)

    # count the X for distinct spaces
    return f.count("X")

def part2():

    f = open("test.txt").read() # get input
    length = f.find("\n") # total length of row, including \n
    f = list(f) # list because I want to be able to assign single values within the string

    print("".join(f), end="\n\n")

    path = []
    # Iterate to create a path that we will iterate through so that
    # we do not need to iterate n times again
    i, guard = found_guard(f) # initial guard position
    # iterate while we have found the guard so far
    while (guard):
        # determine which way to move, update f, guard, and string
        if   guard == "^": f, guard, i = move_up(f, length, i)
        elif guard == ">": f, guard, i = move_right(f, i)
        elif guard == "<": f, guard, i = move_left(f, i)
        elif guard == "v": f, guard, i = move_down(f, length, i)
        if i: path.append(i)

    sum = 0
    # iterate while we have found the guard so far
    for j in range(0, len(f)):
        newf = list("".join(f))
        i, guard = found_guard(f) # initial guard position
        if newf[j] == "\n" or i == j or newf[j] == "#": continue
        newf[j] = "#"

        point_map = {}
        while (True):
            # determine which way to move, update f, guard, and string
            if   guard == "^": newf, guard, i = move_up(newf, length, i)
            elif guard == ">": newf, guard, i = move_right(newf, i)
            elif guard == "<": newf, guard, i = move_left(newf, i)
            elif guard == "v": newf, guard, i = move_down(newf, length, i)

            if not guard: break

            if i not in point_map:
                point_map[i] = 1
            else:
                if point_map[i] > 5:
                    print("".join(newf), end="\n\n")
                    sum += 1; break
                point_map[i] += 1

        # print("".join(newf), end="\n\n")

    # return the sum of all possible obstructions
    return sum

if __name__ == "__main__":
    main()