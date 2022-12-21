# https://adventofcode.com/2022/day/21
from collections import defaultdict
from copy import deepcopy
import os
import re
from time import time
from rich import print


def solve(m, m_ref):
    while type(m["root"]) != int:
        for mname, n in [(mname, n) for mname, n in m.items() if type(n) in (int, float)]:
            for mref in m_ref[mname]:
                if type(m[mref]) == str:
                    m[mref] = m[mref].replace(mname, str(int(n)))
                    if re.fullmatch("\([-]?\d+ [+/*-] [-]?\d+\)", m[mref]):
                        m[mref] = eval(m[mref])
            m_ref.pop(mname)

    print("")
    print("Solution 1 ...:", m["root"])


def solve2(m, m_ref):
    m["root"] = m["root"].replace("+", "==")
    m["humn"] = "x"

    while len(m_ref) > 2:  # type(m["root"]) != int:
        for mname, n in m.items():
            if type(n) == int or re.fullmatch("\((x|[-]?\d+) [+/*-=]=? (x|[-]?\d+)\)", n):
                # replace
                for mref in m_ref[mname]:
                    m[mref] = m[mref].replace(mname, str(int(n)) if type(n) == int else n)
                    if re.fullmatch("\([-]?\d+ [+/*-] [-]?\d+\)",m[mref]):
                        m[mref] = eval(m[mref])
                m_ref.pop(mname)

    print("")
    print("Solution 1 ...:", m["root"])


def main(test):

    print("")
    print("****", "TEST" if test else "INPUT", "****************")
    # READ INPUT FILE
    script_path = os.path.dirname(os.path.realpath(__file__))
    filename = "test.txt" if test else "input.txt"
    with open(os.path.join(script_path, filename), encoding="utf-8") as input:
        lines = input.read().strip().split("\n")

    # root: pppw + sjmn
    # dbpl: 5
    m = defaultdict(list)
    m_ref = defaultdict(list)

    for monkey in [line.split() for line in lines]:
        mname, *mops = monkey
        mname = mname[:-1]  # remove :
        if len(mops) == 1:
            m[mname] = int(mops[0])
        else:
            m[mname] = f"({mops[0]} {mops[1]} {mops[2]})"
            m_ref[mops[0]].append(mname)
            m_ref[mops[2]].append(mname)

    # PART 1
    start = time()
    solve(deepcopy(m), deepcopy(m_ref))
    print(f"{time() - start:5f} seconds")

    # PART 2
    start = time()
    solve2(deepcopy(m), deepcopy(m_ref))
    print(f"{time() - start:5f} seconds")


main(test=True)  #
main(test=False)  #
