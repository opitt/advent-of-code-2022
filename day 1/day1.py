# https://adventofcode.com/2022/day/1
from itertools import groupby
import os

def solve1(cals_per_elf):
    return max(cals_per_elf)

def solve2(cals_per_elf):
    return sum(sorted(cals_per_elf,reverse=True)[:3])
    
def main():
    # READ INPUT FILE
    script_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(script_path, "input.txt"), encoding="utf-8") as input:
        lines = input.readlines()
    lines = list(map(str.strip, lines))
    
    cals_per_elf = [sum(map(int,list(cals))) for elf,cals in groupby(lines, key=lambda cal: cal!="") if elf]

    # PART 1
    result=solve1(cals_per_elf)
    print(
        f"The max amount of cals an elf has is {result}."
    )
    # 70509

    # PART 2
    result = solve2(cals_per_elf)
    print(
        f"Together the 3 elfs with max cals carry {result}."
    )
    # 208567

main()
