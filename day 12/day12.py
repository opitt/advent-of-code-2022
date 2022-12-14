from math import inf
from rich import print
import os

def solve1(S,E,nodes):
    dist = {S:0}
    visited=[]
    pre={}

    dist={(y,x):inf for x in range(len(nodes[0])) for y in range(len(nodes))}
    dist[(0,0)]=0

    def get_neighbours(nodes, node):
        # neighbours not visited
        # neighbours possible to visit
        neighbours = []
        Y,X = node
        H = ord(nodes[Y][X])
        # up
        y = Y-1
        if y >= 0: #up
            h = ord(nodes[y][X])
            if h <= H or h==H+1:
                if (y,X) not in visited:
                    neighbours.append((y,X))
        y = Y+1
        if y < len(nodes): #down
            h = ord(nodes[y][X])
            if h <= H or h==H+1:
                if (y,X) not in visited:
                    neighbours.append((y,X))
        x = X-1
        if x >= 0: #left
            h = ord(nodes[Y][x])
            if h <= H or h==H+1:
                if (Y,x) not in visited:
                    neighbours.append((Y,x))
        x = X+1
        if x < len(nodes[0]): #dright
            h = ord(nodes[Y][x])
            if h <= H or h==H+1:
                if (Y,x) not in visited:
                    neighbours.append((Y,x))
        return neighbours

    while len(visited) < len(dist):
        node = min([node for node in dist if node not in visited],key=lambda yx: dist[yx])
        visited.append(node)
        print(len(visited),"of",len(dist))
        if node == E:
            break
        for n in get_neighbours(nodes, node):
            d = dist[node] + 1
            if d < dist[n]:
                dist[n] = d
                pre[n] = node
    print(f"Solution part 1 ... {dist[E]}")


def main(test):

    print("****", "TEST" if test else "INPUT", "****************")
    # READ INPUT FILE
    script_path = os.path.dirname(os.path.realpath(__file__))
    with open(
        os.path.join(script_path, "test.txt" if test else "input.txt"), encoding="utf-8"
    ) as input:
        lines = input.read().rstrip().split("\n")

    for y,line in enumerate(lines):
        if line.find("S")>=0:
            S=(y,line.find("S"))
            lines[y] = line.replace("S","a")
        if line.find("E")>=0:
            E=(y,line.find("E"))
            lines[y] = line.replace("E","z")

    # PART 1
    solve1(S,E,lines)

    # PART 2


main(test=True)  # 
main(test=False)  #
