# Day 3

Final answer in Python:

```python
def answer():
    f = open("input.txt")

    sum = 0
    for nums in [ list(map(int, x.split(" "))) for x in f ]:
        test1 = all(l < r for l,r in zip(nums, nums[1:])) # increasing test
        test2 = all(l > r for l,r in zip(nums, nums[1:])) # decreasing test
        test3 = all( (abs(r - l) <= 3 and abs(r - l) >= 1) for l,r in zip(nums, nums[1:])) # within bounds test
        sum += 1 if ((test1 or test2) and test3) else 0

    return sum
```