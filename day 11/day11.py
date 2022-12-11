# https://adventofcode.com/2022/day/11
from copy import deepcopy
import os
import re
from rich import print


def solve(monkeys):
    # PART 1
    for round in range(20):
        for monkey in monkeys.values():
            for _ in range(len(monkey.items)):
                to, item = monkey.inspect()
                monkeys[to].catch(item)
    # check, the monkey business
    business = sorted([monkey.inspections for monkey in monkeys.values()])
    res = business[-2]*business[-1]
    print(f"Solution 1 ... : {res}")


def solve2(monkeys):
    # PART 2
    for round in range(1,10000+1):
        for monkey in monkeys.values():
            for _ in range(len(monkey.items)):
                to, item = monkey.inspect2()
                monkeys[to].catch(item)
        if round in (1,20,1000):
            print("-- Round ", round)
            print(*[(m.id,m.inspections) for m in monkeys.values()])
    # check, the monkey business
    business = sorted([monkey.inspections for monkey in monkeys.values()])
    res = business[-2]*business[-1]
    print(f"Solution 2 ... : {res}")


class Monkey():

    def __init__(self, monkey, items, op, op_val, test, to_true, to_false):
        self.id = monkey
        self.items = deepcopy(items)
        self.op = op
        self.op_val = op_val
        self.test = test
        self.to_true = to_true
        self.to_false = to_false
        self.inspections = 0

    def inspect(self):
        self.inspections += 1
        item = self.items.pop(0)
        o1 = item
        o2 = item if self.op_val == "old" else int(self.op_val)
        new = o1*o2 if self.op == "*" else o1+o2
        new = int(new / 3)
        remainder = new%self.test
        to = self.to_true if remainder == 0 else self.to_false
        return to, new

    def inspect2(self):
        self.inspections += 1
        item = self.items.pop(0)
        o1 = item
        o2 = item if self.op_val == "old" else int(self.op_val)
        new = o1*o2 if self.op == "*" else o1+o2
        div, remainder = divmod(new, self.test)
        to = self.to_true if remainder == 0 else self.to_false
        if remainder == 0:
            new = div
        else:
            new = remainder
        return to, new

    def catch(self, item):
        self.items.append(item)


def parse_input(lines):
    monkeys = {}
    for line in lines:
        if line.startswith("Monkey"):
            n = int(line.split()[-1][:-1])  # skip :
        elif line.startswith("  Starting"):
            items = list(map(int, re.findall("(\d+)", line)))
        elif line.startswith("  Operation"):
            m = re.findall("old ([+*]) (old|\d+)", line)
            op = m[0][0]
            op_val = m[0][1]
        elif line.startswith("  Test:"):
            test = int(line.split()[-1])
        elif line.startswith("    If true:"):
            to_true = int(line.split()[-1])
        elif line.startswith("    If false:"):
            to_false = int(line.split()[-1])
        elif line == "":
            monkeys[n] = Monkey(n, items, op, op_val, test, to_true, to_false)
    monkeys[n] = Monkey(n, items, op, op_val, test, to_true, to_false)
    return monkeys


def main(test):

    print("****", "TEST" if test else "INPUT", "****************")
    # READ INPUT FILE
    script_path = os.path.dirname(os.path.realpath(__file__))
    with open(
        os.path.join(script_path, "test.txt" if test else "input.txt"), encoding="utf-8"
    ) as input:
        lines = input.read().rstrip().split("\n")

    monkeys = parse_input(lines)

    # PART 1
    solve(deepcopy(monkeys))

    # PART 2
    solve2(deepcopy(monkeys))


main(test=True)  # 10605, ...
# main(test=False)  # 120384, ...
