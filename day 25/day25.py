# https://adventofcode.com/2022/day/25
import os
from time import time
from rich import print

def solve(fuel):
    fuel_dec = [snafu2dec(snafu) for snafu in fuel]
    fuel_needed = sum(fuel_dec)
    print(f"Fuel needed: {fuel_needed}")
    print(f"Solution 1 ... : {base52snafu(dec2base5(fuel_needed))}")
    #
    print(
        f"[green on black]Looking forward to a happy new AoC {base52snafu(dec2base5(2023))}[green on black]")


def snafu2dec(s):
    # s snafu string
    N = {"-": -1, "=": -2, "0": 0, "1": 1, "2": 2}
    d = sum([N[c]*(5**pof) for pof, c in enumerate(s[::-1])])
    return d


def dec2base5(d):
    # d integer
    res = []
    while d:
        d, n = divmod(d, 5)
        res.append(str(n))
    return "".join(res[::-1])


def base52snafu(s):
    # s = base5 number as string
    N = {"-2": "=", "-1": "-"}
    res = []
    mem = 0
    for n in map(int, s[::-1]):
        n += mem
        if n in [0, 1, 2]:
            mem = 0
        else:
            n = n-5
            mem = 1
        res.append(n)
    if mem:
        res.append(mem)
    return "".join(map(lambda n: N.get(n, n), map(str, res[::-1])))


def main(test):

    print("")
    print("****", "TEST" if test else "INPUT", "****************")
    # READ INPUT FILE
    script_path = os.path.dirname(os.path.realpath(__file__))
    filename = "test.txt" if test else "input.txt"
    with open(os.path.join(script_path, filename), encoding="utf-8") as input:
        lines = input.read().rstrip().split("\n")

    # PART 1
    start = time()
    solve(lines)
    print(f"{time() - start:5f} seconds")


main(test=True)  # 2=-1=0
main(test=False)  # 20-1-0=-2=-2220=0011
