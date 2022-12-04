# https://adventofcode.com/2022/day/4
import os

def solve1(lines):
    result=0
    for line in lines:
        #2-4,6-8
        elf1, elf2 = [list(map(int,elf.split("-"))) for elf in line.split(",")]
        print(elf1,elf2)
        s1 = elf1[0] <= elf2[0] and elf1[1] >= elf2[1] 
        s2 = elf2[0] <= elf1[0] and elf2[1] >= elf1[1] 
        result += s1 or s2

    print(
        f"... is {result}"
    )
    return result

def solve2(lines):
    result=0
    for line in lines:
        #2-4,6-8
        elf1, elf2 = [list(map(int,elf.split("-"))) for elf in line.split(",")]
        #print(elf1,elf2)
        s1 = elf1[1] < elf2[0] or elf1[0] > elf2[1]
        #s2 = elf2[0] > elf1[1] or elf2[1] < elf1[0]
        result += s1 # s2

    print(
        f"... is {len(lines)-result}"
    )    
    return result
    
def main(test):

    # READ INPUT FILE
    script_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(script_path, "test.txt" if test else "input.txt"), encoding="utf-8") as input:
        lines = input.read().strip().split("\n")
    
    # PART 1
    solve1(lines) # ==

    # PART 2
    solve2(lines) # == 

#main(test=True)
main(test=False)
