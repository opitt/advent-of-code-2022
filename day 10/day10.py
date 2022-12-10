# https://adventofcode.com/2022/day/10
import os
from rich import print

def nextCommand(cmds):
    NOOP_CYCLES = 1
    ADDX_CYCLES = 2
    cmd, cmd_n = cmds.pop(0), 0
    if cmd.startswith("addx"):
        cmd, cmd_n = cmd.split()
    return cmd, int(cmd_n), NOOP_CYCLES if cmd == "noop" else ADDX_CYCLES

def draw_crt(crt):
    fg = "green"
    bg = "grey3"
    for row in range(0, len(crt), 40):
        crt_line = crt[row : row + 40]
        crt_line = crt_line.replace("#", f"[{fg} on {bg}]#[/{fg} on {bg}]")
        crt_line = crt_line.replace(".", f"[{fg} on {bg}] [/{fg} on {bg}]")
        print(crt_line)


def solve(cmds):

    cycle, x = 0, 1
    cmd, cmd_n, cmd_cycle = nextCommand(cmds)
    cycle_sig, cycle_x = [0], []
    while cmds:
        cycle += 1  # cycle begins
        if cmd_cycle == 0:  # when command finished
            cmd, cmd_n, cmd_cycle = nextCommand(cmds)
        cmd_cycle -= 1  # do the command
        cycle_sig.append(x * cycle)  # signal strength during the cycle
        cycle_x.append(x)
        if cmd_cycle == 0 and cmd == "addx":
            x += cmd_n

    res = sum(cycle_sig[cycle] for cycle in (20, 60, 100, 140, 180, 220))
    print(f"Solution 1 ... sum of signal strengths: {res}")

    # PART 2
    crt = ""
    for cycle, x in enumerate(cycle_x):
        crt_pos = cycle % 40  # one crt row: 0-39
        crt += "#" if crt_pos in (x - 1, x, x + 1) else "."

    print(f"Solution 2 ... read the screen")
    draw_crt(crt)


def main(test):

    print("****", "TEST" if test else "INPUT", "****************")
    # READ INPUT FILE
    script_path = os.path.dirname(os.path.realpath(__file__))
    with open(
        os.path.join(script_path, "test.txt" if test else "input.txt"), encoding="utf-8"
    ) as input:
        lines = input.read().rstrip().split("\n")

    # PART 1 and 2
    solve(lines)


main(test=True)  # 13140,
main(test=False)  # 14920, BUCACBUZ
