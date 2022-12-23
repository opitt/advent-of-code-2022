# https://adventofcode.com/2022/day/22
from copy import deepcopy
from curses.ascii import isdigit
import os
import re
from time import time
from rich import print


def solve(board, cmds):

    def turn(facing, c):
        facing = facing - 1 if c == "L" else facing + 1
        facing = 3 if facing < 0 else facing % 4
        return facing

    def wraparound_x(y, x, xd):
        xnew = x
        while board[y][xnew] != " ":
            xnew += (-1*xd)
        return xnew+xd

    def wraparound_y(x, y, yd):
        ynew = y
        while board[ynew][x] != " ":
            ynew += (-1*yd)
        return ynew+yd

    def move(y, x, d, steps):
        DIFFS = {0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1, 0)}
        yd, xd = DIFFS[d]
        for _ in range(steps):
            ynew = y+yd
            xnew = x+xd
            tile = board[ynew][xnew]
            if tile == ".":
                y, x = ynew, xnew
            elif tile == " ":
                # try to wrap around to the other side of the board
                if yd:
                    ynew = wraparound_y(x, y, yd)
                if xd:
                    xnew = wraparound_x(y, x, xd)
                if board[ynew][xnew] == "#":
                    # If you run into a wall, you stop moving forward
                    break
                if board[ynew][xnew] == ".":
                    y, x = ynew, xnew
            else:
                # If you run into a wall, you stop moving forward
                break
        return y, x

    FACINGSYM = ">v<^"
    facing = 0
    y = 1
    x = board[y].index(".")  # ......#.
    boardpath = deepcopy(board)
    boardpath[y] = boardpath[y][:x] + FACINGSYM[facing] + boardpath[y][x+1:]
    for cmd in re.findall("\d+|[RL]", cmds):  # 10R5L5R10L4R5L5
        if cmd.isdigit():
            c_steps = int(cmd)
            for _ in range(c_steps):
                y, x = move(y, x, facing, 1)
                boardpath[y] = boardpath[y][:x] + \
                    FACINGSYM[facing] + boardpath[y][x+1:]
        else:
            c_turn = cmd
            facing = turn(facing, c_turn)
            boardpath[y] = boardpath[y][:x] + FACINGSYM[facing] + boardpath[y][x+1:]

    boardpath[y] = boardpath[y][:x] + f"[red]{facing}[/red]" + boardpath[y][x+1:]
    print(*boardpath, sep="\n")

    res = (y) * 1000 + (x) * 4 + facing
    print("")
    print("Solution 1 ...:", res)


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
    board = [f" {line.ljust(width, ' ')} " for line in board]
    board.append(" "*(width+2))
    board.insert(0, " "*(width+2))
    cmds = lines[1]

    # PART 1
    start = time()
    solve(deepcopy(board), cmds)
    print(f"{time() - start:5f} seconds")

    # PART 2


main(test=True)  # 6032,
main(test=False)  # 131052,
