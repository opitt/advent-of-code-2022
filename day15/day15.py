# https://adventofcode.com/2022/day/15
from collections import defaultdict
from rich import print
import os
from time import time
import re


def solve(lines, y):
    coverage = defaultdict(list)
    beacons = set()
    for line in lines:
        # example line: "Sensor at x=2, y=18: closest beacon is at x=-2, y=15"
        sx, sy, bx, by = list(map(int, re.findall("[-]?\d+", line)))
        # calc the sensor range, i.e. manhatten length between beacon and sensor
        s_range = abs(sx-bx)+abs(sy-by)
        if sy-s_range <= y <= sy+s_range:
            # the sensor covers the interesting row
            # get the min x and the max x, which depends on the y of the sensor and the sensor range
            xleft = sx-(s_range-(abs(y-sy)))
            xright = sx+(s_range-(abs(y-sy)))
            coverage[y].append((xleft, xright))
            if by == y:
                # there might be a beacon in the row already (test case)
                beacons.add(bx)

    max_x = max(coverage[y], key=lambda x: x[1])[1]
    min_x = min(coverage[y], key=lambda x: x[0])[0]
    # +1 to count inclusive e.g. 5-10 has 6 elements 5,6,7,8,9,10
    print("Solution 1 is", max_x - min_x + 1 - len(beacons))


def solve2(lines, max_coord):
    coverage = defaultdict(list)
    for line in lines:
        # Sensor at x=2, y=18: closest beacon is at x=-2, y=15
        sx, sy, bx, by = list(map(int, re.findall("[-]?\d+", line)))
        s_range = abs(sx-bx)+abs(sy-by)
        for y in range(sy-s_range, sy+s_range+1):
            xleft = sx-(s_range-(abs(y-sy)))
            xright = sx+(s_range-(abs(y-sy)))
            coverage[y].append((xleft, xright))

    for y, y_intervalls in coverage.items():
        if y < 0 or y > max_coord:
            continue
        y_intervalls.sort()
        left, right = y_intervalls[0]
        for intervall in y_intervalls[1:]:
            intleft, intright = intervall
            if left <= (intleft+1) and intleft <= (right+1):
                right = max(right, intright)
            else:
                print("Solution 2 is ....")
                res = (right+1)*4000000+y
                print(
                    y, f"({left},{right}), ({intleft},{intright}) = {res}")
                return res


def main(test):
    print("")
    print("****", "TEST" if test else "INPUT", "****************")
    # READ INPUT FILE
    script_path = os.path.dirname(os.path.realpath(__file__))
    with open(
        os.path.join(script_path, "test.txt" if test else "input.txt"), encoding="utf-8"
    ) as input:
        lines = input.read().rstrip().split("\n")

    # PART 1
    testline = 10 if test else 2000000
    start = time()
    solve(lines, testline)
    print(time() - start, " seconds")

    # PART 2
    start = time()
    if test:
        solve2(lines, 20)
    else:
        solve2(lines, 4000000)
    print(time() - start, " seconds")


main(test=True)  # 26, 56000011
main(test=False)  # 4725496, 12051287042458
