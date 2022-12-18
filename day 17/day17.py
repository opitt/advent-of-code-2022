import os
import itertools as it
from time import time
from rich import print


def start_falling(tile):
    global tile_pos
    global tile_row
    global chamber

    chamber = list(it.dropwhile(lambda r: r == AIR_ROW, chamber))
    # add air rows to cover the current tile starting to fall
    for _ in range(3+tile[1]):
        chamber.insert(0,AIR_ROW)
    tile_pos = TILE_START_INDEX
    tile_row = tile[1]-1  # the row, that the lowest tile part covers


def push_tile(direction, tile):
    global tile_pos
    global tile_row

    if direction == ">":
        if tile_pos+1+tile[2] <= 7 and fits_in_row(tile, tile_row, tile_pos+1):
            tile_pos += 1
    elif direction == "<":
        if tile_pos-1 >= 0 and fits_in_row(tile, tile_row, tile_pos-1):
            tile_pos -= 1


def fits_in_row(tile, to_row, to_pos):
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
            lambda z: z[0] == " " or z[1] == " " or z[1] == " " and z[0] == "#", zip(p, chamber[to_row-t])))
    return fits


def falling(tile):
    global tile_row
    global tile_pos

    fits = fits_in_row(tile, tile_row, tile_pos)
    if fits and (tile_row+1) < len(chamber) and fits_in_row(tile, tile_row+1, tile_pos):
        # fits here, and can fall to next row ... continue falling
        tile_row += 1
        return True
    landing(tile)
    return False  # not falling anymore


def landing(tile):
    global tile_row
    global tile_pos
    global chamber

    for part in tile[0][::-1]:
        p = " "*tile_pos + part + " "*(7-tile_pos-len(part))
        if tile_row >= 0:
            chamber[tile_row] = "".join(
                [p[i] if b == " " else b for i, b in enumerate(chamber[tile_row])])
            tile_row -= 1
        else:
            chamber = [p, *chamber]


def solve1(streams, rounds):
    global chamber

    chamber = []
    tiles = it.cycle(TILES)
    jets = it.cycle(list(streams))
    for r in range(rounds):
        tile = next(tiles)
        start_falling(tile)
        push_tile(next(jets), tile)
        still_falling = True
        while still_falling:
            still_falling = falling(tile)
            if still_falling:
                push_tile(next(jets), tile)

    chamber = list(it.dropwhile(lambda r: r == AIR_ROW, chamber))
    print("Solution 1 ... ", len(chamber))

# tile patterns, with hight and width
TILES = [(["####"], 1, 4),
         ([" # ", "###", " # "], 3, 3),
         (["  #", "  #", "###"], 3, 3),
         (["#", "#", "#", "#"], 4, 1),
         (["##", "##"], 2, 2)]
TILE_START_INDEX = 2  # 2 empty positions from left
AIR_ROW = "       "


def main(test):
    global chamber

    print("****", "TEST" if test else "INPUT", "****************")
    # READ INPUT FILE
    script_path = os.path.dirname(os.path.realpath(__file__))
    with open(
        os.path.join(script_path, "test.txt" if test else "input.txt"), encoding="utf-8"
    ) as input:
        lines = input.read().rstrip().split("\n")

    # PART 1
    start = time()
    solve1(lines[0], 2022)
    print(time() - start, " seconds")

    # PART 2
    #start = time()
    #solve1(lines[0], 1000000000000)
    #print(time() - start, " seconds")


main(test=True)  # 3068, inf
main(test=False)  # 3184, inf
