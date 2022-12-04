# https://adventofcode.com/2022/day/4
import os

from rich import print
from rich.table import Table
from rich.live import Live
from time import sleep

def solve1(lines):
    """Count pairs with fully overlapping sectors

    Args:
        lines (list): a list of elf-pair-sectors e.g.: 2-9,6-8

    Returns:
        int: number of elf pairs with at least one fully overlapping sectors
    """
    result=0
    for line in lines:
        elf1_sector, elf2_sector = [list(map(int,sector.split("-"))) for sector in line.split(",")]
        isOverlapping=lambda s1,s2: s1[0] <= s2[0] and s1[1] >= s2[1] 
        result += isOverlapping(elf1_sector,elf2_sector) or isOverlapping(elf2_sector,elf1_sector)

    print(
        f"Part 1 ... is {result}"
    )
    return result

def solve2(lines):
    """Count pairs with partially overlapping sectors

    Args:
        lines (list): a list of elf-pair-sectors e.g.: 2-7,6-8

    Returns:
        int: number of elf pairs with at least partially overlapping sectors
    """
    result=0
    for line in lines:
        elf1_sector, elf2_sector = [list(map(int,sector.split("-"))) for sector in line.split(",")]
        result += elf1_sector[1] < elf2_sector[0] or elf1_sector[0] > elf2_sector[1]

    print(
        f"Part 2 ... is {len(lines)-result}"
    )    
    return result

def visualize_sectors(lines):

    def generate_table(lines) -> Table:
        """Generate new table to visualise the sectores

        Args:
            lines (list): list of tuples containing team and sectors

        Returns:
            Table: renderable
        """
        table = Table()
        table.add_column("Team", justify="right")
        table.add_column("Sector cleaning", justify="center")

        EMPTY = " "
        CLEANING = f"[bold green]-[/bold green]"
        OVERLAP  = f"[red bold]=[/red bold]"

        for line in lines:
            sector = [EMPTY]*100
            elf1_sector, elf2_sector = [list(map(int,sector.split("-"))) for sector in line[1].split(",")]
            for s in range(elf1_sector[0], elf1_sector[1]+1):
                sector[s] = CLEANING
            for s in range(elf2_sector[0], elf2_sector[1]+1):
                sector[s] = CLEANING if sector[s]==EMPTY else OVERLAP
            sector = "".join(sector[1:])

            team = f"{line[0]:03}"
            if OVERLAP not in sector:    team = f"{team}" 
            elif CLEANING not in sector: team = f"[bold white on red]{team}"
            else: team = f"[red]{team}"
            
            table.add_row(
                    f"{team}", f"{sector}"
            )
        return table

    SHOW_LINES = 30
    with Live(generate_table(lines[:SHOW_LINES]), refresh_per_second=4) as live:
        for l in range(0,len(lines)-SHOW_LINES):
            sleep(0.1)
            live.update(generate_table(lines[l:l+SHOW_LINES]))

def main(test):

    # READ INPUT FILE
    script_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(script_path, "test.txt" if test else "input.txt"), encoding="utf-8") as input:
        lines = input.read().strip().split("\n")
    
    # PART 1
    solve1(lines) # == 542

    # PART 2
    solve2(lines) # == 900

    visualize_sectors([(i,line) for i, line in enumerate(lines)])

#main(test=True)
main(test=False)
