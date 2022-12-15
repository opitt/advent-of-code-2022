# https://adventofcode.com/2022/day/15
from rich import print
import os
from time import time
import re


def solve(lines, testline):
    coverage = []
    beacons = set()
    for line in lines:
        # Sensor at x=2, y=18: closest beacon is at x=-2, y=15
        sx, sy, bx, by = list(map(int, re.findall("[-]?\d+", line)))
        s_range = abs(sx-bx)+abs(sy-by)
        if sy-s_range <= testline <= sy+s_range:
            # the sensor covers the interesting row
            # get the min x and the max x, which depends on the y of the sensor and the sensor range
            s_coverage_testline = (sx-(s_range-(abs(testline-sy))),
                                   sx+(s_range-(abs(testline-sy))))
            coverage.append(s_coverage_testline)
            if by == testline: # there might be a beacon in the row already (test case)
                beacons.add(bx)
        pass
    #coverage.sort()
    max_x = max(coverage, key=lambda x: x[1])[1]
    min_x = min(coverage, key=lambda x: x[0])[0]
    print("Solution 1 is", max_x - min_x + 1 - len(beacons))


def main(test):

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


main(test=True)  # 26, 4725496
main(test=False)  #
