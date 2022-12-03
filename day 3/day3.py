# https://adventofcode.com/2022/day/3
import os
from string import ascii_letters

from rich import print
from rich.console import Console
from rich.table import Table

def solve1(bags):
    
    def get_duplicate(bag):
        """Finds the single duplicate item in the 2 compartments of a bag.
        The compartments are first half and second half of the bag (string).

        Args:
            bag (str): items in the bag

        Returns:
            str: the single duplicate item among the compartments
        """
        l=len(bag)
        return (set(bag[:l//2]) & set(bag[l//2:])).pop()

    def visualize_bags(rows):
        table = Table(title="Elf bags")
        table.add_column("bag", justify="right", style="black", no_wrap=True)
        table.add_column(">1", justify="right", style="red bold")
        table.add_column("prio", justify="right", style="bright_green")
        table.add_column("compartment 1", justify="right", style="grey100")
        table.add_column("compartment 2", justify="left", style="grey100")
        console = Console(record=True)

        for i, r in enumerate(rows[:-1], start=1):
            item, item_prio, bag  = r[0], r[1], r[2]
            l = len(bag)
            c1 = bag[:l//2].replace(item,f"[red bold]{item}[/red bold]")
            c2 = bag[l//2:].replace(item,f"[red bold]{item}[/red bold]")
            table.add_row(f"{i}", f"{item}", f"{item_prio}", c1, c2)
        table.add_section()
        table.add_row(f"", f"", f"{rows[-1][1]}", "", "")
        
        console.print(table)
    
    rows_vis = []
    priority = 0
    for b in bags:
        item = get_duplicate(b)
        item_prio = ascii_letters.index(item)+1
        priority += item_prio

        rows_vis.append((item, item_prio, b)) # remember for visual representation of bags 

    rows_vis.append(("", priority, ""))  # remember total priority as last row for visual representation of bags
    visualize_bags(rows_vis)

    print(
        f"The sum of priorities of duplicate items per bag is {priority}"
    )
    return priority

def solve2(bags):

    def get_duplicate(bags):
        return (set(bags[0]) & set(bags[1]) & set(bags[2])).pop()

    priority=0
    for group_bags in [bags[bag_no:bag_no+3] for bag_no in range(0,len(bags),3)]:
        item=get_duplicate(group_bags)
        priority += ascii_letters.index(item)+1
    print(
        f"The priority of duplicate items in groups is {priority}"
    )    
    return priority
    
def main(test):

    # READ INPUT FILE
    script_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(script_path, "test.txt" if test else "input.txt"), encoding="utf-8") as input:
        lines = input.readlines()
    rucksacks = list(map(str.strip, lines))
    
    # PART 1
    solve1(rucksacks) # ==7903

    # PART 2
    solve2(rucksacks) # ==2548 

#main(test=True)
main(test=False)
