# https://adventofcode.com/2022/day/4
import os

def solve1(lines):
    result=0
    print(
        f"... is {result}"
    )
    return result

def solve2(lines):
    result=0
    print(
        f"... is {result}"
    )    
    return result
    
def main(test):

    # READ INPUT FILE
    script_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(script_path, "test.txt" if test else "input.txt"), encoding="utf-8") as input:
        lines = input.readlines()
    lines = list(map(str.strip, lines))
    
    # PART 1
    solve1(lines) # ==

    # PART 2
    solve2(lines) # == 

main(test=True)
#main(test=False)
