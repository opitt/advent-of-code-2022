# https://adventofcode.com/2022/day/4
import os

def solve1(lines):
    """Count pairs with fully overlapping sectors

    Args:
        lines (list): a list of elf-pair-sectors e.g.: 2-9,6-8

    Returns:
        int: number of elf pairs with at least one fully overlapping sectors
    """
    result=0
    for line in lines:
        elf1_sector, elf2_sector = [list(map(int,sector.split("-"))) for sector in line.split(",")]
        isOverlapping=lambda s1,s2: s1[0] <= s2[0] and s1[1] >= s2[1] 
        result += isOverlapping(elf1_sector,elf2_sector) or isOverlapping(elf2_sector,elf1_sector)

    print(
        f"Part 1 ... is {result}"
    )
    return result

def solve2(lines):
    """Count pairs with partially overlapping sectors

    Args:
        lines (list): a list of elf-pair-sectors e.g.: 2-7,6-8

    Returns:
        int: number of elf pairs with at least partially overlapping sectors
    """
    result=0
    for line in lines:
        elf1_sector, elf2_sector = [list(map(int,sector.split("-"))) for sector in line.split(",")]
        result += elf1_sector[1] < elf2_sector[0] or elf1_sector[0] > elf2_sector[1]

    print(
        f"Part 2 ... is {len(lines)-result}"
    )    
    return result
    
def main(test):

    # READ INPUT FILE
    script_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(script_path, "test.txt" if test else "input.txt"), encoding="utf-8") as input:
        lines = input.read().strip().split("\n")
    
    # PART 1
    solve1(lines) # == 542

    # PART 2
    solve2(lines) # == 900

#main(test=True)
main(test=False)
