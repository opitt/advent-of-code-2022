# https://adventofcode.com/2022/day/20
from copy import deepcopy
import os
from time import time
from rich import print


def solve(nums, decryption_key, mixit):
    # number = [(index, number), ...]
    zero = (nums.index(0), 0) # store the index of 0 in the org list
    # store the index for each number in the org list
    numbers = [(i, int(n)*decryption_key) for i, n in enumerate(nums)]
    decoded = deepcopy(numbers)

    for _ in range(mixit):
        for n in numbers:
            i = decoded.index(n)
            decoded.pop(i)
            move_to = (i + n[1]) % len(decoded)
            if move_to == 0:
                decoded.append(n)
            else:
                decoded.insert(move_to, n)

    i = decoded.index(zero)
    grove = [decoded[(i + pos) % len(decoded)][1] for pos in (1000, 2000, 3000)]
    res = sum(grove)
    
    print("")
    print("Solution 2 ...:")
    print("  Grove coords: ", *grove)
    print("  sum of coords:", res)


def main(test):

    print("")
    print("****", "TEST" if test else "INPUT", "****************")
    # READ INPUT FILE
    script_path = os.path.dirname(os.path.realpath(__file__))
    filename = "test.txt" if test else "input.txt"
    with open(os.path.join(script_path, filename), encoding="utf-8") as input:
        lines = input.read().strip().split("\n")

    nums = list(map(int, lines))

    # PART 1
    start = time()
    solve(nums, 1, 1)
    print(f"{time() - start:5f} seconds")

    # PART 2
    start = time()
    solve(nums, 811589153, 10)
    print(f"{time() - start:5f} seconds")


main(test=True)  # 3, 1623178306
main(test=False)  # 7278, 14375678667089
