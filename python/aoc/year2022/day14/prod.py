from aoc.utils import *
from aoc.utils.vectors import *

def pour(M):
    p = V2(500,0)
    while True:
        if p.y > 1000:
            return None

        moved = False
        for d in [V2(0, 1), V2(-1, 1), V2(1, 1)]:
            v = M[p+d]
            if v == ' ':
                p += d
                moved = True
                break

        if not moved:
            M[p] = 'o'
            return p

def partA(filename: str) -> int:
    lines = getLines(filename)

    cavemap, minx, miny, maxx, maxy = getCavemap(lines)

    i = 1
    while True:
        # pour returns None if it "falls off" the map
        if pour(cavemap) is None:
            return i
        i += 1

def getCavemap(lines):
    walls = []
    for l in lines:
        points = list(map(lambda x:V2(*x), chunkBySize(ints(l), 2)))
        walls += [list(points)]

    minx, miny = 0, 0
    maxx, maxy = 0, 0
    for wall in walls:
        for (x, y) in wall:
            maxx = max(maxx, x)
            maxy = max(maxy, y)

    cavemap = SparseMap(unset=' ')

    for wall in walls:
        start = wall[0]
        for end in wall[1:]:
            for p in line(start, end):
                cavemap[p] = '#'
            start = end

    return cavemap, minx, miny, maxx, maxy

def partB(filename: str) -> int:
    lines = getLines(filename)

    cavemap, minx, miny, maxx, maxy = getCavemap(lines)

    # Add the floor
    for x in range(0,1000):
        cavemap[V2(x, maxy+2)] = '#'

    i = 1
    while True:
        p = pour(cavemap)
        # If it settles right where it comes out, we're done
        if p == V2(500,0):
            return i
        i += 1