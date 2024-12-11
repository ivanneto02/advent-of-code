import sys
from tqdm import tqdm
import time

def timing(func):
    def wrapper(*arg, **kw):
        t1 = time.time()
        result = func(*arg, **kw)
        t2 = time.time()
        return (t2 - t1), result, func.__name__
    return wrapper

def main():
    n = len(sys.argv)
    fname = "test.txt"
    if n > 1:
        fname = sys.argv[1]

    p1 = part1(fname)
    p2 = part2(fname)
    bo = bonus(fname)

    print(f"Part 1: {p1[1]} ({p1[0]*1000:.4f}ms)")
    print(f"Part 2: {p2[1]} ({p2[0]*1000:.4f}ms)")
    print(f"Bonus (x10000): {bo[1]} ({bo[0]*1000:.6f}ms)")

# Algorithm keeps track of all numbers that have been seen so far. We remove the number in the
# dictionary once we are ready to compute the numbers that result from blinking on it. Then, we add those numbers
# and their counts (the original number's count) to the dictionary. Repeat until the required number of blinks,
# then sum up the values in the dictionary.
def count_stones(fname, blinks=6):

    f = open(fname).read()
    nums = f.split(" ")
    nums_map = {}

    # add initial values
    for num in nums:
        if num not in nums_map: nums_map[num] = 1
        else: nums_map[num] += 1

    # count 75 blinks, process numbers further each time
    for blink in tqdm(range(blinks)):
        # Iterate through each key
        tmp_map = {}
        for key in list(nums_map.keys()):
            # update map based on how the keys could be added to the map
            count = nums_map[key]
            if key == "0":
                # 0, adding "1" to the map
                if "1" not in tmp_map: tmp_map["1"] = count
                else: tmp_map["1"] += count
            elif len(key) % 2 == 0:
                # even length, add left and right to the map
                left = str(int(key[0:len(key)//2]))
                right = str(int(key[len(key)//2:]))
                if left not in tmp_map: tmp_map[left] = count
                else: tmp_map[left] += count
                if right not in tmp_map: tmp_map[right] = count
                else: tmp_map[right] += count
            else:
                # other case, add key * 2024 to the map
                add = str(int(key) * 2024)
                if add not in tmp_map: tmp_map[add] = count
                else: tmp_map[add] += count

            del nums_map[key]

        nums_map = tmp_map.copy()

    # count all values for each key
    return sum(list(nums_map.values()))

@timing
def part1(fname):
    return count_stones(fname, 25)

@timing
def part2(fname):
    return count_stones(fname, 75)

@timing
def bonus(fname):
    return count_stones(fname, 10000)

if __name__ == "__main__":
    main()