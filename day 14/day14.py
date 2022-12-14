import os
from rich import print
import itertools as it

def solve1(cave):
    res=0
    sand = (0,500)
    filled = 0
    while True:

    print(f"Solution part 1 ... {res}")



def parse_scan(lines):
    # 503,4 -> 502,4 -> 502,9 -> 494,9
    cave = {}
    for line in lines:
        points = [eval(f"({point})") for point in line.split(" -> ")]
        for p1, p2 in it.pairwise(points):
            x1,y1 = p1
            x2,y2 = p2
            for y in range(min(y1, y2), max(y1, y2)+1):
                for x in range(min(x1, x2), max(x1, x2)+1):
                    row = cave.get(x, set())
                    row.add(y)
                    cave[x] = row
    return cave

def main(test):

    print("****", "TEST" if test else "INPUT", "****************")
    # READ INPUT FILE
    script_path = os.path.dirname(os.path.realpath(__file__))
    with open(
        os.path.join(script_path, "test.txt" if test else "input.txt"), encoding="utf-8"
    ) as input:
        lines = input.readlines()

    cave = parse_scan(lines)
    # PART 1
    solve1(cave)

    # PART 2


#main(test=True)  # 
main(test=False)  # 
