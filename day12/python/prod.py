def getCoords(lines, s):
    for l in range(len(lines)):
        if s in lines[l]:
            return (lines[l].index(s), l)
    assert False

def getNeighbors(x, y):
    return [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]

def isMoveValid(lines, x1, y1, x2, y2):
    f = lines[y1][x1]
    t = lines[y2][x2]
    if f == 'S':
        f = 'a'
    if t == 'E':
        t = 'z'
    if ord(t) <= ord(f)+1:
        return True
    return False

def isWithinBounds(lines, x, y):
    if 0 <= y < len(lines):
        if 0 <= x < len(lines[y]):
            return True
    return False

def dijkstra(lines, starts, end):
    from queue import PriorityQueue
    q = PriorityQueue()

    for s in starts:
        q.put((0, s))

    visited = set()
    while not q.empty():
        cost, (x, y) = q.get()

        if (x, y) == end:
            return cost

        if (x, y) in visited:
            continue
        visited.add((x, y))

        for nx, ny in getNeighbors(x, y):
            if isWithinBounds(lines, nx, ny):
                if isMoveValid(lines, x, y, nx, ny):
                    q.put((cost+1, (nx, ny)))
    assert False

def partA(filename: str) -> int:
    lines = getLines(filename)

    start = getCoords(lines, 'S')
    end = getCoords(lines, 'E')
    return dijkstra(lines, [start], end)

def partB(filename: str) -> int:
    lines = getLines(filename)

    end = getCoords(lines, 'E')
    starts = []
    for x in range(len(lines[0])):
        for y in range(len(lines)):
            if lines[y][x] in ['a', 'S']:
                starts += [(x, y)]
    return dijkstra(lines, starts, end)

def getLines(filename: str) -> list:
    lines = []
    with open(filename) as f:
        for l in f:
            l = l.rstrip('\n')
            lines += [l]
    return lines

if __name__ == '__main__':
    import os.path
    print(partA(os.path.dirname(__file__) + '/../data/sample.txt'))
    print(partA(os.path.dirname(__file__) + '/../data/input.txt'))
    print(partB(os.path.dirname(__file__) + '/../data/input.txt'))