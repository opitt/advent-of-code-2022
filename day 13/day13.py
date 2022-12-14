from itertools import zip_longest
import os
from rich import print
from copy import deepcopy
from functools import cmp_to_key


def compare(p1, p2):
    #    If both values are integers, the lower integer should come first.
    #    If the left integer is lower than the right integer, the inputs are in the right order.
    #    If the left integer is higher than the right integer, the inputs are not in the right order.
    #    Otherwise, the inputs are the same integer; continue checking the next part of the input.
    #
    #    If both values are lists, compare the first value of each list, then the second value, and so on.
    #    If the left list runs out of items first, the inputs are in the right order.
    #    If the right list runs out of items first, the inputs are not in the right order.
    #    If the lists are the same length and no comparison makes a decision about the order,
    #    continue checking the next part of the input.
    #
    #    If exactly one value is an integer, convert the integer to a list which contains that integer
    #    as its only value, then retry the comparison.
    #    For example, if comparing [0,0,0] and 2, convert the right value to [2] (a list containing 2);
    #    the result is then found by instead comparing [0,0,0] and [2].

    for left, right in zip_longest(p1, p2, fillvalue=None):
        #print(p1, p2, sep="\n")
        inorder = 0
        if type(left) == int and type(right) == int:
            if left < right:
                inorder = -1
            elif left > right:
                inorder = 1
        elif type(left) == list and type(right) == int:
            inorder = compare(left, [right])
        elif type(right) == list and type(left) == int:
            inorder = compare([left], right)
        elif type(right) == list and type(left) == list:
            inorder = compare(left, right)
        elif left == None:
            inorder = -1
        elif right == None:
            inorder = 1

        if inorder == 0:
            continue
        return inorder
    return 0


def solve1(pairs):
    correct = 0
    for idx, p in enumerate(pairs, start=1):
        p1, p2 = p.split("\n")
        if compare(eval(p1), eval(p2)) == -1:
            correct += idx
    print(f"Solution part 1 ... {correct}")


def solve2(lines):
    M2, M6 = "[[2]]", "[[6]]"
    lines.extend([M2, M6])
    #lines = sorted(lines, key=cmp_to_key(compare))

    swapped = True
    while swapped:
        swapped = False
        for idx in range(len(lines)-1):
            p1, p2 = lines[idx], lines[idx+1]
            if compare(eval(p1), eval(p2)) == 1:
                lines[idx], lines[idx+1] = lines[idx+1], lines[idx]
                swapped = True
    code = (lines.index(M2)+1) * (lines.index(M6)+1)
    print(f"Solution part 2 ... {code}")


def main(test):

    print("****", "TEST" if test else "INPUT", "****************")
    # READ INPUT FILE
    script_path = os.path.dirname(os.path.realpath(__file__))
    with open(
        os.path.join(script_path, "test.txt" if test else "input.txt"), encoding="utf-8"
    ) as input:
        L = input.read().rstrip()

    # PART 1
    pairs = L.split("\n\n")
    solve1(pairs)

    # PART 2
    lines = list(filter(lambda l: l != "", L.split("\n")))
    solve2(deepcopy(lines))


main(test=True)  # 13, 140
#main(test=False)  # 6272, 22288
