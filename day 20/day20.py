# https://adventofcode.com/2022/day/20
from copy import deepcopy
import os
from time import time
from rich import print


def solve1(numbers, zero):
    # number = [(index, number), ...]
    result = deepcopy(numbers)
    for number in numbers:
        i = result.index(number)
        result.pop(i)
        move_to = (i + number[1]) % len(result)
        if move_to == 0:
            result.append(number)
        else:
            result.insert(move_to, number)
        #temp = [res[1] for res in result]

    i = result.index(zero)
    res = [result[(i + pos) % len(result)][1] for pos in (1000, 2000, 3000)]
    print("")
    print("Solution 1 ...:")
    print("  Grove coords: ", *res)
    print("  sum of coords:", sum(res))


def solve2(numbers, zero):
    # number = [(index, number), ...]
    result = deepcopy(numbers)
    for mix in range(10):
        for number in numbers:
            i = result.index(number)
            result.pop(i)
            move_to = (i + number[1]) % len(result)
            if move_to == 0:
                result.append(number)
            else:
                result.insert(move_to, number)
            #temp = [res[1] for res in result]

    i = result.index(zero)
    res = [result[(i + pos) % len(result)][1] for pos in (1000, 2000, 3000)]
    print("")
    print("Solution 2 ...:")
    print("  Grove coords: ", *res)
    print("  sum of coords:", sum(res))


def main(test):

    print("")
    print("****", "TEST" if test else "INPUT", "****************")
    # READ INPUT FILE
    script_path = os.path.dirname(os.path.realpath(__file__))
    filename = "test.txt" if test else "input.txt"
    with open(os.path.join(script_path, filename), encoding="utf-8") as input:
        lines = input.read().strip().split("\n")

    zero = (lines.index("0"), 0)

    # PART 1
    start = time()
    numbers = [(i, int(n)) for i, n in enumerate(lines)]
    solve1(numbers, zero)
    print(f"{time() - start:5f} seconds")

    # PART 2
    start = time()
    numbers = [(i, int(n)*811589153) for i, n in enumerate(lines)]
    solve2(numbers, zero)
    print(f"{time() - start:5f} seconds")


main(test=True)  # 3, 1623178306
main(test=False)  # 7278, 14375678667089
