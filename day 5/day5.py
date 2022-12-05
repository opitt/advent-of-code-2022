# https://adventofcode.com/2022/day/5
import os
from itertools import takewhile
import re
from copy import deepcopy

def solve1(stacks, commands):
    for crates, from_s, to_s in commands:
        for _ in range(crates):
            c = stacks[from_s].pop()
            stacks[to_s].append(c)
    res = "".join([stacks[id][-1] for id in range(1, len(stacks))])
    print(f"solution 1: {res}")
    return res


def solve2(stacks, commands):
    for crates, from_s, to_s in commands:
        pile = []
        for _ in range(crates):
            pile.append(stacks[from_s].pop())
        stacks[to_s].extend(pile[::-1])
    res = "".join([stacks[id][-1] for id in range(1, len(stacks))])
    print(f"solution 2: {res}")
    return res


def main(test):

    # READ INPUT FILE
    script_path = os.path.dirname(os.path.realpath(__file__))
    with open(
        os.path.join(script_path, "test.txt" if test else "input.txt"), encoding="utf-8"
    ) as input:
        lines = input.read().rstrip().split("\n")

    #    [D]
    # [N] [C]
    # [Z] [M] [P]
    # 1   2   3
    stack_ids, *crate_content = list(takewhile(lambda x: x != "", lines))[::-1]
    height = len(crate_content)
    stack_count = len(re.findall("[0-9]", stack_ids))
    stacks = [[] for _ in range(stack_count + 1)]  # dummy stack to index crates by 1
    for line in crate_content:
        content = [line[content_pos] for content_pos in range(1, len(line), 4)]
        for stack_id, c in enumerate(content, 1):
            if c != " ":
                stacks[stack_id].append(c)
    commands = [
        tuple(map(int, re.findall("[0-9]+", command_line)))
        for command_line in lines[height + 1 + 1 :]
    ]

    # PART 1
    
    solve1(deepcopy(stacks), commands)  # ==

    # PART 2
    solve2(deepcopy(stacks), commands)  # ==


#main(test=True)  # MCD
main(test=False)
