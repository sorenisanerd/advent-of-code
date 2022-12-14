def pour(cavemap):
    (x, y) = (500, 0)
    while True:
        if y == len(cavemap)-1:
            return None
        if cavemap[y+1][x] == ' ':
            y += 1
            continue
        elif cavemap[y+1][x] in ['#', 'o']:
            if cavemap[y+1][x-1] == ' ':
                x, y = x-1, y+1
                continue
            else:
                if cavemap[y+1][x+1] == ' ':
                    x, y = x+1, y+1
                    continue
                else:
                    cavemap[y][x] = 'o'
                    return (x, y)

def printCaveMap(cavemap):
    for l in cavemap:
        print(''.join(l[470:530]))

def partA(filename: str) -> int:
    lines = getLines(filename)

    cavemap = getCavemap(lines)

    i = 1
    while True:
        # pour returns None if it "falls off" the map
        if pour(cavemap) is None:
            return i
        i += 1

def getCavemap(lines):
    walls = []
    for l in lines:
        points = map(lambda s:s.strip(), l.split(' -> '))
        points = map(lambda s:tuple(s.split(',')), points)
        points = map(lambda x:(int(x[0]), int(x[1])), points)
        walls += [list(points)]

    minx = 0
    miny = 0
    maxx = 0
    maxy = 0
    for wall in walls:
        for (x, y) in wall:
            maxx = max(maxx, x)
            maxy = max(maxy, y)

    cavemap = []

    for y in range(maxy + 2):
        cavemap.append([' '] * (maxx*2))

    for wall in walls:
        start = wall[0]
        for end in wall[1:]:
            if start[0] == end[0]:
                d = -(start[1] - end[1]) // abs(start[1] - end[1])
                for y in range(start[1], end[1] + d, d):
                    cavemap[y][start[0]] = '#'
            elif start[1] == end[1]:
                d = -(start[0] - end[0]) // abs(start[0] - end[0])
                for x in range(start[0], end[0] + d, d):
                    cavemap[start[1]][x] = '#'
            start = end
    return cavemap

def partB(filename: str) -> int:
    lines = getLines(filename)

    cavemap = getCavemap(lines)

    # Add the floor
    cavemap += [['#'] * len(cavemap[0])]

    i = 1
    while True:
        p = pour(cavemap)
        # If it settles right where it comes out, we're done
        if p == (500,0):
            return i
        i += 1

def getLines(filename: str) -> list:
    lines = []
    with open(filename) as f:
        for l in f:
            l = l.rstrip('\n')
            lines += [l]
    return lines

if __name__ == '__main__':
    import os.path
#    print(partA(os.path.dirname(__file__) + '/../data/sample.txt'))
    print(partA(os.path.dirname(__file__) + '/../data/input.txt'))
#    print(partB(os.path.dirname(__file__) + '/../data/sample.txt'))
    print(partB(os.path.dirname(__file__) + '/../data/input.txt'))