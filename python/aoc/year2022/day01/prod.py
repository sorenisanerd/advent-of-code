from aoc.utils import *

def partA(filename: str) -> int:
    elves = getData(filename).split('\n\n')

    return max([sum(ints(elf)) for elf in elves])

def partB(filename: str) -> int:
    elves = getData(filename).split('\n\n')

    return sum(sorted([sum(ints(elf)) for elf in elves])[-3:])