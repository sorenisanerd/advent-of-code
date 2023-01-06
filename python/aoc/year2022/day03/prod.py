import string
from aoc.utils import *

def getScore(s: str) -> int:
    return string.ascii_letters.index(s)+1

def partA(filename: str):
    return sum(getScore(set(comp1).intersection(comp2).pop())
               for comp1, comp2 in [chunkByCount(l.strip(), 2) for l in getLines(filename)])

def partB(filename: str) -> int:
    return sum(getScore(set(elf1).intersection(elf2).intersection(elf3).pop())
               for elf1, elf2, elf3 in chunkBySize(getLines(filename), 3))