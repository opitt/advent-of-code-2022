# https://adventofcode.com/2022/day/22
from collections import defaultdict
import os
from time import time
from rich import print

def solve(elfs):

    def all_empty(elfs, y, x, lookat):
        return all([elfs.get((y+yd, x+xd), 101) == 101 for yd, xd in lookat])

    NORTH = [(-1, -1), (-1, 0), (-1, +1)]
    SOUTH = [(+1, -1), (+1, 0), (+1, +1)]
    WEST = [(-1, -1), (0, -1), (+1, -1)]
    EAST = [(-1, +1), (0, +1), (+1, +1)]

    DIRECTIONS = [NORTH, SOUTH, WEST, EAST]  # the order is important!

    rounds = 0
    while True:
        rounds += 1
        # consider moving
        elfs_wanttomove = []
        elfs_wanttomove_to = defaultdict(list)
        for y, x in elfs:
            # If no other Elves are in one of those eight positions, the Elf does not do anything during this round.
            if all_empty(elfs, y, x, set(NORTH) | set(SOUTH) | set(EAST) | set(WEST)):
                continue
            elfs_wanttomove.append((y, x))
        # stop, if no elf wants to move
        if len(elfs_wanttomove) == 0: break
        # try moving
        for y, x in elfs_wanttomove:
            for direction in DIRECTIONS:
                if not all_empty(elfs, y, x, direction): continue
                to = (y+direction[1][0], x+direction[1][1])
                elfs_wanttomove_to[to].append((y, x))
                break
        # If two or more Elves propose moving to the same position, none of those Elves move.
        for to, elfswantomove_to in elfs_wanttomove_to.items():
            if len(elfswantomove_to) == 1:
                elfs.pop(elfswantomove_to[0])
                elfs[to] = False
        # change direction for next round
        DIRECTIONS = [*DIRECTIONS[1:], DIRECTIONS[0]]
        if rounds == 10:
            # calculate the size of the area
            ys, xs = [elf[0] for elf in elfs], [elf[1] for elf in elfs]
            ymin, ymax = min(ys), max(ys)
            xmin, xmax = min(xs), max(xs)
            res = abs(xmax-xmin+1)*abs(ymax-ymin+1) - len(elfs)
            print("")
            print("Solution 1 ...:", res)
    print("")
    print("Solution 2 ...:", rounds)

def main(test):

    print("")
    print("****", "TEST" if test else "INPUT", "****************")
    # READ INPUT FILE
    script_path = os.path.dirname(os.path.realpath(__file__))
    filename = "test.txt" if test else "input.txt"
    with open(os.path.join(script_path, filename), encoding="utf-8") as input:
        lines = input.read().rstrip().split("\n")

    elfs = {}
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == "#": elfs[(y, x)] = 1

    # PART 1 and PART 2
    start = time()
    solve(elfs)
    print(f"{time() - start:5f} seconds")


main(test=True)  # 110, 20
main(test=False)  # 4302, 1025
