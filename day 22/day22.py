# https://adventofcode.com/2022/day/22
from collections import defaultdict
from copy import deepcopy
import os
import re
from time import time
from rich import print


def solve(board, cmds):
    DIRS = "rdlu"
    dir = 0

    def turn(dir_idx, c):
        dir_idx = dir_idx - 1 if c == "L" else dir_idx + 1
        dir_idx = 3 if dir_idx < 0 else dir_idx % 4
        return dir_idx

    def step(idx, d, idxmax):
        idx = idx + d
        idx = idxmax if idx < 0 else idx % (idxmax + 1)
        return idx

    def wraparound(x, xnew, y, ynew):
        ...

    def move(y, x, d, steps):
        DIFFS = {0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1, 0)}
        yd, xd = DIFFS[d]
        ymax, xmax = len(board) - 1, len(board[0]) - 1
        for _ in range(steps):
            ynew, xnew = step(y, yd, ymax), step(x, xd, xmax)
            tile = board[ynew][xnew]
            if tile == ".":
                y, x = ynew, xnew
            elif tile == " ":
                # wrap around to the other side of the board
                ynew, xnew = wraparound(x, xnew, y, ynew)
                if board[ynew][xnew] == "#":
                    # If you run into a wall, you stop moving forward
                    break
                if board[ynew][xnew] == " ":
                    raise ValueError
                y, x = ynew, xnew
            else:
                # If you run into a wall, you stop moving forward
                break
        return y, x

    x = board[0].index(".")  #    ......#.
    y = 0
    for cmd in re.findall("\d+[A-Z]+", cmds):  # 10R5L5R10L4R5L5
        c_steps = int(cmd[:-1])
        c_turn = cmd[-1]
        y, x = move(y, x, dir, c_steps)
        dir = turn(dir, c_turn)

    res = (y + 1) * 1000 + (x + 1) * 4
    print("")
    print("Solution 1 ...:", m["root"])


def solve2():
    print("")
    print(
        "Solution 2 ...:",
        0,
        sep="\n",
    )


def main(test):

    print("")
    print("****", "TEST" if test else "INPUT", "****************")
    # READ INPUT FILE
    script_path = os.path.dirname(os.path.realpath(__file__))
    filename = "test.txt" if test else "input.txt"
    with open(os.path.join(script_path, filename), encoding="utf-8") as input:
        lines = input.read().rstrip().split("\n\n")

    board = lines[0].split("\n")
    width = max(len(line) for line in board)
    board = [line.ljust(width, " ") for line in board]
    cmds = lines[1]

    # PART 1
    start = time()
    solve(deepcopy(board), cmds)
    print(f"{time() - start:5f} seconds")

    # PART 2


main(test=True)  #
# main(test=False)  #
