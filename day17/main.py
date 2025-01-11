import sys
import time
import heapq


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

    print(f"Part 1: {p1[1]} ({p1[0]*1000:.4f}ms)")
    print(f"Part 2: {p2[1]} ({p2[0]*1000:.4f}ms)")


# OPCODE 0
def adv(registers, op):
    registers["A"] = registers["A"] // (2 ** combo(registers, op))
    return registers


# OPCODE 1
def bxl(registers, literal):
    registers["B"] = registers["B"] ^ literal
    return registers


# OPCODE 2
def bst(registers, op):
    registers["B"] = combo(registers, op) % 8
    return registers


# OPCODE 3
def jnz(registers, ptr, literal):
    if registers["A"] != 0:
        ptr = literal
        return ptr
    return ptr


# OPCODE 4
def bxc(registers, _):  # we ignore 2nd operand
    registers["B"] = registers["B"] ^ registers["C"]
    return registers


# OPCODE 5
def out(registers, op):
    return str(combo(registers, op) % 8)


# OPCODE 6
def bdv(registers, op):
    registers["B"] = registers["A"] // (2 ** combo(registers, op))
    return registers


# OPCODE 7
def cdv(registers, op):
    registers["C"] = registers["A"] // (2 ** combo(registers, op))
    return registers


def combo(registers, op):
    if op == 4:
        return registers["A"]
    elif op == 5:
        return registers["B"]
    elif op == 6:
        return registers["C"]
    return op


@timing
def part1(fname):
    input = open(fname).read().strip().split("\n\n")

    registers = [
        (x.split(" ")[1][0], int(x.split(" ")[2])) for x in input[0].split("\n")
    ]
    registers = dict(registers)
    program = list(map(int, input[1].split(" ")[1].split(",")))

    ops = {0: adv, 1: bxl, 2: bst, 3: jnz, 4: bxc, 5: out, 6: bdv, 7: cdv}

    final_string = ""

    ptr = 0
    while ptr < len(program):
        # i = 0
        # while i < 20:
        instruction = program[ptr]
        arg = program[ptr + 1]

        if instruction == 3:
            oldptr = ptr
            ptr = ops[instruction](registers, ptr, arg)
            if oldptr != ptr:  # we did not jump
                continue

        elif instruction == 5:
            final_string += ops[instruction](registers, arg) + ","

        else:
            registers = ops[instruction](registers, arg)

        ptr += 2
        # i += 1

    final_string = final_string[:-1]
    return final_string


@timing
def part2(fname):
    input = open(fname).read().strip().split("\n\n")

    registers = [
        (x.split(" ")[1][0], int(x.split(" ")[2])) for x in input[0].split("\n")
    ]
    registers = dict(registers)
    program = list(map(int, input[1].split(" ")[1].split(",")))

    ops = {0: adv, 1: bxl, 2: bst, 3: jnz, 4: bxc, 5: out, 6: bdv, 7: cdv}

    # should take a while, 0.2ms per try
    i = 0
    while True:
        registers = registers.copy()
        registers["A"] = i
        final_string = ""
        ptr = 0
        while ptr < len(program):
            instruction = program[ptr]
            arg = program[ptr + 1]

            if instruction == 3:
                oldptr = ptr
                ptr = ops[instruction](registers, ptr, arg)
                if oldptr != ptr:  # we did not jump
                    continue

            elif instruction == 5:
                final_string += ops[instruction](registers, arg) + ","
            else:
                registers = ops[instruction](registers, arg)

            ptr += 2
        final_string = final_string[:-1]
        # print(final_string)
        final_string = list(map(int, final_string.split(",")))
        # print(final_string, program)
        if final_string == program:
            return attempt

    return 0  # not found, should not get here


if __name__ == "__main__":
    main()
