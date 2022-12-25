# Right, down, left, up
directions = [(1,0), (0,1), (-1,0), (0,-1)]

def partA(filename: str) -> int:
    data = getData(filename)
    M, curPos, instructions = parseData(data)

    curDirIdx = 0
    for inst in instructions:
        if type(inst) == int:
            for _ in range(inst):
                newPos = makeMove(M, curPos, directions[curDirIdx])
                if M[newPos[1]][newPos[0]] == '#':
                    break
                elif M[newPos[1]][newPos[0]] == '.':
                    curPos = newPos
                else:
                    assert False
        else:
            if inst == 'R':
                curDirIdx = (curDirIdx + 1) % len(directions)
            elif inst == 'L':
                curDirIdx = (curDirIdx - 1) % len(directions)

    return (curPos[1]+1) * 1000 + (curPos[0]+1) * 4 + curDirIdx

def getData(filename: str) -> str:
    with open(filename) as f:
        return f.read()

def parseData(data):
    mapData, rawInstructions = data.split('\n\n')

    M = []
    for line in mapData.splitlines():
        M += [list(line)]

    # Make sure all lines are the same length
    maxx = max([len(l) for l in M])
    for i in range(len(M)):
        M[i] += [' '] * (maxx - len(M[i]))

    for x in range(len(M[0])):
        if M[0][x] == '.':
            curPos = (x, 0)
            break

    rawInstructions = rawInstructions.strip()

    buf = ''
    instructions = []
    for c in rawInstructions:
        if c in 'RL':
            if buf != '':
                instructions += [int(buf), c]
                buf = ''
        elif c in '0123456789':
            buf += c
        else:
            assert False

    if buf != '':
        instructions += [int(buf)]

    return M, curPos, instructions

def makeMove(M, curPos, curDir):
    while True:
        newPos = ((curPos[0] + curDir[0]) % (len(M[0])),
                  (curPos[1] + curDir[1]) % len(M))

        if M[newPos[1]][newPos[0]] != ' ':
            break

        curPos = newPos

    return newPos


def partB(filename: str, cubeSize=50) -> int:
    data = getData(filename)
    M, curPos, instructions = parseData(data)

    translationMap, regions =  buildTranslationMap(M, cubeSize)

    curDir = directions[0]
    for inst in instructions:
        if type(inst) == int:
            for _ in range(inst):
                newPos, newDir, _ = moveOnCube(M, *curPos, curDir, translationMap, cubeSize, regions)
                if M[newPos[1]][newPos[0]] == '#':
                    break
                assert M[newPos[1]][newPos[0]] == '.'
                curDir, curPos = newDir, newPos
        else:
            if inst == 'R':
                curDir = directions[(directions.index(curDir) + 1) % len(directions)]
            elif inst == 'L':
                curDir = directions[(directions.index(curDir) - 1) % len(directions)]
            else:
                assert False

    return (curPos[1]+1) * 1000 + (curPos[0]+1) * 4 + directions.index(curDir)





def printMap(M, curPos):
    for y, l in enumerate(M):
        print(''.join([(x,y) == curPos and 'X' or c for x, c in enumerate(l)]))

