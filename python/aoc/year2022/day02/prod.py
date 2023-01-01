from aoc.utils import *

# Rock Paper Scissors
# i loses against i+1 mod 3
# i wins  against i-1 mod 3
hands: list[str] = ['R', 'P', 'S']

def partA(filename: str) -> int:
    return partAB(filename)[0]

def partB(filename: str) -> int:
    return partAB(filename)[1]

def partAB(filename: str) -> tuple[int, int]:
    data = []
    for l in getLines(filename):
        data += [l.strip().split(' ')]

    scoreA = 0
    scoreB = 0

    for (them, me) in data:
        them = 'ABC'.index(them)
        me = 'XYZ'.index(me)

        # Outcome score part 1
        if them == me:
            scoreA += 3
        elif (me - them) % 3 == 1:
            scoreA += 6

        # Hand score part 1
        scoreA += me + 1

        # Outcome score part 2
        scoreB += me * 3

        # Hand score part 2
        scoreB += (them + [-1, 0, 1][me]) % 3 + 1

    return scoreA, scoreB