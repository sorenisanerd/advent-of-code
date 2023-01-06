from aoc.utils import *

def isMoveValid(M:Map, f, t):
    f = M[f].replace('S', 'a').replace('E', 'z')
    t = M[t].replace('S', 'a').replace('E', 'z')
    if ord(t) <= ord(f)+1:
        return True
    return False

def partA(filename: str) -> int:
    M = Map(getLines(filename))

    generateNeighbors = getGenerateNeighbors(M)

    start = M.find('S')
    end = M.find('E')
    return dijkstra([start], end, generateNeighbors=generateNeighbors)

def getGenerateNeighbors(M):
    def generateNeighbors(p):
        for d in map(V, four_directions):
            p_ = p + d
            if M.boundsCheck(p_):
                if isMoveValid(M, p, p_):
                    yield (1, p_)
    return generateNeighbors

def partB(filename: str) -> int:
    M = Map(getLines(filename))

    generateNeighbors = getGenerateNeighbors(M)
    end = M.find('E')
    starts = set(M.findAll('a')) | set(M.findAll('S'))
    return dijkstra(starts, end, generateNeighbors=generateNeighbors)