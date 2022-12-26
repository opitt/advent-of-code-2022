# https://adventofcode.com/2022/day/24
from collections import defaultdict, deque
from copy import deepcopy
import os
from time import time, sleep
from rich import print
from rich.table import Table
from rich.live import Live


def solve(left, right, up, down, startx, destx):

    def mergeblizz(left, right, up, down):
        blizz = []
        for y in range(len(left)):
            blizz.append([])
            for x in range(len(left[0])):
                l, r, u, d = left[y][x], right[y][x], up[y][x], down[y][x]
                # overlay the blizzard, just for visuality
                v = u
                v = v if d == "." else d
                v = v if l == "." else l
                v = v if r == "." else r
                blizz[y].append(v)
        return blizz

    def moveblizz(left, right, up, down):
        down = [down[-1], *down[:-1]]
        up = [*up[1:], up[0]]
        left = [[*line[1:], line[0]] for line in left]
        right = [[line[-1], *line[:-1]] for line in right]
        return left, right, up, down

    def generate_table(blizzmap) -> Table:
        table = Table()
        table.add_column("Blizzard", justify="center")
        for line in blizzmap:
            l = "".join(line)
            l = l.replace(
                ".", "[bright_white on white].[/bright_white on white]")
            l = l.replace(
                ">", "[bright_white on deep_sky_blue2]>[/bright_white on deep_sky_blue2]")
            l = l.replace(
                "^", "[bright_white on bright_green]^[/bright_white on bright_green]")
            l = l.replace(
                "<", "[bright_white on deep_sky_blue2]<[/bright_white on deep_sky_blue2]")
            l = l.replace(
                "v", "[bright_white on bright_green]v[/bright_white on bright_green]")
            table.add_row(f"{l}")
        return table

    # merge the blizzards to the initial map
    blizzmap = mergeblizz(left, right, up, down)
    maxy = len(blizzmap)-1
    maxx = len(blizzmap[0])-1
    minutes = 0

    # wait until elf can move into the map from the start pos (border)
    while True:
        minutes += 1
        print(minutes)
        left, right, up, down = moveblizz(left, right, up, down)
        blizzmap = mergeblizz(left, right, up, down)
        if blizzmap[0][startx] == ".":
            break

    q = deque()
    q.append((0, startx))
    while q:
        for _ in range(len(q)):
            # check all elfs, where they can move. If they can't move anymore, they die ... :(
            elfy, elfx = q.popleft()
            moves = set([(max(0, elfy-1), elfx), (min(maxy, elfy+1), elfx),  # y+/- down/up
                         (elfy, max(0, elfx-1)), (elfy,
                                                  min(maxx, elfx+1)),  # x+/- right/left
                         (elfy, elfx)])  # wait

            actions = [(y, x) for y, x in moves if blizzmap[y]
                       [x] == "." and (y, x) not in q]
            if (maxy, destx) in actions:
                q.clear()
                print("Destination reached after (mins): ", minutes+1)
                break
            else:
                q.extend(actions)
        minutes += 1
        print(minutes)
        left, right, up, down = moveblizz(left, right, up, down)
        blizzmap = mergeblizz(left, right, up, down)

    return
    with Live(generate_table(blizzmap), refresh_per_second=1) as live:
        for _ in range(100):
            sleep(1)
            # print_blizz(blizzmap)
            left, right, up, down = moveblizz(
                left, right, up, down)
            blizzmap = mergeblizz(left, right, up, down)
            live.update(generate_table(blizzmap))


def main(test):

    print("")
    print("****", "TEST" if test else "INPUT", "****************")
    # READ INPUT FILE
    script_path = os.path.dirname(os.path.realpath(__file__))
    filename = "test.txt" if test else "input.txt"
    with open(os.path.join(script_path, filename), encoding="utf-8") as input:
        lines = input.read().rstrip().split("\n")

    # DIR = {"<":(0, -1), ">":(0, +1), "v":(+1, 0), "^":(-1,0), "#":(0,0)}
    left = []
    right = []
    up = []
    down = []

    for line in lines[1:-1]:
        left.append([])
        right.append([])
        up.append([])
        down.append([])
        y = -1
        for b in line[1:-1]:
            o = "."
            if b == "<":
                left[y].append(b)
                right[y].append(o)
                up[y].append(o)
                down[y].append(o)
            elif b == ">":
                left[y].append(o)
                right[y].append(b)
                up[y].append(o)
                down[y].append(o)
            elif b == "^":
                left[y].append(o)
                right[y].append(o)
                up[y].append(b)
                down[y].append(o)
            elif b == "v":
                left[y].append(o)
                right[y].append(o)
                up[y].append(o)
                down[y].append(b)
            else:
                left[y].append(b)
                right[y].append(b)
                up[y].append(b)
                down[y].append(b)

    startx = lines[0][1:-1].index(".")
    destx = lines[-1][1:-1].index(".")

    # PART 1 and PART 2
    start = time()
    solve(left, right, up, down, startx, destx)
    print(f"{time() - start:5f} seconds")


#main(test=True)  #
main(test=False)  #
