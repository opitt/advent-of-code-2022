# https://adventofcode.com/2022/day/2
import os

def solve1(game_rounds):
    BEATS={"A":"C", # rock beats ...
           "B":"A", # paper beats ...
           "C":"B"} # scissor beats ...
    SHAPE_POINTS={"A":1,
                  "B":2,
                  "C":3} 
    WIN_POINTS={"draw":3,"loose":0,"win":6}
    trans="".maketrans("XYZ","ABC")
    
    score=0
    for elf, me  in [round.split() for round in game_rounds]:
        me=me.translate(trans)
        if BEATS[elf]==me:
            score += WIN_POINTS["loose"]
        elif elf==me:
            score += WIN_POINTS["draw"]
        else:
            score += WIN_POINTS["win"]
        score += SHAPE_POINTS[me]
    return score

def solve2(game_rounds):
    BEATS={"A":"C", # rock beats ...
           "B":"A", # paper beats ...
           "C":"B"} # scissor beats ...
    SHAPE_POINTS={"A":1,
                  "B":2,
                  "C":3} 
    WIN_POINTS={"draw":3,"loose":0,"win":6}
    BEATS_REVERSE={v:k for k,v in BEATS.items()}

    score=0
    for elf, result  in [round.split() for round in game_rounds]:
        # X means you need to lose
        # Y means you need to end the round in a draw
        # Z means you need to win
        if result=="X":
            me = BEATS_REVERSE[elf]
            score += WIN_POINTS["loose"]
        elif result =="Y":
            me = elf
            score += WIN_POINTS["draw"]
        else:
            me = BEATS_REVERSE[elf]
            score+= WIN_POINTS["win"]
        score += SHAPE_POINTS[me]
    return score
    
def main(test):
    # READ INPUT FILE
    script_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(script_path, "test.txt" if test else "input.txt"), encoding="utf-8") as input:
        lines = input.readlines()
    lines = list(map(str.strip, lines))
    
    # PART 1
    result=solve1(lines)
    print(
        f"The score is {result}."
    )
    # 9759

    # PART 2
    result=solve2(lines)
    print(
        f"The score is {result}."
    )
     # 12429

#main(test=True)
main(test=False)
