# https://adventofcode.com/2022/day/3
import os
from string import ascii_letters

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

    priority=0
    for b in bags:
        item=get_duplicate(b)
        priority += ascii_letters.index(item)+1
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
