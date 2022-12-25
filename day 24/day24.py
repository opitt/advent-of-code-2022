# https://adventofcode.com/2022/day/24
from collections import defaultdict
from copy import deepcopy
import os
from time import time, sleep
from rich import print
from rich.table import Table
from rich.live import Live


def solve(blizz_left, blizz_right, blizz_up, blizz_down, startx, targx):

    def join_map(blizz_left, blizz_right, blizz_up, blizz_down):
        blizzmap = []
        for y in range(len(blizz_left)):
            blizzmap.append([])
            for x in range(len(blizz_left[0])):
                l, r, u, d = blizz_left[y][x], blizz_right[y][x], blizz_up[y][x], blizz_down[y][x]
                v = u
                v = v if d == "." else d
                v = v if l == "." else l
                v = v if r == "." else r
                blizzmap[y].append(v)
        return blizzmap

    def print_blizz(blizzmap):
        print("")
        for line in blizzmap:
            l = "".join(line)
            l = l.replace(">", "[red]>[/red]").replace("^", "[blue]^[/blue]").replace(
                "v", "[green]<[/green]").replace("v", "[yellow]v[/yellow]")
            print(l)

    def nextround(blizz_left, blizz_right, blizz_up, blizz_down):
        blizz_down = [blizz_down[-1], *blizz_down[:-1]]
        blizz_up = [*blizz_up[1:], blizz_up[0]]
        blizz_left = [[*line[1:], line[0]] for line in blizz_left]
        blizz_right = [[line[-1], *line[:-1]] for line in blizz_right]
        return blizz_left, blizz_right, blizz_up, blizz_down

    def generate_table(blizzmap) -> Table:
        table = Table()
        table.add_column("Blizzard", justify="center")
        for line in blizzmap:
            l = "".join(line)
            l = l.replace(">", "[red]>[/red]").replace("^", "[blue]^[/blue]").replace(
                "v", "[green]<[/green]").replace("v", "[yellow]v[/yellow]")
            table.add_row(f"{l}")
        return table

    blizzmap = join_map(blizz_left, blizz_right, blizz_up, blizz_down)

    with Live(generate_table(blizzmap), refresh_per_second=4) as live:
        for _ in range(1000000):
            sleep(0.2)
            # print_blizz(blizzmap)
            blizz_left, blizz_right, blizz_up, blizz_down = nextround(
                blizz_left, blizz_right, blizz_up, blizz_down)
            blizzmap = join_map(blizz_left, blizz_right, blizz_up, blizz_down)
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
    blizz_left = []
    blizz_right = []
    blizz_up = []
    blizz_down = []

    for line in lines[1:-1]:
        blizz_left.append([])
        blizz_right.append([])
        blizz_up.append([])
        blizz_down.append([])
        y = -1
        for b in line[1:-1]:
            o = "."
            if b == "<":
                blizz_left[y].append(b)
                blizz_right[y].append(o)
                blizz_up[y].append(o)
                blizz_down[y].append(o)
            elif b == ">":
                blizz_left[y].append(o)
                blizz_right[y].append(b)
                blizz_up[y].append(o)
                blizz_down[y].append(o)
            elif b == "^":
                blizz_left[y].append(o)
                blizz_right[y].append(o)
                blizz_up[y].append(b)
                blizz_down[y].append(o)
            elif b == "v":
                blizz_left[y].append(o)
                blizz_right[y].append(o)
                blizz_up[y].append(o)
                blizz_down[y].append(b)
            else:
                blizz_left[y].append(b)
                blizz_right[y].append(b)
                blizz_up[y].append(b)
                blizz_down[y].append(b)

    startx = lines[0].index(".")
    targx = lines[-1].index(".")

    # PART 1 and PART 2
    start = time()
    solve(blizz_left, blizz_right, blizz_up, blizz_down, startx, targx)
    print(f"{time() - start:5f} seconds")


# main(test=True)  #
main(test=False)  #
