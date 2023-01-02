from aoc.utils import *

def getSet(elf):
    start, end = map(int, elf.split('-'))
    return set(range(start, end+1))

def eitherIsSubset(s1, s2) -> bool:
    return s1.issubset(s2) or s2.issubset(s1)

def hasOverlap(s1, s2) -> bool:
    return bool(s1.intersection(s2))

def partA(filename: str) -> int:
    return sum(eitherIsSubset(s1, s2) and 1 or 0 for s1, s2 in
        [map(getSet, l.split(',')) for l in getLines(filename)])

def partB(filename: str) -> int:
    return sum(hasOverlap(s1, s2) and 1 or 0 for s1, s2 in
        [map(getSet, l.split(',')) for l in getLines(filename)])