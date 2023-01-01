from aoc.utils import *

def partA(filename: str) -> int:
    with open(filename) as fp:
        elves = fp.read().split('\n\n')

    return max([sum(ints(elf)) for elf in elves])

def partB(filename: str) -> int:
    with open(filename) as fp:
        elves = fp.read().split('\n\n')

    return sum(sorted([sum(ints(elf)) for elf in elves])[-3:])