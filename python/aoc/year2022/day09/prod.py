from aoc.utils import *

def partA(filename: str) -> int:
    lines = getLines(filename)
    return partB(filename, n=2)

def track(h, t):
    if abs(h.x-t.x) == 2 and (h.y == t.y):
        t += V((h.x-t.x)//2, 0)
    elif abs(h.y-t.y) == 2 and (h.x == t.x):
        t += V(0, (h.y-t.y)//2)
    elif abs(h.y-t.y)>1 or abs(h.x-t.x)>1:
        t += V((h.x-t.x)//abs(h.x-t.x), (h.y-t.y)//abs(h.y-t.y))
    return t


def partB(filename: str, n=10) -> int:
    lines = getLines(filename)

    visited = set()
    knots = [V(0,0)]*n

    d = {'U': V(0,1),
                       'D': V(0,-1),
                       'R': V(1,0),
                       'L': V(-1,0)}

    for l in lines:
        direction, length = l.split(' ')
        length = int(length)
        for _ in range(length):
            knots[0] += d[direction]
            for i in range(len(knots)-1):
                knots[i+1] = track(knots[i], knots[i+1])

            visited.add((knots[-1]))

    return len(visited)