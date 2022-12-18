import os
import itertools as it
from time import time
from rich import print

class Tetris():
    # tile patterns, with hight and width
    TILES = [(["####"], 1, 4),
         ([" # ", "###", " # "], 3, 3),
         (["  #", "  #", "###"], 3, 3),
         (["#", "#", "#", "#"], 4, 1),
         (["##", "##"], 2, 2)]
    TILE_START_INDEX = 2  # 2 empty positions from left
    AIR_ROW = "       "

    def __init__(self, streams, rounds):
        self.chamber = []
        self.tile_pos = None
        self.tile_row = None
        self.streams = streams
        self.rounds = rounds


    def solve1(self):
        self.chamber = []
        tiles = it.cycle(self.TILES)
        jets = it.cycle(list(self.streams))
        for r in range(self.rounds):
            tile = next(tiles)
            self.start_falling(tile)
            self.push_tile(next(jets), tile)
            still_falling = True
            while still_falling:
                still_falling = self.falling(tile)
                if still_falling:
                    self.push_tile(next(jets), tile)

        self.chamber = list(it.dropwhile(lambda r: r == self.AIR_ROW, self.chamber))
        print("Solution 1 ... ", len(self.chamber))


    def start_falling(self, tile):
        self.chamber = list(it.dropwhile(lambda r: r == self.AIR_ROW, self.chamber))
        # add air rows to cover the current tile starting to fall
        for _ in range(3+tile[1]):
            self.chamber.insert(0,self.AIR_ROW)
        self.tile_pos = self.TILE_START_INDEX
        self.tile_row = tile[1]-1  # the row, that the lowest tile part covers


    def push_tile(self, direction, tile):
        if direction == ">":
            if self.tile_pos+1+tile[2] <= 7 and self.fits_in_row(tile, self.tile_row, self.tile_pos+1):
                self.tile_pos += 1
        elif direction == "<":
            if self.tile_pos-1 >= 0 and self.fits_in_row(tile, self.tile_row, self.tile_pos-1):
                self.tile_pos -= 1


    def fits_in_row(self, tile, to_row, to_pos):
        # .@.....
        # @@@....
        # .@#....
        # ..#....
        # ..#....
        # ..#...
        # -------
        fits = True
        for t, part in enumerate(tile[0][::-1]):
            p = " "*to_pos + part + " "*(7-to_pos-len(part))
            fits = fits and all(map(
                lambda z: z[0] == " " or z[1] == " " or z[1] == " " and z[0] == "#", zip(p, self.chamber[to_row-t])))
        return fits


    def falling(self, tile):
        fits = self.fits_in_row(tile, self.tile_row, self.tile_pos)
        if fits and (self.tile_row+1) < len(self.chamber) and self.fits_in_row(tile, self.tile_row+1, self.tile_pos):
            # fits here, and can fall to next row ... continue falling
            self.tile_row += 1
            return True
        self.landing(tile)
        return False  # not falling anymore


    def landing(self, tile):
        for part in tile[0][::-1]:
            p = " "*self.tile_pos + part + " "*(7-self.tile_pos-len(part))
            if self.tile_row >= 0:
                self.chamber[self.tile_row] = "".join(
                    [p[i] if b == " " else b for i, b in enumerate(self.chamber[self.tile_row])])
                self.tile_row -= 1
            else:
                self.chamber.insert(0,p)


def main(test):

    print("****", "TEST" if test else "INPUT", "****************")
    # READ INPUT FILE
    script_path = os.path.dirname(os.path.realpath(__file__))
    with open(
        os.path.join(script_path, "test.txt" if test else "input.txt"), encoding="utf-8"
    ) as input:
        lines = input.read().rstrip().split("\n")

    # PART 1
    start = time()
    game = Tetris(lines[0], 2022)
    game.solve1()
    print(time() - start, " seconds")


main(test=True)  # 3068, inf
main(test=False)  # 3184, inf
