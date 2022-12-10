# https://adventofcode.com/2022/day/10
import math
import os
from rich import print


def solve1(cmds):
    # Find the signal strength during the 20th, 60th, 100th, 140th, 180th, and 220th cycles.
    # What is the sum of these six signal strengths?

    def nextCommand(cmds):
        cmd, cmd_n = cmds.pop(0), 0
        if cmd.startswith("addx"):
            cmd, cmd_n = cmd.split()
        return cmd, int(cmd_n), 1 if cmd == "noop" else 2

    # noop
    # addx 3
    # addx -5

    cycle = 0
    cmd, cmd_n, cmd_cycle = nextCommand(cmds)
    X = 1
    signal_strength = [0]
    while cmds:
        cycle += 1
        # next command
        if cmd_cycle == 0:
            cmd, cmd_n, cmd_cycle = nextCommand(cmds)
        # cycle begins
        # do the command
        cmd_cycle -= 1
        # signal strength during the cycle
        signal = X * cycle
        if cmd_cycle == 0:
            if cmd == "noop":
                pass
            elif cmd == "addx":
                X += cmd_n
        print(f"{cycle=}, {signal=}, [{cmd_cycle}] {cmd} {cmd_n}, {X=}")
        signal_strength.append(signal)
        # end cycle

    res = 0
    for cycle in (20, 60, 100, 140, 180, 220):
        print(signal_strength[cycle])
        res += signal_strength[cycle]
    print(f"Solution 1 ... {res}")

    # PART 2
    # res = solution(cmds, knots)
    print(f"Solution 2 ... {res}")


def main(test):

    print("****", "TEST" if test else "INPUT", "****************")
    # READ INPUT FILE
    script_path = os.path.dirname(os.path.realpath(__file__))
    with open(
        os.path.join(script_path, "test.txt" if test else "input.txt"), encoding="utf-8"
    ) as input:
        lines = input.read().rstrip().split("\n")

    # PART 1
    solve1(lines)


main(test=True)  # 13140,
main(test=False)  #
