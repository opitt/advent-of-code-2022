# https://adventofcode.com/2022/day/9
import math
import os
from rich import print


def solve1(cmds):
    Y, X = 0, 1

    def move_head(cmd, h):
        D = {"R": (0, 1), "L": (0, -1), "D": (1, 0), "U": (-1, 0)}
        h[Y] += D[cmd][Y]
        h[X] += D[cmd][X]

    def follow_knot(h, t):
        dist = math.dist(h, t)
        if dist > 1:
            DX = -1 if h[X] < t[X] else 1
            DY = -1 if h[Y] < t[Y] else 1
            if t[Y] == h[Y]:  # same row (head and tail have same y)
                t[X] += DX
            elif t[X] == h[X]:  # same column (head and tail have same x)
                t[Y] += DY
            elif dist > 1.5:  # need to catch up with the head
                t[Y] += DY
                t[X] += DX

    def solution(cmds, knots):
        tail_trail = {tuple(knots[-1])}
        for cmd in cmds:
            c,n = cmd
            for _ in range(n):
                move_head(c, knots[0])
                for k1, k2 in zip(knots[:-1], knots[1:]):
                    follow_knot(k1, k2)
                tail_trail.add(tuple(knots[-1]))
        res = len(tail_trail)
        return res

    # PART 1
    knots = [
        [0, 0],
        [0, 0],
    ]  # [h[y, x], ... t[]]
    res = solution(cmds, knots) 
    print(f"Solution 1 ... {res}")

    # PART 2
    knots = [
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
        [0, 0],
    ]  # [h[y, x], ... t[]]
    res = solution(cmds, knots) 
    print(f"Solution 2 ... {res}")


def main(test):

    print("****", "TEST" if test else "INPUT", "****************")
    # READ INPUT FILE
    script_path = os.path.dirname(os.path.realpath(__file__))
    with open(
        os.path.join(script_path, "test.txt" if test else "input.txt"), encoding="utf-8"
    ) as input:
        lines = input.read().rstrip().split("\n")

    lines = [(line.split()[0], int(line.split()[1])) for line in lines]

    # PART 1 and 2
    solve1(lines)


main(test=True)    # 13, 1
main(test=False)  # 6044, 2384
