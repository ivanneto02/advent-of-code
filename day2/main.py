

def main():
    print("Part1 orig: ", part1original())
    print("Part2 orig: ", part2original(), "\n")

    print("Part1 impr1: ", part1impr1())
    print("Part2 impr1: ", part2())

    print("Part1 impr2: ", part1impr2())
    print("Part2 impr2: ", part2())
    return 0

# My final answer :)
def part1impr2():
    f = open("main.txt")

    sum = 0
    for nums in [ list(map(int, x.split(" "))) for x in f ]:
        test1 = all(l < r for l,r in zip(nums, nums[1:])) # inc
        test2 = all(l > r for l,r in zip(nums, nums[1:])) # dec
        test3 = all( (abs(r - l) <= 3 and abs(r - l) >= 1) for l,r in zip(nums, nums[1:]))
        sum += 1 if ((test1 or test2) and test3) else 0

    return sum

def part1impr1():

    f = open("main.txt")

    sum = 0
    for line in f:
        nums = [int(x) for x in line.split(" ")]

        inc = True
        dec = True
        dif = True
        for l,r in zip(nums, nums[1:]):
            if (l < r): dec = False
            if (l > r): inc = False
            if (abs(l - r) > 3) or (abs(l - r) < 1): dif = False
        
        if (inc or dec) and dif:
            sum += 1
    
    return sum

def part2():



    return 0

# poop answer
def part1original():

    f = open("main.txt")

    sum = 0

    for line in f:
        
        # do something with each line
        numbers = line.split(" ")

        # print(line)

        # increasing
        inc = True
        for i in range(1, len(numbers)):
            if (int(numbers[i - 1]) > int(numbers[i])):
                inc = False

        dec = True
        for i in range(1, len(numbers)):
            if (int(numbers[i - 1]) < int(numbers[i])):
                dec = False
        
        if (not dec) and (not inc):
            continue
        
        # differences
        within = True
        for i in range(1, len(numbers)):
            dif = abs((int(numbers[i-1])) - int(numbers[i]))
            if (dif == 0 or dif > 3):
                within = False
        
        if (within):
            sum += 1

    return sum


def part2original():
    f = open("main.txt")

    sum = 0

    for line in f:
        
        # do something with each line
        numbers = line.split(" ")

        # increasing
        inc = True
        for i in range(1, len(numbers)):
            if (int(numbers[i - 1]) > int(numbers[i])):
                inc = False

        dec = True
        for i in range(1, len(numbers)):
            if (int(numbers[i - 1]) < int(numbers[i])):
                dec = False
        
        # differences
        within = True
        for i in range(1, len(numbers)):
            dif = abs((int(numbers[i-1])) - int(numbers[i]))
            if (dif == 0 or dif > 3):
                within = False
                break
        
        if ((not dec) and (not inc)) or (not within):
            for i in range(0, len(numbers)):
                updated_nums = []
                for j in range(0, len(numbers)):
                    if (i != j):
                        updated_nums.append(numbers[j])
                    
                # increasing
                iinc = True
                for j in range(1, len(updated_nums)):
                    if (int(updated_nums[j - 1]) > int(updated_nums[j])):
                        iinc = False

                ddec = True
                for j in range(1, len(updated_nums)):
                    if (int(updated_nums[j - 1]) < int(updated_nums[j])):
                        ddec = False
                
                if (not ddec) and (not iinc):
                    continue

                # differences
                wwithin = True
                for j in range(1, len(updated_nums)):
                    diff = abs(int(updated_nums[j-1]) - int(updated_nums[j]))
                    if (diff == 0 or diff > 3):
                        wwithin = False
                        break
                    
                if (wwithin):
                    sum += 1
                    break
        else:
            sum += 1

    return sum





    return 0

if __name__ == "__main__":
    main()