# Day 1

The problems were OK.

Part1 was really easy whereas Part2 took some thinking. I was able to do part1 by creating two lists, sorting both, then getting the difference of each pair of ints.

Part2 was not too hard. All we had to do was make a map of the second items with each index being the number itself, and the value being the number of times it appears. Then, we iterate through each number in list1 and check if it is in the map. If it is, then I compute that number times the count.

Final solution: [./day1](./day1/)

# Day 2

I did okay, but took significantly longer than day1. For the solution, my first and second attempt look dirty but they are actually time same time complexity as my most polished answer. I just took the time to make them look more Pythonic!

Final solution: [./day2](./day2)

# Day 3

Part 1 was easy, but I really dropped the ball on part 2! It took me a whole **2 hours** to finish it. However, it was mostly because my experience with Regex is a little shaky. I was able to get a regex that removed everything between a `don't()` and a `do()`, including multiple predicate `don't()`'s.

The problems were the following:

1. I was not deleting characters like `\t`, `\n`, `\r\n` before actually removing the strings. I promptly fixed that up.
2. My regex was not removing a `don't()` followed by `.*` followed by `EOF`. So I added `(?:do\(\)|$)` at the end of my regex to handle that.

It took about 10 attempts.

Final two regex removals:
```python
res = re.sub(r"\n|\t|\r\n", " ", x)
res = re.sub(r"don't\(\).*?(?:do\(\)|$)", "BUFF", res)
```

Final solution: [./day3](./day3)

# Day 4

Today was ROUGH because I did not know about Python's strides capabilities. But overall I really enjoyed the problems and learned A LOT about how to grid search for words. I will definitely be using this knowledge for problems in the future.

Part 1 required understanding strides and how to grab a stubstring by non contiguous index.

Part 2 required the same knowledge but applied in a different way. After understanding how strides work, it was basically problem solving :)

---

**Credit:** [Ben](https://gist.github.com/TheThirdOne) and [Bradley](https://gist.github.com/bradleymoore111/) for helping me with their approach!

---

Final solution: [./day4](./day4)

# Day 5

Today was actually great. I started a day late because I did day4 very late. Figuring out the actual brute force solution was quick, and I don't think it was too inefficient because of early abort in part1. In part2, it was efficient because the algorithm did not require me to iterate through each item in update in an O(n^2) complexity.

Final solution: [./day5](./day5)

# Timekeeping

```
      --------Part 1--------   --------Part 2--------
Day       Time   Rank  Score       Time   Rank  Score
  5       >24h  73915      0       >24h  64489      0
  4       >24h  83612      0       >24h  76829      0
  3   00:10:05   4212      0   02:18:46  18641      0
  2   00:18:17   6285      0   00:36:39   5637      0
  1   00:11:44   4791      0   00:29:48   6691      0
```