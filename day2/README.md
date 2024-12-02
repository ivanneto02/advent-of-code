# Day 2

Final answer in Python:

## Part 1:

```python
def part1():
    f = open("input.txt")

    sum = 0
    for nums in [ list(map(int, x.split(" "))) for x in f ]:
        test1 = all(l < r for l,r in zip(nums, nums[1:])) # increasing test
        test2 = all(l > r for l,r in zip(nums, nums[1:])) # decreasing test
        test3 = all( (abs(r - l) <= 3 and abs(r - l) >= 1) for l,r in zip(nums, nums[1:])) # within bounds test
        sum += 1 if ((test1 or test2) and test3) else 0

    return sum
```

## Part 2:

```python
def part2():
    f = open("input.txt")

    sum = 0
    for nums in [ list(map(int, x.split(" "))) for x in f ]:
        test1 = all(l < r for l,r in zip(nums, nums[1:])) # increasing test
        test2 = all(l > r for l,r in zip(nums, nums[1:])) # decreasing test
        test3 = all( (abs(r - l) <= 3 and abs(r - l) >= 1) for l,r in zip(nums, nums[1:])) # within bounds test
        sum += 1 if ((test1 or test2) and test3) else removeOneAndCheck(nums)

    return sum

def removeOneAndCheck(nums):
    for i in range(0, len(nums)):
        newNums = [ nums[j] for j in range(0, len(nums)) if i != j ]
        test1 = all(l < r for l,r in zip(newNums, newNums[1:])) # increasing test
        test2 = all(l > r for l,r in zip(newNums, newNums[1:])) # decreasing test
        test3 = all( (abs(r - l) <= 3 and abs(r - l) >= 1) for l,r in zip(newNums, newNums[1:])) # within bounds test
        if ((test1 or test2) and test3): return 1
    
    return 0
```