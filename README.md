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

# Day 6

Today was okay. I was able to get an efficient solution for part 1 quickly. But, for part 2, I am stuck with a slow solution. It is a pseudo cycle detection by using a map and looking whether the box has been traversed more than twice. In almost all cases, this means it is a cycle. I will probably implement DFS for a proper cycle detection solution.

Final solution: [./day6](./day6)

# Day 7

Today was okay as well. I think the trick was knowing that breadth-first-search graph-based search could work. It was a little slow, maybe a better search algorithm like A* would work better. Part 2 was slow with breadth-first search so I implemented depth-first search. I was also able to catch up today :)

Final solution: [./day7](./day7)

# Day 8

It took me a while to get the solution for part 1 because I misunderstood the prompt. I thought that the "distance" between the two antennas corresponds to the raw number of points in between, not the x and y distance. Thus, I was placing too many antinodes where they would have been out of bounds. After fixing this issue, I got correct answers. I was going to change my code to have a grid-based solution but I opted for a stream of characters instead.

---

**Credit:** [Ben](https://gist.github.com/TheThirdOne) and [Bradley](https://gist.github.com/bradleymoore111/) for helping me with their approach!

---

Final solution: [./day8](./day8)

# Day 9

(4:53 AM). Today was painful. I had an issue with part 1 where I was only taking single-digit numbers into account. After fixing up the issue, I was able to get the right answer. Part 2 was a bit more complicated but nothing insane. It is quadratic complexity, so it takes about 15 seconds to run. However both solutions are pretty straightforward, and involves first creating the "representation" array, then using two different algorithms to move the file blocks to the left.

---

**Credit:** [Ben](https://gist.github.com/TheThirdOne) and [Bradley](https://gist.github.com/bradleymoore111/) for helping me with their approach!

---

Final solution: [./day9](./day9)

# Day 10: :christmas_tree: :santa: :tada:

Today was pretty straightforward. It was clearly a search problem, and I think I could have used any type of searching algorithm. I opted for Depth-First Search since I have experience with it and I find the recursive solution pretty clean. For part 1, it required stopping when reaching the first 9 since we are counting that as a single score. For part 2, it required continuing even after finding the 9, because we want to count all the possible paths from 0 to 9.

Final solution: [./day10](./day10)

# Day 11: :racing_car:

Today was pretty tough, but very rewarding. I learned a lot about the speed advantage of using dictionaries as opposed to regular lists. My solution went from potentially taking hours, being optimized to take milliseconds. I timed part 1, part 2, and a bonus (x10000 blinks):

```
Part 1: 203953                (12.5060ms)
Part 2: 242090118578155       (91.0668ms)
Bonus (x10000) 13640739...    (33697.892189ms)
```

The solution involved storing every newly discovered value into a dictionary where the key is the number on the stone, and the value is its count.

Final solution: [./day11](./day11)

# Day 12: 

Today was pretty tough again. I unfortunately had trouble with both parts, though part 2 came a little easier. The way it works for part 1 is (1) I identify all of the regions in the graph by running Depth-First Search on every unexplored node (and DFS does the job of exploring them as well), (2) then for every group I count all of the nodes that have neighbors in the grid that are not the same character, with the function `calculate_perimeter(grid, group)`. Adding those all up results in the correct pricing answer.

For part 2, it was similar, except now we are using my utility `calculate_sides(grid, group)`. Instead of counting each neighbor that is not the same character as the group, I run an algorithm that iterates over the entire grid. I detect the number of contiguous in-group same-letter characters that have an unrelated neighbor. I concluded that running this same algorithm top to bottom, bottom to top, left to right, and right to left, would correctly give me the number of sides. Thus, I ran the algorithm 4 times to calculate the sides.

I think the difficulty in today was the edge cases...

# Day 13:

This problem was tough for me. Originally, I planned to create an A* based solution where the algorithm finds the shortest path between the initial state (0, 0), and the final state, which is the goal. This approach did not work, and instead I opted to solve a system of equations in the form `a * AXS + b * BXS = GoalX` and `a * AYS + b * BYS = GoalY`. By solving the system, we can do both of the following:

1. Find the lowest amount of tokens needed to get from the initial state to the goal
2. Check whether `a` and `b` are actually integers, thereby ensuring there exists a solution. If we have a solution where either `a` or `b` are not integers, then we know there is no way to get to the goal state from the start state.

# Day 14:

Today's puzzle was okay. I did part 1 very quickly because I figured I can just calculate the final position with the modulo operator. For part 2, I got a little stuck because I figured I should simulate the robots running every second and find when the picture would be symmetrical. However, after running the program for about 10 minutes I realized that (1) the picture may not be symmetrical, and (2) not all robots would be part of the Christmas tree.

After thinking, I decided to simply look at the output to see if I could find any weird patterns. I was able to find a pattern starting at second 39, and increasing by 101 seconds. I simulated every second from 39 to 10,000 with a step of 101. By visually looking at the output, I found the tree at t = 7412 seconds!

Here is what the tree looks like. The output is truncated to fit the page:

```
t = 7412s
................................................................
....................................1...........................
................................................................
................1111111111111111111111111111111.................
................1.............................1......1...1......
................1.............................1.................
................1.............................1.................
1...............1.............................1.................
..1.............1..............1..............1.................
.......1........1.............111.............1.................
................1............11111............1.................
................1...........1111111...........1.................
.........1......1..........111111111..........1.................
................1............11111............1.................
................1...........1111111...........1.................
................1..........111111111..........1....1............
................1.........11111111111.........1.................
................1........1111111111111........1.................
.....1..........1..........111111111..........1.................
................1.........11111111111.........1.................
.........1......1........1111111111111........1.................
................1.......111111111111111.......1.............1...
................1......11111111111111111......1.................
................1........1111111111111........1.................
................1.......111111111111111.......1.................
................1......11111111111111111......1.................
................1.....1111111111111111111.....1.......1.........
................1....111111111111111111111....1.................
................1.............111.............1.................
................1.............111.............1.................
................1.............111.............1.................
1.......1.......1.............................1.................
................1.............................1.................
................1.............................1.................
................1.............................1.................
................1111111111111111111111111111111.................
................................................................
....................1...........................................
```

# Day 15 :anger: :pensive: :persevere: :relieved:

Part 1 was not terribly difficult. There were some edge cases to be aware of, such as pushing multiple boxes at once. The code was not too difficult for this.
    
Where day 15 got really hard was on part 2, dealing with moving multiple boxes at once that all influence each other and may collide with the boundary.
Coding this feature was very difficult for me, as I am not used to dealing with many edge cases. I settled on a recursive solution where we use postOrdertraversal
traversal to propagate the movement of all the boxes after checking if they do not collide with the boundary. To achieve this, I had to create a testing suite
foundfound [here](./day15/test.py). Overall, this was probably the most difficult day for me because of the sheer number of edge cases. However, since I
had a suite that covers basically all cases, I was not too unhappy throughout the process. I was able to quickly correct the code when problems
arose with the test cases.

# Timekeeping

```
      --------Part 1--------   --------Part 2--------
Day       Time   Rank  Score       Time   Rank  Score
 15       >24h  39462      0       >24h  30345      0
 14       >24h  44142      0       >24h  39683      0
 13       >24h  46039      0       >24h  41651      0
 12   02:58:33  11983      0   04:46:49   8154      0
 11   01:57:30  13577      0   05:37:54  16298      0
 10   04:45:43  19265      0   04:56:24  18547      0
  9   03:15:10  14920      0   07:48:58  16695      0
  8   03:14:34  13582      0   04:06:18  14188      0
  7   02:54:17  14085      0   03:27:13  14005      0
  6   19:21:55  61712      0       >24h  44174      0
  5       >24h  73915      0       >24h  64489      0
  4       >24h  83612      0       >24h  76829      0
  3   00:10:05   4212      0   02:18:46  18641      0
  2   00:18:17   6285      0   00:36:39   5637      0
  1   00:11:44   4791      0   00:29:48   6691      0
``` 
