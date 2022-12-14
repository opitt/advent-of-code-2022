from math import inf
from rich import print
import os


def solve1(S, E, nodes):
    visited = []
    dist = {(y, x): inf for x in range(
        len(nodes[0])) for y in range(len(nodes))}
    dist[S] = 0
    pre = {}

    def get_neighbours(node):

        def check_cangothere(y, x, H):
            h = ord(nodes[y][x])
            if (h <= H or h == H+1) and (y, x) not in visited:
                neighbours.append((y, x))

        neighbours = []
        Y, X = node
        H = ord(nodes[Y][X])
        for y, x in [(Y-1, X), (Y+1, X), (Y, X-1), (Y, X+1)]:
            if 0 <= y < len(nodes) and 0 <= x < len(nodes[0]):
                check_cangothere(y, x, H)
        return neighbours

    while dist[E] == inf:  # len(visited) < len(dist):
        node = min([node for node in dist if node not in visited],
                   key=lambda node: dist[node])
        visited.append(node)
        print(f"{node=} {dist[node]=} {len(visited)} of {len(dist)}")
        # if node == E:
        #    break
        for n in get_neighbours(node):
            d = dist[node] + 1
            if d < dist[n]:
                dist[n] = d
                pre[n] = node
    print(f"Solution part 1 ... {dist[E]}")


def solve2(S, nodes):
    visited = []
    dist = {(y, x): inf for x in range(
        len(nodes[0])) for y in range(len(nodes))}
    dist[S] = 0
    pre = {}

    def get_neighbours(node):

        def check_cangothere(y, x, H):
            h = ord(nodes[y][x])
            if (h >= H or h == H-1) and (y, x) not in visited:
                neighbours.append((y, x))

        neighbours = []
        Y, X = node
        H = ord(nodes[Y][X])
        for y, x in [(Y-1, X), (Y+1, X), (Y, X-1), (Y, X+1)]:
            if 0 <= y < len(nodes) and 0 <= x < len(nodes[0]):
                check_cangothere(y, x, H)
        return neighbours

    while len(visited) < len(dist):
        node = min([node for node in dist if node not in visited],
                   key=lambda node: dist[node])
        visited.append(node)
        Y, X = node
        print(
            f"{node=} {dist[node]=} {nodes[Y][X]} {len(visited)} of {len(dist)}")
        if nodes[Y][X] == "a":
            break
        for n in get_neighbours(node):
            d = dist[node] + 1
            if d < dist[n]:
                dist[n] = d
                pre[n] = node
    print(f"Solution part 2 ... {dist[node]}")


def main(test):

    print("****", "TEST" if test else "INPUT", "****************")
    # READ INPUT FILE
    script_path = os.path.dirname(os.path.realpath(__file__))
    with open(
        os.path.join(script_path, "test.txt" if test else "input.txt"), encoding="utf-8"
    ) as input:
        lines = input.read().rstrip().split("\n")

    for y in range(len(lines)):
        if lines[y].find("S") >= 0:
            S = (y, lines[y].find("S"))
            lines[y] = lines[y].replace("S", "a")
        if lines[y].find("E") >= 0:
            E = (y, lines[y].find("E"))
            lines[y] = lines[y].replace("E", "z")

    # PART 1
    # search from start to end
    # jumping down, climbin up 1
    solve1(S, E, lines)

    # PART 2
    # search from end to the first "a"
    # climbing up any, jumping down 1
    solve2(E, lines)


main(test=True)  # 30, 29
main(test=False)  # 380, 375
