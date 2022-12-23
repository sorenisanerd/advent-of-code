directions = [(1,0), (0,1), (-1,0), (0,-1)]

def printMap(M, curPos):
    for y, l in enumerate(M):
        print(''.join([(x,y) == curPos and 'X' or c for x, c in enumerate(l)]))

def getRegion(x, y, cubeSize):
    return (x//cubeSize, y//cubeSize)

def getRegions(M, cubeSize):
    for y in range(0, len(M), cubeSize):
        for x in range(0, len(M[y]), cubeSize):
            if M[y][x] != ' ':
                yield (x//cubeSize, y//cubeSize)

def getNeighborDirections(dir):
    return ((dir[0] + dir[1]*dir[1], dir[1] + dir[0]*dir[0]),
            (dir[0] - dir[1]*dir[1], dir[1] - dir[0]*dir[0]))

def getAllNeighborEdges(x, y, dir):
    for edge in getPossibleCornerEdges(x, y, dir):
        yield edge
    yield x+dir[1], y+dir[0], dir
    yield x-dir[1], y-dir[0], dir

def getPossibleCornerEdges(x, y, dir):
    for dx in (dir[0], dir[0]-1):
        for dy in (dir[1], dir[1]-1):
            yield (x+dx, y+dy, (dir[1], dir[0]))

def isCornerConcave(regions, x1, y1, dir1, x2, y2, dir2):
    # Somewhat surprisingly, direction doesn't matter.
    x = max(x1, x2)
    y = max(y1, y2)
    # (x, y) is the square that is shared by the two edges
    # If that is a space, then the corner is concave.
    return (x, y) not in regions

def buildTranslationMap(M, cubeSize):
    regions = list(getRegions(M, cubeSize))

    translationMap = {}
    edges = set()
    for region in regions:
        for dir in directions:
            if (region[0] + dir[0], region[1] + dir[1]) in regions:
                translationMap[region, dir] = ((region[0] + dir[0], region[1] + dir[1]), dir)
            else:
                # Couldn't go in that direction. So, we're at an outside edge.
                edges.add(
                    (region[0] + min(0, dir[0]), region[1] + min(0, dir[1]), (abs(dir[0]), abs(dir[1]))))

    concaveCorners = set()
    for edge1 in edges:
        for edge2 in getPossibleCornerEdges(*edge1):
            if edge2 in edges:
                if isCornerConcave(regions, *edge1, *edge2):
                    concaveCorners.add(tuple(sorted([edge1, edge2], key=lambda x:x[2])))

    def isPartOfConcaveCorner(x, y, dir, concaveCorners=concaveCorners):
        for corner in concaveCorners:
            if (x, y, dir) in corner:
                return True
        return False

    def getRegionAndDirectionOfOuterEdge(x, y, dir, regions=regions):
        r = set([(x, y), (x+dir[0], y+dir[1])]).intersection(regions)
        assert len(r) == 1
        r = r.pop()
        if r == (x, y):
            d = dir
        else:
            d = (-dir[0], -dir[1])

        return r, d

    handledEdges = set([edge for corner in concaveCorners for edge in corner])
    for edge1, edge2 in concaveCorners:
        # They are ordered by direction, so the first one is the horizontal one.
        region1, dir1 = getRegionAndDirectionOfOuterEdge(*edge1)
        region2, dir2 = getRegionAndDirectionOfOuterEdge(*edge2)

        translationMap[region1, dir1] = (region2, dir2)
        translationMap[region2, dir2] = (region1, dir1)

    currentPairs = set(concaveCorners)
    while handledEdges != edges:
        nextPairs = set()
        for pair in currentPairs:
            p = set()
            for e in pair:
                nextEdge = set(getAllNeighborEdges(*e)).intersection(edges) - handledEdges
                if len(nextEdge) == 1:
                    p.add(nextEdge.pop())

            if len(p) == 2 and p.intersection(set([pp for ppp in nextPairs for pp in ppp])) == set():
                nextPairs.add(tuple(sorted(p)))

        for (edge1, edge2) in nextPairs:
            region1, dir1 = getRegionAndDirectionOfOuterEdge(*edge1)
            region2, dir2 = getRegionAndDirectionOfOuterEdge(*edge2)

            translationMap[region1, dir1] = (region2, dir2)
            translationMap[region2, dir2] = (region1, dir1)
            handledEdges.add(edge1)
            handledEdges.add(edge2)
        currentPairs = nextPairs

    return translationMap

def isWithinBounds(M, x, y):
    return (x >= 0 and y >= 0 and y < len(M) and x < len(M[y]))

def moveOnCube(M, x, y, dir, translationMap, cubeSize):
    print('Current map, about to move', dir)
    printMap(M, (x, y))
    import time
    time.sleep(0.5)
    maybePos = (x+dir[0], y+dir[1])

    # Simple case
    if isWithinBounds(M, *maybePos) and M[maybePos[1]][maybePos[0]] != ' ':
        if M[maybePos[1]][maybePos[0]] == '#':
            return (x, y), dir
        elif M[maybePos[1]][maybePos[0]] == '.':
            return maybePos, dir
        else:
            assert False

    fromRegion = getRegion(x, y, cubeSize)
    rx, ry = getRelativeCoordinates(x, y, fromRegion, cubeSize)
    newRegion, toDir = translationMap[fromRegion, dir]

    newDir = (-toDir[0], -toDir[1])
    if abs(newDir[0]) == abs(dir[1]) and abs(newDir[1]) == abs(dir[0]):
        # We're either going from horizontal to vertical or vice versa.
        newX, newY = ry, rx
        if dir[0]+dir[1]+newDir[0]+newDir[1] != 0:
            newX, newY = cubeSize-newX-1, cubeSize-newY-1
        else:
            print('Weird case', dir, newDir, newX, newY)
    else:
        newX, newY = rx, ry
        if newDir[0] == 0:
            newX = cubeSize-newX-1
        if newDir[1] == 0:
            newY = cubeSize-newY-1

    return getAbsoluteCoordinates(newX, newY, newRegion, cubeSize), newDir


def getRelativeCoordinates(x, y, region, cubeSize):
    return (getRelativeCoordinate(x, region[0], cubeSize),
            getRelativeCoordinate(y, region[1], cubeSize))

def getRelativeCoordinate(x, r, cubeSize):
    return x-r*cubeSize

def getAbsoluteCoordinates(x, y, region, cubeSize):
    return (x + region[0]*cubeSize, y + region[1]*cubeSize)

def partA(filename: str) -> int:
    data = getData(filename)
    M, curPos, instructions = parseData(data)

    printMap(M, curPos)
    print()

    for inst in instructions:
        curDir = inst[0]
        curPos = makeMove(M, curPos, inst)

    return (curPos[1]+1) * 1000 + (curPos[0]+1) * 4 + directions.index(curDir)

def makeMove(M, curPos, inst):
    for _ in range(inst[1]):
        newPos = curPos
        newPos = moveBounded(M, newPos, inst[0])
        while True:
            if ((newPos[1] >= len(M)) or
                (newPos[1] < 0) or
                (newPos[0] < 0) or
                (newPos[0] >= len(M[newPos[1]])) or
                (M[newPos[1]][newPos[0]] == ' ')):

                newPos = moveBounded(M, newPos, inst[0])
            else:
                break

        if M[newPos[1]][newPos[0]] == '.':
            curPos = newPos
        elif M[newPos[1]][newPos[0]] == '#':
            break
        else:
            assert False

    return curPos

def makeMoveOnCube(M, sides, curPos, inst, cubeSize):
    curDir = inst[0]
    for _ in range(inst[1]):
        curSide = (curPos[0] // cubeSize, curPos[1] // cubeSize)

        newPos = (curPos[0] + curDir[0], curPos[1] + curDir[1])
        newSide = (newPos[0] // cubeSize, newPos[1] // cubeSize)

        if newSide in sides:
            curPos = newPos
            continue

        if curDir == (1,0):
            maybe = (curSide[0] + 1, curSide[1]-1)
            if maybe in sides:
                newPos = getAbsoluteCoordinates(curPos[1] % cubeSize, cubeSize - 1, maybe, cubeSize)
                curPos = newPos
                curdir


    return curPos


def moveBounded(M, curPos, curDir):
    return ((curPos[0] + curDir[0]) % max([len(s) for s in M]), (curPos[1] + curDir[1]) % len(M))

def parseData(data):
    mapData, rawInstructions = data.split('\n\n')
    M = []
    for line in mapData.splitlines():
        M += [list(line)]

    for x in range(len(M[0])):
        if M[0][x] == '.':
            curPos = (x, 0)
            break

    curDir = directions[0]
    rawInstructions = rawInstructions.strip()

    b = ''
    instructions = []
    for c in rawInstructions:
        if c == 'R':
            if b != '':
                instructions += [(curDir, int(b))]
                b = ''
            curDir = directions[(directions.index(curDir) + 1) % len(directions)]
        elif c == 'L':
            if b != '':
                instructions += [(curDir, int(b))]
                b = ''
            curDir = directions[(directions.index(curDir) - 1) % len(directions)]
        elif c in '0123456789':
            b += c
        else:
            assert False

    instructions += [(curDir, int(b))]
    return M,curPos,instructions

def partB(filename: str, cubeSize=50) -> int:
    data = getData(filename)
    M, curPos, instructions = parseData(data)

    translationMap =  buildTranslationMap(M, cubeSize)

    for inst in instructions:
        curDir = inst[0]
        for _ in range(inst[1]):
            curPos, curDir = moveOnCube(M, curPos[0], curPos[1], curDir, translationMap, cubeSize)

    return (curPos[1]+1) * 1000 + (curPos[0]+1) * 4 + directions.index(curDir)


def getData(filename: str) -> list:
    with open(filename) as f:
        return f.read()

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
#    print(partA(os.path.dirname(__file__) + '/../data/input.txt'))
    print(partB(os.path.dirname(__file__) + '/../data/sample.txt', 4))
#    print(partB(os.path.dirname(__file__) + '/../data/input.txt'))