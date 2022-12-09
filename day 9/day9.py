# https://adventofcode.com/2022/day/9
import math
import os
from rich import print


def solve1(cmds):
    res = 0
    h = [0, 0]  # [y, x]
    t = [0, 0]  # [y, x]
    t_trail = {tuple(t)}

    def move1(cmd, h, t, trail):
        Y, X = 0, 1
        D = {"R": (0, 1), "L": (0, -1), "D": (1, 0), "U": (-1, 0)}
        DX = D[cmd][X]
        DY = D[cmd][Y]
        # move head
        h[Y] += DY
        h[X] += DX
        # calculate distance to tail
        dist = math.dist(t, h)

        if dist > 1:
            if t[Y] == h[Y]:  # same row (head and tail have same y)
                t[X] += DX
            elif t[X] == h[X]:  # same column (head and tail have same x)
                t[Y] += DY
            elif dist < 1.5:  # touching, diagonal
                pass
            else:
                t[Y] += -1 if h[Y] < t[Y] else 1
                t[X] += -1 if h[X] < t[X] else 1

        trail.add(tuple(t))

    for cmd in cmds:
        for _ in range(cmd[1]):
            move1(cmd[0], h, t, t_trail)

    res = len(t_trail)
    print(f"Solution 1 ... {res}")
    return res


def solve2(cmds):
    res = 0

    print(f"Solution 2 ... {res}")
    return res


def main(test):

    print("****", "TEST" if test else "INPUT", "****************")
    # READ INPUT FILE
    script_path = os.path.dirname(os.path.realpath(__file__))
    with open(
        os.path.join(script_path, "test.txt" if test else "input.txt"), encoding="utf-8"
    ) as input:
        lines = input.read().rstrip().split("\n")

    lines = [(line.split()[0], int(line.split()[1])) for line in lines]

    # PART 1
    solve1(lines)

    # PART 2
    solve2(lines)


# main(test=True)    #
main(test=False)  #
