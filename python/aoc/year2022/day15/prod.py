from aoc.utils import *

def partA(filename: str, target_row=2000000) -> int:
    lines = getLines(filename)
    pairs, B = parseLines(lines)

    cols = set()
    for s, b, distance in pairs:
        radius = distance - abs(target_row - s.y)
        if radius > 0:
            for x in range(s.x-radius, s.x+radius+1):
                if (x, target_row) not in B:
                    cols.add(x)

    return len(cols)

def parseLines(lines):
    pairs = []
    B = set()
    for l in lines:
        sx, sy, bx, by = ints(l)
        s = V(sx, sy)
        b = V(bx, by)
        B.add(b)
        d = MD2(s, b)
        pairs += [(s, b, d)]
    return pairs,B

def followEdge(s, b):
    dist = MD2(s, b)

    p = V(s.x-dist-1, s.y)
    # and go down and to the right
    while p.x < s.x:
        yield p
        p += V(1, 1)

    # then go up and to the right
    while p.y > s.y:
        yield p
        p += (1, -1)

    # then up and to the left
    while p.x > s.x:
        yield p
        p += (-1, -1)

    # then down and to the left
    while p.y < s.y:
        yield p
        p += (-1, 1)

    # We should be back where we started
    assert p == (s.x-dist-1, s.y)


def partB(filename: str, minx=0, miny=0, maxx=4_000_000, maxy=4_000_000) -> int:
    lines = getLines(filename)
    pairs, _ = parseLines(lines)

    def isCovered(p, pairs=pairs):
        for (s, b, d) in pairs:
            if MD2(s, p) <= d:
                return True
        return False

    for (s, b, d) in pairs:
        for p in followEdge(s, b):
            if minx <= p.x <= maxx and miny <= p.y <= maxy:
                if not isCovered(p):
                    return p.x*4000000+p.y

    assert False

if __name__ == '__main__':
    import os.path
    print(partA(get_data_file_path('sample.txt'), 10))
    print(partA(get_data_file_path('input.txt'), 2000000))
    print(partB(get_data_file_path('sample.txt'), 0, 0, 20, 20))
    print(partB(get_data_file_path('input.txt'), 0, 0, 4000000, 4000000))
