import re
import time

def dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def partA(filename: str, target_row) -> int:
    lines = getLines(filename)
    pairs, B = parseLines(lines)

    cols = set()
    for pair in pairs:
        sx, sy, bx, by, distance = pair
        radius = distance - abs(target_row - sy)
        if radius > 0:
            for x in range(sx-radius, sx+radius+1):
                if (x, target_row) not in B:
                    cols.add(x)

    return len(cols)

def parseLines(lines):
    pairs = []
    B = set()
    pattern = re.compile('Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)')
    for l in lines:
        sx, sy, bx, by = list(map(int, pattern.match(l).groups()))
        B.add((bx, by))
        d = dist(sx, sy, bx, by)
        pairs += [(sx, sy, bx, by, d)]
    return pairs,B

def followEdge(sx, sy, bx, by):
    dist = abs(sx - bx) + abs(sy - by)
    # Start right beyond the the left corner...
    x, y = sx-dist-1, sy
    # and go down and to the right
    while x < sx:
        yield x, y
        x += 1
        y += 1
    # then go up and to the right
    while y > sy:
        yield x, y
        x += 1
        y -= 1
    # then up and to the left
    while x > sx:
        yield x, y
        x -= 1
        y -= 1
    # then down and to the left
    while y < sy:
        yield x, y
        x -= 1
        y += 1
    # We should be back where we started
    assert (x, y) == (sx-dist-1, sy)


def partB(filename: str, minx, miny, maxx, maxy) -> int:
    lines = getLines(filename)
    pairs, _ = parseLines(lines)

    def isCovered(x, y, pairs=pairs):
        for pair in pairs:
            sx, sy, _, _, d = pair
            if dist(sx, sy, x, y) <= d:
                return True
        return False

    for pair in pairs:
        for (x, y) in followEdge(*pair[:-1]):
            if minx <= x <= maxx and miny <= y <= maxy:
                if not isCovered(x, y):
                    return x*4000000+y

    assert False

def getLines(filename: str) -> list:
    lines = []
    with open(filename) as f:
        for l in f:
            l = l.rstrip('\n')
            lines += [l]
    return lines

if __name__ == '__main__':
    import os.path
    print(partA(os.path.dirname(__file__) + '/../data/sample.txt', 10))
    print(partA(os.path.dirname(__file__) + '/../data/input.txt', 2000000))
    print(partB(os.path.dirname(__file__) + '/../data/sample.txt', 0, 0, 20, 20))
    print(partB(os.path.dirname(__file__) + '/../data/input.txt', 0, 0, 4000000, 4000000))
