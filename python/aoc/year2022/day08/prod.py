from aoc.utils import *

def partA(filename: str) -> int:
    M = Map(getLines(filename), mapFunc=int)

    def checkDirection(p, d, M=M):
        val = M[p]
        while True:
            p += d
            new_value = M[p]
            if new_value == OutOfBounds:
                return True
            elif new_value >= val:
                return False

    counter = 0
    for p in M:
        val = M[p]

        for d in map(V, four_directions):
            if checkDirection(p, d):
                counter += 1
                break

    return counter

def partB(filename: str) -> int:
    M = Map(getLines(filename), mapFunc=int)

    def checkDirection(p, d, M=M):
        val = M[p]
        rv = 0
        while True:
            p += d
            new_value = M[p]

            if new_value == OutOfBounds:
                return rv

            rv += 1

            if new_value >= val:
                return rv


    rv = 0
    for p in M:
        cand = 1
        for d in map(V, four_directions):
            cand *= checkDirection(p, d)
        rv = max(rv, cand)

    return rv