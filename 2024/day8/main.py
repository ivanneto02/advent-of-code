def main():
    print("Part1: ", part1())
    print("Part2: ", part2())

# prints original f alongside all of its
# antinodes. It is useful for debugging.
def print_antinodes(f, antinodes, linelen):
    f = list(f)
    for a in antinodes:
        if f[a] != "." and f[a] != "\n": continue
        f[a] = "#"
    f = "".join(f)
    for i in range(len(f) // linelen): # must divide evenly
        print(f[i*linelen:i*linelen + linelen])

# Iterate through the input, find a lowercase, find all next lowercase(s), replace antinode with # or move on if too far
# Finally count the number of # in the input. We'll do things forward and backward, to find as many antinodes as possible.
def part1():
    f = open("main.txt").read()

    linelen = f.find("\n")  # length of line until \n - 1
    f = f.replace("\n", "") # we want string stream, no newlines

    inputlen = len(f)

    # store all the antinodes, we will get set(list) of this for uniques
    antinodes = []

    # iterate until we find an antenna
    for i, c in enumerate(f):
        if (c != ".") and (c != "#"): # found antenna
            # find other antennas
            for j, n in list(enumerate(f))[i+1:]:
                # if it's an antenna of the same calibration, calculate distance
                # and apply # forward (from j) and backward (from i)

                # x1 = antenna1 x value
                # x2 = antenna2 x value
                x1, x2 = ( i % linelen, j % linelen )

                # change in x1 and x2 based on their x distance
                dx = x1 - x2

                if (n == c): # found antenna pair
                    dist = abs(j - i)
                    if not (i - dist < 0): # out of bounds check
                        if x1 + dx >= 0 and x1 + dx < linelen: antinodes.append(i - dist)
                    if not (j + dist > inputlen + 1): # already accounting for change in y, we don't need y1 and y2, out of bounds check
                        if x2 - dx >= 0 and x2 - dx < linelen: antinodes.append(j + dist)

    # set(list) gets only unique values
    return len(set(antinodes))

def part2():

    f = open("main.txt").read()

    linelen = f.find("\n")  # length of line until \n - 1
    f = f.replace("\n", "") # we want string stream, no newlines

    inputlen = len(f)
    height = inputlen // linelen

    # store all the antinodes, we will get set(list) of this for uniques
    antinodes = []

    # iterate until we find an antenna
    for i, c in enumerate(f):
        if (c != ".") and (c != "#"): # found antenna
            # find other antennas
            for j, n in list(enumerate(f))[i+1:]:
                # if it's an antenna of the same calibration, calculate distance
                # and apply # forward (from j) and backward (from i)

                # x1 = antenna1 x value
                # x2 = antenna2 x value
                x1, x2 = ( i % linelen , j % linelen  )
                y1, y2 = ( i // linelen, j // linelen )

                # change in x1 and x2 based on their x distance
                dx, dy = ( x1 - x2, y1 - y2 )

                if (n == c): # found antenna pair
                    dist = abs(j - i)

                    t = i
                    # place #, dx, dy away from x1,y1 until out of bounds
                    while x1 >= 0 and x1 < linelen and y1 >= 0 and y1 < height:
                        antinodes.append(t)
                        t -= dist; x1 += dx; y1 += dy

                    t = j
                    # need to change dx away from x2 until out of bounds
                    while x2 >= 0 and x2 < linelen and y2 >= 0 and y2 < height:
                        antinodes.append(t)
                        t += dist; x2 -= dx; y2 -= dy

    # set(list) gets only unique values
    # print_antinodes(f, antinodes, linelen)
    return len(set(antinodes))

if __name__ == "__main__":
    main()