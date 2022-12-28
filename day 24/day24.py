# https://adventofcode.com/2022/day/24
from collections import deque
from copy import deepcopy
import os
from time import time, sleep
from rich import print
from rich.table import Table
from rich.live import Live
import re


class Blizzard():

    def __init__(self, lines, history=False):
        self.left = []
        self.right = []
        self.up = []
        self.down = []
        self.blizzmap = []
        self.EMPTY = "."
        self.minutes = 0
        #
        self.history = history
        self.blizzmap_history = []
        #self.maxx = 0
        #self.maxy = 0
        self.__parse_blizzards(lines)
        self.__merge()

    def __parse_blizzards(self, lines):
        self.left = []
        self.right = []
        self.up = []
        self.down = []
        for line in lines[1:-1]:
            self.left.append([])
            self.right.append([])
            self.up.append([])
            self.down.append([])
            y = -1  # the last line added
            o = self.EMPTY
            for b in line[1:-1]:
                if b == "<":
                    self.left[y].append(b)
                    self.right[y].append(o)
                    self.up[y].append(o)
                    self.down[y].append(o)
                elif b == ">":
                    self.left[y].append(o)
                    self.right[y].append(b)
                    self.up[y].append(o)
                    self.down[y].append(o)
                elif b == "^":
                    self.left[y].append(o)
                    self.right[y].append(o)
                    self.up[y].append(b)
                    self.down[y].append(o)
                elif b == "v":
                    self.left[y].append(o)
                    self.right[y].append(o)
                    self.up[y].append(o)
                    self.down[y].append(b)
                else:
                    self.left[y].append(b)
                    self.right[y].append(b)
                    self.up[y].append(b)
                    self.down[y].append(b)
        #
        self.maxx = len(self.left[0])-1
        self.maxy = len(self.left)-1
        self.s = (0, lines[0][1:-1].index("."))
        self.d = (len(lines)-3, lines[-1][1:-1].index("."))

    def __merge(self):
        if self.history and len(self.blizzmap):
            self.blizzmap_history.append(
                "\n".join("".join(line) for line in self.blizzmap))
        self.blizzmap = []
        for y in range(len(self.left)):
            self.blizzmap.append([])
            for x in range(len(self.left[0])):
                l, r, u, d = self.left[y][x], self.right[y][x], self.up[y][x], self.down[y][x]
                samefield = set([l, r, u, d]) - set(self.EMPTY)
                if len(samefield) == 0:
                    v = self.EMPTY
                elif len(samefield) == 1:
                    v = list(samefield)[0]
                else:
                    v = str(len(samefield))
                # overlay the blizzard, just for visuality
                #v = u
                #v = v if d == self.EMPTY else d
                #v = v if l == self.EMPTY else l
                #v = v if r == self.EMPTY else r

                self.blizzmap[y].append(v)

    def __move(self):
        self.down = [self.down[-1], *self.down[:-1]]
        self.up = [*self.up[1:], self.up[0]]
        self.left = [[*line[1:], line[0]] for line in self.left]
        self.right = [[line[-1], *line[:-1]] for line in self.right]

    def print(self, visiting=[]):
        print(f"*** Minute {self.minutes}")
        if len(visiting
               ):
            temp = deepcopy(self.blizzmap)
            for y, x in visiting:
                temp[y][x] = "E"
            print("\n".join("".join(line) for line in temp))
        else:
            print("\n".join("".join(line) for line in self.blizzmap))
        print(f"")

    def map_nextmin(self):
        self.minutes += 1
        self.__move()
        self.__merge()

    def isempty(self, y, x):
        return self.blizzmap[y][x] == self.EMPTY

    def reachable_fields(self, y, x):
        fields = [(max(0, y-1), x), (min(self.maxy, y+1), x),  # y+/- down/up
                  (y, max(0, x-1)), (y, min(self.maxx, x+1)),  # x+/- right/left
                  (y, x)]  # wait
        return set(fields)


def solve(blizz, first, last):

    def visualise(blizz, visiting) -> Table:
        table = Table()
        table.add_column(
            f"Map after {blizz.minutes} minutes", justify="center")
        bm = deepcopy(blizz.blizzmap)
        for y, x in visiting:
            bm[y][x] = "@"
        for line in bm:
            l = "".join(line)
            l = l.replace(
                "@", "[bright_white on red]@[/bright_white on red]")
            l = l.replace(
                ".", "[white on white].[/white on white]")
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

    visiting = deque()
    # no field visiting yet. Elf is sitting on the edge, waiting that they can can step to the FIRST field on map
    while True:
        blizz.map_nextmin()
        blizz.print(visiting)
        if blizz.isempty(*first):  # can elf visit the first in that minute
            # step into the field
            visiting.append(first)
            break

    while visiting and last not in visiting:
        # next round
        blizz.map_nextmin()
        # try to move the elfs
        elfs = len(visiting)
        for _ in range(elfs):
            # check all elfs currently visiting fields
            #   if they can move during this new minutet. If they can't move anymore, they die ... :(
            fields = blizz.reachable_fields(*visiting.popleft())
            visit_nextmin = [(y, x) for y, x in fields if blizz.isempty(
                y, x) and (y, x) not in visiting]
            visiting.extend(visit_nextmin)
        blizz.print(visiting)
    # the next minute is used to step to the target
    if last in visiting:
        # the elf steps in the next minute to the desition field
        blizz.map_nextmin()
    else:
        raise ValueError(f"Did not reach the destination {last}")

# Minute 17
# 2.v.<>
# <.<..<
# .^>^22
# .2..2E


def main(test):

    print("")
    print("****", "TEST" if test else "INPUT", "****************")
    # READ INPUT FILE
    script_path = os.path.dirname(os.path.realpath(__file__))
    filename = "test.txt" if test else "input.txt"
    with open(os.path.join(script_path, filename), encoding="utf-8") as input:
        lines = input.read().rstrip().split("\n")

    blizz = Blizzard(lines, history=True)
    # is the last line of the maze, but actually it is the next line (border)

    # PART 1
    start = time()

    blizz.print()
    solve(blizz, blizz.s, blizz.d)
    print("Solution 1 to START->DEST:", blizz.minutes)
    blizz.print()

    # PART 2
    print("Solve start->DEST->START ...", blizz.minutes)
    solve(blizz, blizz.d, blizz.s)
    print("Solution 2-1:")
    blizz.print()
    print("Solve start->dest->START->DEST ...", blizz.minutes)
    solve(blizz, blizz.s, blizz.d)
    blizz.print()
    print("Solution 2-2::")

    print(f"{time() - start:5f} seconds")


main(test=True)  #
# main(test=False)  #
