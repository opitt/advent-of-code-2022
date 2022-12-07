# https://adventofcode.com/2022/day/7
import os
from rich import print
from collections import defaultdict
from copy import deepcopy


def solve1(dir_sizes):
    res = sum([sum(s) for s in dir_sizes.values() if sum(s) <= 100000])
    print(f"Solution 1 ... {res}")
    return res

def solve2(dir_sizes):
    free = 70000000 - sum(dir_sizes["/"])
    need = 30000000 - free
    res = min(sum(size) for size in dir_sizes.values() if sum(size) >= need)
    print(f"Solution 2 ... {res}")
    return res


def get_dir_sizes(dirs):
    dir_sizes = deepcopy(dirs)
    for dir in sorted(dirs.keys(), key=len, reverse=True)[
        :-1
    ]:  # ignor the top level (-1)
        upper = ":".join(dir.split(":")[:-1])
        dir_sizes[upper].extend(dir_sizes[dir])
    dir_sizes = {dir: [sum(sizes)] for dir, sizes in dir_sizes.items()}
    #print(dir_sizes)
    return dir_sizes


def parse_input(lines):
    """parse the command input; look for $ commands and collect files sizes per directory in a dict.

    Args:
        lines (list): commands and output

    Returns:
        dict: with directory names and the corresponding list of file sizes
    """
    # $ cd /
    # $ ls
    # dir a
    # 14848514 b.txt
    # 8504156 c.dat
    # dir d
    # $ cd a

    dirs = defaultdict(list)
    wd = ""  # current working directory
    for line in [line.split() for line in lines]:
        if line[0] == "$" and line[1] == "cd":
            if line[2] == "..":
                # update current working directory to the parent directory
                wd = ":".join(wd.split(":")[:-1])
            else:
                # update current working directory to new directory
                wd += f"{line[2]}" if wd == "" else f":{line[2]}"
                dirs[wd] = []
        elif line[0].isdigit():
            # line contains output from ls: starts with file size
            dirs[wd].append(int(line[0]))
    return dirs


def main(test):

    print("****", "TEST" if test else "INPUT", "****************")
    # READ INPUT FILE
    script_path = os.path.dirname(os.path.realpath(__file__))
    with open(
        os.path.join(script_path, "test.txt" if test else "input.txt"), encoding="utf-8"
    ) as input:
        lines = input.read().rstrip().split("\n")

    dir_tree = parse_input(lines)
    dir_sizes = get_dir_sizes(dir_tree)

    # PART 1
    solve1(dir_sizes)

    # PART 2
    solve2(dir_sizes)


main(test=True)  # 95437, 24933642
main(test=False)  # 1581595, 1544176
