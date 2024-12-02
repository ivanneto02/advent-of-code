# Day 1

The problems were OK.

Part1 was really easy whereas Part2 took some thinking. I was able to do part1 by creating two lists, sorting both, then getting the difference of each pair of ints.

Part2 was not too hard. All we had to do was make a map of the second items with each index being the number itself, and the value being the number of times it appears. Then, we iterate through each number in list1 and check if it is in the map. If it is, then I compute that number times the count.

Final solution: [./day1](./day1/)

# Day 2

I did okay, but took significantly longer than day1. For the solution, my first and second attempt look dirty but they are actually time same time complexity as my most polished answer. I just took the time to make them look more Pythonic!

Final solution: [./day2](./day2)

# Timekeeping

```
      -------Part 1--------   -------Part 2--------
Day       Time  Rank  Score       Time  Rank  Score
  2   00:18:17  6285      0   00:36:39  5637      0
  1   00:11:44  4791      0   00:29:48  6691      0
```