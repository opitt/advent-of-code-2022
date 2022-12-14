# https://adventofcode.com/2022/day/15
from rich import print
import os
from time import time

def solve():
    res=0
    print(f"Solution ... {res}")


def main(test):

    print("****", "TEST" if test else "INPUT", "****************")
    # READ INPUT FILE
    script_path = os.path.dirname(os.path.realpath(__file__))
    with open(
        os.path.join(script_path, "test.txt" if test else "input.txt"), encoding="utf-8"
    ) as input:
        lines = input.read().rstrip().split("\n")


    # PART 1
    start = time()
    solve(lines)
    print(time() - start, " seconds")

    # PART 2
    start = time()
    #solve2(lines)
    print(time() - start, " seconds")


main(test=True)  # 
#main(test=False)  # 