def getRegionByCoordinates(x, y, cubeSize):
    return (x//cubeSize, y//cubeSize)

def getAllRegions(M, cubeSize):
    for y in range(0, len(M), cubeSize):
        for x in range(0, len(M[y]), cubeSize):
            if M[y][x] != ' ':
                yield (x//cubeSize, y//cubeSize)

def getNeighborDirections(dir):
    # ( 1, 0) -> ( 1, 1), ( 1,-1)
    # ( 0, 1) -> ( 1, 1), (-1, 1)
    # (-1, 0) -> (-1, 1), (-1,-1)
    # ( 0,-1) -> ( 1,-1), (-1,-1)
    return ((dir[0] + dir[1]*dir[1], dir[1] + dir[0]*dir[0]),
            (dir[0] - dir[1]*dir[1], dir[1] - dir[0]*dir[0]))

def getPossibleCornerEdges(x, y, dir):
    # for horizontal edges, yield all the adjacent vertical
    # ones, and vice versa
    for dx in (dir[0], dir[0]-1):
        for dy in (dir[1], dir[1]-1):
            yield (x+dx, y+dy, (dir[1], dir[0]))

def getAllNeighborEdges(x, y, dir):
    # All the possible corner edges, plus the similarly oriented
    # edges in either direction.
    for edge in getPossibleCornerEdges(x, y, dir):
        yield edge
    yield x+dir[1], y+dir[0], dir
    yield x-dir[1], y-dir[0], dir

def isCornerConcave(regions, x1, y1, dir1, x2, y2, dir2):
    # Somewhat surprisingly, direction doesn't matter.
    x = max(x1, x2)
    y = max(y1, y2)
    # (x, y) is the square that is shared by the two edges
    # If that is a space, then the corner is concave.
    return (x, y) not in regions

def buildTranslationMap(M, cubeSize):
    regions = list(getAllRegions(M, cubeSize))

    translationMap = {}

    edges = set()
    for region in regions:
        for dir in directions:
            if (region[0] + dir[0], region[1] + dir[1]) not in regions:
                # Couldn't go in that direction. This means we've found an outer edge.
                # Edges are stored as (x, y, dir), where dir is either (1,0) or (0,1).
                # So, e.g. (2,3)'s upper edge is (2, 2, (0, 1)).
                edges.add((region[0] + min(0, dir[0]),
                           region[1] + min(0, dir[1]),
                          (abs(dir[0]), abs(dir[1]))))

    concaveCorners = set()
    for edge1 in edges:
        for edge2 in getPossibleCornerEdges(*edge1):
            if edge2 in edges:
                if isCornerConcave(regions, *edge1, *edge2):
                    concaveCorners.add(tuple(sorted([edge1, edge2], key=lambda x:x[2])))

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

            if len(p) == 2:
                if p.intersection(set([pp for ppp in nextPairs for pp in ppp])) == set():
                    nextPairs.add(tuple(sorted(p)))
                else:
                    # If an edge would be in more than one pair, get rid of both pairs
                    nextPairs = set(filter(lambda x: set(x).intersection(p) == set(), nextPairs))

        if nextPairs == set():
            assert len(edges - handledEdges) == 2
            nextPairs.add(tuple(edges - handledEdges))

        for (edge1, edge2) in nextPairs:
            region1, dir1 = getRegionAndDirectionOfOuterEdge(*edge1)
            region2, dir2 = getRegionAndDirectionOfOuterEdge(*edge2)

            translationMap[region1, dir1] = (region2, dir2)
            translationMap[region2, dir2] = (region1, dir1)
            handledEdges.add(edge1)
            handledEdges.add(edge2)
        currentPairs = nextPairs

    return translationMap, regions

def isWithinBounds(M, x, y):
    return (x >= 0 and y >= 0 and y < len(M) and x < len(M[y]))

def moveOnCube(M, x, y, dir, translationMap, cubeSize, regions):
    maybePos = (x+dir[0], y+dir[1])

    if isWithinBounds(M, *maybePos) and getRegionByCoordinates(*maybePos, cubeSize) in regions:
        return maybePos, dir, False

    fromRegion = getRegionByCoordinates(x, y, cubeSize)
    rx, ry = getRelativeCoordinates(x, y, fromRegion, cubeSize)
    newRegion, toDir = translationMap[fromRegion, dir]

    newDir = (-toDir[0], -toDir[1])
    if abs(newDir[0]) == abs(dir[1]) and abs(newDir[1]) == abs(dir[0]):
        # We're either going from horizontal to vertical or vice versa.
        newX, newY = ry, rx
        if dir[0]+dir[1]+newDir[0]+newDir[1] != 0:
            newX, newY = cubeSize-newX-1, cubeSize-newY-1
    elif newDir == dir:
        newX, newY = rx, ry
        if newDir[1] == 0:
            newX = cubeSize-newX-1
        if newDir[0] == 0:
            newY = cubeSize-newY-1
    else:
        newX, newY = rx, ry
        if newDir[0] == 0:
            newX = cubeSize-newX-1
        if newDir[1] == 0:
            newY = cubeSize-newY-1

    newCoords = getAbsoluteCoordinates(newX, newY, newRegion, cubeSize)
    return newCoords, newDir, False

def getRelativeCoordinates(x, y, region, cubeSize):
    return (getRelativeCoordinate(x, region[0], cubeSize),
            getRelativeCoordinate(y, region[1], cubeSize))

def getRelativeCoordinate(x, r, cubeSize):
    return x-r*cubeSize

def getAbsoluteCoordinates(x, y, region, cubeSize):
    return (x + region[0]*cubeSize, y + region[1]*cubeSize)

def moveBounded(M, curPos, curDir):
    return ((curPos[0] + curDir[0]) % max([len(s) for s in M]), (curPos[1] + curDir[1]) % len(M))


if __name__ == '__main__':
    import os.path
    print(partA(os.path.dirname(__file__) + '/../data/sample.txt'))
    print(partA(os.path.dirname(__file__) + '/../data/input.txt'))
    print(partB(os.path.dirname(__file__) + '/../data/sample.txt', 4))
    print(partB(os.path.dirname(__file__) + '/../data/input.txt'))