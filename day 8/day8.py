# https://adventofcode.com/2022/day/8
from itertools import takewhile
import os
from rich import print
from copy import deepcopy


def solve1(trees):

    def is_visible(trees, heigth):
        return max(trees) < heigth

    tree_cols = [list(t) for t in zip(*trees)]
    forrest_h, forrest_w = len(tree_cols), len(trees)
    res = 2 * (forrest_h - 1) + 2 * (forrest_w - 1)

    for x in range(1, forrest_w - 1):
        for y in range(1, forrest_h - 1):
            h = trees[y][x]
            if (
                is_visible(tree_cols[x][:y], h)
                or is_visible(tree_cols[x][y + 1 :], h)
                or is_visible(trees[y][:x], h)
                or is_visible(trees[y][x + 1 :], h)
            ):
                res += 1

    print(f"Solution 1 ... {res}")
    return res


def solve2(trees):

    def viewing_distance(trees, heigth):
        # function will not receive the edge trees (distance = 0)
        dist = 0
        for h in trees:
            dist += 1
            if h >= heigth:
                break
        return dist

    tree_cols = [list(t) for t in zip(*trees)]
    forrest_h, forrest_w = len(tree_cols), len(trees)
    res = 0

    for x in range(1, forrest_w - 1):
        for y in range(1, forrest_h - 1):
            h = trees[y][x]
            dist = 1
            dist *= viewing_distance(trees[y][:x][::-1], h)  # look left
            dist *= viewing_distance(trees[y][x + 1 :], h)  # look right
            dist *= viewing_distance(tree_cols[x][:y][::-1], h)  # look down
            dist *= viewing_distance(tree_cols[x][y + 1 :], h)  # look up
            res = max(res, dist)

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

    lines = [list(map(int, line)) for line in lines]

    # PART 1
    solve1(lines)

    # PART 2
    solve2(lines)


main(test=True)  # 21, 8
main(test=False)  # 1695, 287040
