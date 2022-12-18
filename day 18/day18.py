# https://adventofcode.com/2022/day/18
import os
from time import time
from rich import print

def solve1(cubes):
    touching = {cube: set() for cube in cubes}

    for cube in cubes:
        for c in cubes:
            if c == cube:
                continue
            if abs(c[0]-cube[0])+abs(c[1]-cube[1])+abs(c[2]-cube[2]) == 1:
                touching[cube].add(c)
                touching[c].add(cube)
    print(sum([6-len(v) for v in touching.values()]))


def main(test):

    print("****", "TEST" if test else "INPUT", "****************")
    # READ INPUT FILE
    script_path = os.path.dirname(os.path.realpath(__file__))
    filename = "test.txt" if test else "input.txt"
    with open(os.path.join(script_path, filename), encoding="utf-8") as input:
        lines = input.readlines()

    cubes = [tuple(map(int, line.split(","))) for line in lines]

    # PART 1
    start = time()
    solve1(cubes)
    print(time() - start, " seconds")

    # PART 2


main(test=True)  # 64,
main(test=False)  # 4282, 
