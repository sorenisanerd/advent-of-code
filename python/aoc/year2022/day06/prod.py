from aoc.utils import *

def partA(filename: str, n=4) -> int:
    d = getData(filename)
    for i in range(n, len(d)+1):
        if len(set(d[i-n:i])) == n:
            return i
    return -1

def partB(filename: str) -> int:
    return partA(filename, 14)