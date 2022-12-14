import os
from rich import print
import itertools as it


def print_cave(cave):
    h = max([max(stoneys) for stoneys in cave.values()])+2
    for y in range(h):
        row = ""
        for x in range(min(cave), max(cave)+1):
            if y not in cave.get(x, []):
                row += "."
            else:
                row += "#"
        print(f"{y:>2}{row}")
    print("")


def solve1(cave):

    def drop(x, sandy):
        # check if sand can fall below current sand y pos
        groundy = min([y-1 for y in cave[x] if y > sandy], default=None)
        if groundy == None:
            return False  # could not find air in this column
        left, right = x-1, x+1
        # check, if lef and right columns are in the scan - if not we reached the infinity hole
        if cave.get(left, None) == None or cave.get(right, None) == None:
            return False
        # check, if the next diagonal y positions are already used
        nexty = groundy+1
        if nexty not in cave[left]:
            return drop(left, groundy)
        if nexty not in cave[right]:
            return drop(right, groundy)
        cave[x].append(groundy)  # land the sand
        return True

    res = 0
    while drop(500, -1):
        res += 1

    print(f"Solution ... {res}")


def parse_scan(lines):
    # 503,4 -> 502,4 -> 502,9 -> 494,9
    # store only stones in a dictionary ... key = x position; values = the stone positions y
    #          x    y    x            y
    # cave = {503: {4}, 502: {4, 5, 6, 7, 8, 9 }, ...}
    cave = dict()
    for line in lines:
        points = [eval(f"({point})") for point in line.split(" -> ")]
        for p1, p2 in it.pairwise(points):
            x1, y1 = p1
            x2, y2 = p2
            for y in range(min(y1, y2), max(y1, y2)+1):
                for x in range(min(x1, x2), max(x1, x2)+1):
                    stones = cave.get(x, [])
                    if y not in stones:
                        stones.append(y)
                    cave[x] = stones
    return cave


def parse_scan2(lines):
    cave = parse_scan(lines)
    # add the ground to the cave scan
    y = max([max(y)+2 for y in cave.values()])
    for x in range(500-y, 500+y + 1):
        cave[x] = [y] if x not in cave else cave[x]+[y]
    return cave


def main(test):

    print("****", "TEST" if test else "INPUT", "****************")
    # READ INPUT FILE
    script_path = os.path.dirname(os.path.realpath(__file__))
    filename = "test.txt" if test else "input.txt"
    with open(os.path.join(script_path, filename), encoding="utf-8") as input:
        lines = input.readlines()

    # PART 1
    cave = parse_scan(lines)
    print("### Part 1 - scan      ###")
    print_cave(cave)
    solve1(cave)
    print("### Part 1 - sand fill ###")
    print_cave(cave)

    # PART 2
    cave = parse_scan2(lines)
    #print("### Part 2 - scan      ###")
    #print_cave(cave)
    solve1(cave)
    #print("### Part 2 - sand fill ###")
    #print_cave(cave)


main(test=True)  # 24, 93
main(test=False)  # 644, 27324
