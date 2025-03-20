from functools import cmp_to_key

def main():
    print("Part1: ", part1())
    print("Part2: ", part2())

# Given the order map, determines if the
# update follows the ordering rules
def correct_order(up, order_map):
    err = False
    for i in range(0, len(up)): # iterate through each num
        for j in range(0, i):   # iterate up to and not including i
            if up[i] not in order_map: continue           # not found in order map, meaning no need to worry about it
            if up[j] not in order_map[up[i]]: continue    # item j was not found in order_map[item i], no rule, move on
            if order_map[up[i]][up[j]]: err = True; break # found an error in the ordering
    return not err

# Brute force approach :D
# For every item i in the ordering, we check whether i-1...0 must come before i.
def part1():
    f = open("main.txt").read()
    sep = f.find("\n\n")

    updates = f[sep+2:].split("\n")
    orders  = f[:sep].split("\n")

    # convert to ints, make the format more readable
    updates = [ list(map(int, update.split(","))) for update in updates ]
    orders  = [ tuple(map(int, order.split("|"))) for order in orders   ]

    # Make a map with the orderings
    order_map = {}
    for l,r in orders:
        if l not in order_map:
            order_map[l] = {}
        order_map[l][r] = True

    # Check if the order is correct
    sum = 0
    for up in updates:
        if correct_order(up, order_map): sum += up[len(up) // 2]
    return sum

# Compares between two objects.
def order_comparator(x, y, map):
    if x not in map:    return 0    # x and y independent
    if y not in map[x]: return 0    # x and y independent
    if map[x][y]:       return -1   # x should come before y, whoops
    else:               return 1    # x and y are fine

# Orders the update based on custom comparator
def ordered_up(up, order_map):
    return sorted(up, key=cmp_to_key(lambda l, r: order_comparator(l, r, order_map)))

# Brute force again
# For every update, check if it's correctly ordered. If not, use the custom comparator
# which uses the order_map to make decisions on whether to move or not
def part2():
    f = open("main.txt").read()
    sep = f.find("\n\n")

    updates = f[sep+2:].split("\n")
    orders  = f[:sep].split("\n")

    # convert to ints, make the format more readable
    updates = [ list(map(int, update.split(","))) for update in updates ]
    orders  = [ tuple(map(int, order.split("|"))) for order in orders   ]

    # Make a map with the orderings
    order_map = {}
    for l,r in orders:
        if l not in order_map:
            order_map[l] = {}
        order_map[l][r] = True

    # Check if the order is incorrect, order and add sum
    sum = 0
    for up in updates:
        if not correct_order(up, order_map): up = ordered_up(up, order_map); sum += up[len(up) // 2]
    return sum

if __name__ == "__main__":
    main()