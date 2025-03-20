from tqdm import tqdm

def main():
    print("Part1: ", part1())
    print("Part2: ", part2())

# Iterate through each number, creating a representation of the file system. Add empty-space-size number of spaces
# to the string. Then move all file blocks to the leftmost available spaces!
def part1():

    f = open("main.txt").read().strip()
    blocks = list(map(int, f))

    # Create the representation string
    repr = []
    file_id = 0
    for i, b in enumerate(blocks):
        if i % 2 == 0: # b block file
            repr += [ str(file_id) ] * b
            file_id += 1
            continue
        repr += ["."] * b

    # Move all file blocks to the left
    start = 0
    end = len(repr) - 1
    while (start <= end): # place repr[end] at each available space :)
        if repr[end] == ".": # skip, "." should be ignored
            end -= 1; continue
        if repr[start] == ".": # we can swap with the ending block
            repr[start] = repr[end]
            repr[end] = "."
            start += 1; end -= 1
        else:
            start += 1

    # Calculate checksum
    return sum([ i * int(c) if c != "." else 0 for i,c in enumerate(repr) ])

# Iterate through each number, creating a representation of the file system. Add empty-space-size number of spaces
# to the string. Then move all file blocks to the leftmost available spaces!
def part2():

    f = open("main.txt").read().strip()
    blocks = list(map(int, f))

    # Create the representation string
    chunks  = []
    file_id = 0
    for i, b in enumerate(blocks):
        if i % 2 == 0: # b block file
            chunks.append([str(file_id)]*b)
            file_id += 1
            continue
        chunks.append(["."]*b)

    # Move all file blocks to the left
    pbar = tqdm(total=len(chunks) - 1)
    end = len(chunks) - 1
    while (end > 0): # place repr[end] at each available space :)

        if chunks[end] == [] or "." in chunks[end]: end -= 1; pbar.update(1); continue # skip if the chunk is not a number
        
        # found a number, now start from the beginning and find a suitable place
        for i in range(end):

            dotidx = -1
            for j in range(len(chunks[i])):
                if chunks[i][j] == ".": dotidx = j; break

            if dotidx != -1 and len(chunks[i][dotidx:]) < len(chunks[end]): continue # we cannot place it in here because not enough space!
            
            # we can place the word here
            if dotidx != -1:
                for j in range(0, len(chunks[end])):
                    chunks[i][dotidx + j] = chunks[end][j]
                    chunks[end][j] = "."
                break # successfully swapped, move on to next end

        # if the for loop finishes, we should subtract 1 from end to move to the next chunk
        end -= 1
        pbar.update(1)

    pbar.close()

    repr = []
    for x in chunks:
        for y in x:
            repr.append(y)

    return sum([ i * int(c) if c != "." else 0 for i,c in enumerate(repr) ])

if __name__ == "__main__":
    main()