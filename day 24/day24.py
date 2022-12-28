# https://adventofcode.com/2022/day/24
from collections import deque
from copy import deepcopy
import os
from time import time
from rich import print

from rich.console import Console
console = Console()


class Blizzard():

    def __init__(self, lines, store_history=False, print_after_nextmap=False):
        self.wall = []
        self.left = []
        self.right = []
        self.up = []
        self.down = []
        self.blizzmap = []
        self.EMPTY = "."
        self.store_history = store_history
        self.print_after_nextmap = print_after_nextmap
        #
        self.minutes = 0
        self.visiting = deque()
        self.blizzmap_history = []
        self.__parse_blizzards(lines)
        self.__merge()

    def __parse_blizzards(self, lines):
        # reads the initial map;
        # finds and stores the entrance / exit of the map as well as the max width and height (x,y)
        # snowflakes: ^<>v
        # walls: #
        # empty fields: .
        self.wall = []
        self.left = []
        self.right = []
        self.up = []
        self.down = []
        for line in lines:
            self.wall.append([])
            self.left.append([])
            self.right.append([])
            self.up.append([])
            self.down.append([])
            y = -1  # the last line added
            for b in line:
                if b == "<":
                    self.wall[y].append(self.EMPTY)
                    self.left[y].append(b)
                    self.right[y].append(self.EMPTY)
                    self.up[y].append(self.EMPTY)
                    self.down[y].append(self.EMPTY)
                elif b == ">":
                    self.wall[y].append(self.EMPTY)
                    self.left[y].append(self.EMPTY)
                    self.right[y].append(b)
                    self.up[y].append(self.EMPTY)
                    self.down[y].append(self.EMPTY)
                elif b == "^":
                    self.wall[y].append(self.EMPTY)
                    self.left[y].append(self.EMPTY)
                    self.right[y].append(self.EMPTY)
                    self.up[y].append(b)
                    self.down[y].append(self.EMPTY)
                elif b == "v":
                    self.wall[y].append(self.EMPTY)
                    self.left[y].append(self.EMPTY)
                    self.right[y].append(self.EMPTY)
                    self.up[y].append(self.EMPTY)
                    self.down[y].append(b)
                elif b == "#":
                    self.wall[y].append(b)
                    self.left[y].append(self.EMPTY)
                    self.right[y].append(self.EMPTY)
                    self.up[y].append(self.EMPTY)
                    self.down[y].append(self.EMPTY)
                else:
                    self.left[y].append(b)
                    self.right[y].append(b)
                    self.up[y].append(b)
                    self.down[y].append(b)
                    self.wall[y].append(b)
        #
        self.maxx = len(self.wall[0])-1
        self.maxy = len(self.wall)-1
        self.IN = (0, self.wall[0].index("."))
        self.OUT = (self.maxy, self.wall[-1].index("."))

    def __merge(self):
        # merge the snowflakes into one blizzard map
        # if more than one thing is on a position, the number of things is shown
        #
        # the merge allows to save prev maps in a history
        if self.store_history and len(self.blizzmap):
            self.blizzmap_history.append(
                "\n".join("".join(line) for line in self.blizzmap))
        #
        self.blizzmap = []
        for y in range(len(self.wall)):
            self.blizzmap.append([])
            for x in range(len(self.wall[0])):
                w, l, r, u, d = self.wall[y][x], self.left[y][x], self.right[y][x], self.up[y][x], self.down[y][x]
                samefield = set([w, l, r, u, d]) - set(self.EMPTY)
                if len(samefield) == 0:
                    v = self.EMPTY
                elif len(samefield) == 1:
                    v = list(samefield)[0]
                else:
                    v = str(len(samefield))
                self.blizzmap[y].append(v)

    def __move(self):
        # move the snowflakes 1 step in their direction (wrap around) - inside the walls
        self.down = [self.down[0], self.down[-2],
                     *self.down[1:-2], self.down[-1]]
        self.up = [self.up[0], *self.up[2:-1], self.up[1], self.up[-1]]
        self.left = [[line[0], *line[2:-1], line[1], line[-1]]
                     for line in self.left]
        self.right = [[line[0], line[-2], *line[1:-2], line[-1]]
                      for line in self.right]

    def print(self):
        if self.print_after_nextmap:
            print(f"*** Minute {self.minutes}")
            if len(self.visiting):
                temp = deepcopy(self.blizzmap)
                for y, x in self.visiting:
                    temp[y][x] = "E"
                print("\n".join("".join(line) for line in temp))
            else:
                print("\n".join("".join(line) for line in self.blizzmap))
            print(f"")

    def __map_nextmin(self):
        self.minutes += 1
        self.__move()
        self.__merge()

    def __isempty(self, pos):
        y, x = pos
        return self.blizzmap[y][x] == self.EMPTY

    def __reachable_fields(self, pos):
        y, x = pos
        fields = [(max(0, y-1), x), (min(self.maxy, y+1), x),  # y+/- down/up
                  (y, max(0, x-1)), (y, min(self.maxx, x+1)),  # x+/- right/left
                  (y, x)]  # wait
        return set(fields)

    def findway(self, first, last):
        self.visiting.clear()
        self.visiting.append(first)
        self.print()
        while last not in self.visiting:
            # next round
            self.__map_nextmin()
            # try to move the elfs
            elfs = len(self.visiting)
            for _ in range(elfs):
                # check all elfs currently visiting fields
                #   if they can move during this new minutet. If they can't move anymore, they die ... :(
                pos = self.visiting.popleft()
                fields = self.__reachable_fields(pos)
                visit_nextmin = [(y, x) for y, x in fields if self.__isempty(
                    (y, x)) and (y, x) not in self.visiting]
                self.visiting.extend(visit_nextmin)
            self.print()


def main(test):
    # console.log(console.color_system)
    console.print("\n****", "TEST" if test else "INPUT",
                  "****************", style="bold black on #F0F0F0")
    # READ INPUT FILE
    script_path = os.path.dirname(os.path.realpath(__file__))
    filename = "test.txt" if test else "input.txt"
    with open(os.path.join(script_path, filename), encoding="utf-8") as input:
        lines = input.read().rstrip().split("\n")

    blizz = Blizzard(lines, store_history=True, print_after_nextmap=True)
    # is the last line of the maze, but actually it is the next line (border)

    # PART 1
    console.rule("PART 1")
    start = time()

    print(f"Solve START->DEST ... {blizz.IN} -> {blizz.OUT}")
    blizz.findway(blizz.IN, blizz.OUT)
    console.print(
        f"Solution 1 ...: {blizz.minutes} minutes", style="green on #F0F0F0")

    # PART 2
    console.rule("PART 2")
    print(
        f"Solve DEST->START ... {blizz.OUT} -> {blizz.IN}")
    blizz.findway(blizz.OUT, blizz.IN)
    print(f"Solve START->DEST ... {blizz.IN} -> {blizz.OUT}")
    blizz.findway(blizz.IN, blizz.OUT)
    console.print(
        f"Solution 2 ...: {blizz.minutes} minutes", style="green on #F0F0F0")

    console.rule(f"Elapsed time {time() - start:5f} seconds")


main(test=True)  # 18, 54
main(test=False)  # 311, 869
