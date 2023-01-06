from aoc.utils import *

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
                curDirIdx += 1
            elif inst == 'L':
                curDirIdx -= 1
            curDirIdx %= len(directions)

    return getScore(curPos, curDirIdx)

def getScore(curPos, curDirIdx):
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
    width = max([len(l) for l in M])
    for i in range(len(M)):
        M[i] += [' '] * (width - len(M[i]))

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
                instructions += [int(buf)]
                buf = ''
            instructions += [c]
        elif c in '0123456789':
            buf += c
        else:
            assert False

    if buf != '':
        instructions += [int(buf)]

    return M, curPos, instructions

def makeMove(M, curPos, curDir):
    # If we get into no-man's-land, wrap around
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
                newPos, newDir = moveOnCube(M, *curPos, curDir, translationMap, cubeSize, regions)

                if M[newPos[1]][newPos[0]] == '#':
                    break

                assert M[newPos[1]][newPos[0]] == '.'

                # All clear
                curDir, curPos = newDir, newPos
        else:
            if inst == 'R':
                curDir = directions[(directions.index(curDir) + 1) % len(directions)]
            elif inst == 'L':
                curDir = directions[(directions.index(curDir) - 1) % len(directions)]
            else:
                assert False

    return getScore(curPos, directions.index(curDir))

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
    # Return all edges that this edge could form a corner with
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
    # Don't believe me? Neither did I, but see the test (in test.py)
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
                    concaveCorners.add(frozenset([edge1, edge2]))

    # This translates from the (X, Y, (1, 0)) / (X, Y, (0, 1))
    # notation back to region/dir
    def getRegionAndDirectionOfOuterEdge(x, y, dir, regions=regions):
        r = set([(x, y), (x+dir[0], y+dir[1])]).intersection(regions)
        assert len(r) == 1
        r = r.pop()
        if r == (x, y):
            d = dir
        else:
            d = (-dir[0], -dir[1])

        return r, d

    currentPairs = set()
    for edge1, edge2 in concaveCorners:
        region1, dir1 = getRegionAndDirectionOfOuterEdge(*edge1)
        region2, dir2 = getRegionAndDirectionOfOuterEdge(*edge2)
        translationMap[region1, dir1] = (region2, dir2)
        translationMap[region2, dir2] = (region1, dir1)
        currentPairs.add(frozenset([edge1, edge2]))

    handledEdges = set([edge for corner in concaveCorners for edge in corner])

    # The next chunk of code is genuinely upsetting to me.
    # If you have a clearer way to do it, please let me know.
    # We're trying see if any of the concave corners are
    # adjacent to another concave corner. If so, we "join" them
    # for the part of the algorightm where we move away from
    # corners to populate the translation map.

    # For each corner...
    for corner in concaveCorners:
        breakk = False
        # ...we look at each of its edges...
        for edge in corner:
            # ...remember the other edge of the corner...
            otherEdge = corner - set([edge])

            # ...and look for additional neighboring edges...
            isect = (set(getPossibleCornerEdges(*edge)) - otherEdge) & handledEdges

            assert len(isect) < 2

            # ...if we do find one...
            if len(isect) == 1:
                neighbor = isect.pop()

                # ...we find the corner it belong to...
                neighborCorner, = set(filter(lambda c: neighbor in c, concaveCorners))

                # ...and determine the other edge of that corner...
                neighborsNeighbor, = (neighborCorner - set([neighbor]))

                # ...and we finally remove both corners...
                currentPairs.remove(corner)
                currentPairs.remove(neighborCorner)

                # ...turn the set into its only element..
                otherEdge, = otherEdge

                # ...and add a new pair with the two far edges.
                currentPairs.add(frozenset([otherEdge, neighborsNeighbor]))
                breakk = True
                break
        if breakk:
            break

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
                    nextPairs.add(frozenset(p))
                else:
                    # If an edge would be in more than one pair, get rid of both pairs
                    nextPairs = set(filter(lambda x: set(x).intersection(p) == set(), nextPairs))

        if nextPairs == set():
            assert len(edges - handledEdges) == 2
            nextPairs.add(frozenset(edges - handledEdges))

        for (edge1, edge2) in nextPairs:
            region1, dir1 = getRegionAndDirectionOfOuterEdge(*edge1)
            region2, dir2 = getRegionAndDirectionOfOuterEdge(*edge2)

            translationMap[region1, dir1] = (region2, dir2)
            translationMap[region2, dir2] = (region1, dir1)
            handledEdges.add(edge1)
            handledEdges.add(edge2)
        currentPairs = nextPairs

    return translationMap, regions

def moveOnCube(M, x, y, dir, translationMap, cubeSize, regions):
    maybePos = (x+dir[0], y+dir[1])

    if getRegionByCoordinates(*maybePos, cubeSize) in regions:
        return maybePos, dir

    fromRegion = getRegionByCoordinates(x, y, cubeSize)
    newRegion, toDir = translationMap[fromRegion, dir]

    newDir = (-toDir[0], -toDir[1])

    curDirIdx = directions.index(dir)
    newDirIdx = directions.index(newDir)

    newX, newY = getRelativeCoordinates(*maybePos, fromRegion, cubeSize)

    i = 0
    while (curDirIdx+i) % 4 != newDirIdx:
        newY, newX = newX, cubeSize-newY-1
        i += 1

    newCoords = getAbsoluteCoordinates(newX, newY, newRegion, cubeSize)
    return newCoords, newDir

def getRelativeCoordinates(x, y, region, cubeSize):
    return (getRelativeCoordinate(x, region[0], cubeSize),
            getRelativeCoordinate(y, region[1], cubeSize))

def getRelativeCoordinate(x_or_y, region, cubeSize):
    return x_or_y-region*cubeSize

def getAbsoluteCoordinates(x, y, region, cubeSize):
    return ((x % cubeSize) + region[0]*cubeSize, (y % cubeSize) + region[1]*cubeSize)

if __name__ == '__main__':
    import os.path
    print(partA(get_data_file_path('sample.txt')))
    print(partA(get_data_file_path('input.txt')))
    print(partB(get_data_file_path('sample.txt'), 4))
    print(partB(get_data_file_path('input.txt')))