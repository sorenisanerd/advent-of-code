from functools import cache
from collections import defaultdict
from queue import PriorityQueue

def partA(filename: str) -> int:
    lines = getLines(filename)
    width, height, bad, start, goal = parseMap(lines)
    return aStar(timedCoordinate(start, 0), goal, bad, width, height)

def timedCoordinate(pos, t):
    return (pos[0], pos[1], t)

def aStar(start, goal, bad, width, height):
    def h(pos, goal=goal):
        x, y, t = pos
        return abs(x - goal[0]) + abs(y - goal[1])

    openSet = PriorityQueue()
    openSet.put((h(start), start))
    cameFrom = dict()

    gScore = defaultdict(lambda: float('inf'))
    gScore[start] = 0

    fScore = defaultdict(lambda: float('inf'))
    fScore[start] = h(start, goal)

    startAndGoal = set([(start[0], start[1]), (goal[0], goal[1])])
    while not openSet.empty():
        current = openSet.get(block=False)[1]

        if (current[0], current[1]) == goal:
            return gScore[current]

        for (dx, dy) in [(1,0), (-1,0), (0,1), (0,-1), (0,0)]:
            neighbor = (current[0]+dx, current[1]+dy, current[2]+1)

            if neighbor[0] < 1 or neighbor[0] >= width-1 and (neighbor[0], neighbor[1]) not in startAndGoal:
                continue
            if (neighbor[1] < 1 or neighbor[1] >= height-1) and (neighbor[0], neighbor[1]) not in startAndGoal:
                continue

            if neighbor in bad:
                continue

            tentative_gScore = gScore[current] + 1
            if tentative_gScore < gScore[neighbor]:
                cameFrom[neighbor] = current
                gScore[neighbor] = tentative_gScore
                fScore[neighbor] = tentative_gScore + h(neighbor, goal)
                openSet.put((fScore[neighbor], neighbor))


def wrapAround(width, height, x, y, dx, dy):
    return (x-1+dx) % (width-2) + 1, (y-1+dy) % (height-2) + 1

def step(width, height, ups, rights, lefts, downs):
    return (set([wrapAround(width, height, *a, 0, -1) for a in ups]),
            set([wrapAround(width, height, *a, 1, 0) for a in rights]),
            set([wrapAround(width, height, *a, -1, 0) for a in lefts]),
            set([wrapAround(width, height, *a, 0, 1) for a in downs]))


def printMap(width, height, ups, rights, lefts, downs, additional_points=None):
    print('#' + (additional_points and additional_points.get((1,0), ' ') or ' ') + '#' * (width - 2))
    for y in range(1, height-1):
        print('#', end='')
        for x in range(1, width-1):
            if additional_points and (x, y) in additional_points:
                print(additional_points[(x, y)], end='')
            elif (x, y) in ups:
                print('^', end='')
            elif (x, y) in rights:
                print('>', end='')
            elif (x, y) in lefts:
                print('<', end='')
            elif (x, y) in downs:
                print('v', end='')
            else:
                print('.', end='')
        print('#')
    print('#' * (width - 2) + ' #')

def partB(filename: str) -> int:
    lines = getLines(filename)
    width, height, bad, start, goal = parseMap(lines)

    there = aStar(timedCoordinate(start, 0), goal, bad, width, height)
    back = aStar(timedCoordinate(goal, there), start, bad, width, height)
    thereAgain = aStar(timedCoordinate(start, there+back), goal, bad, width, height)
    return there + back + thereAgain

def parseMap(lines):
    M = []

    ups = set()
    rights = set()
    lefts = set()
    downs = set()

    # Subtracting the walls
    width = len(lines[0])
    height = len(lines)

    for y, l in enumerate(lines):
        for x, c in enumerate(l):
            if c == '^':
                ups.add((x, y))
            elif c == '>':
                rights.add((x, y))
            elif c == '<':
                lefts.add((x, y))
            elif c == 'v':
                downs.add((x, y))

#    printMap(width, height, ups, rights, lefts, downs)

    bad = set()
    for i in range(1, 2500):
        ups, rights, lefts, downs = step(width, height, ups, rights, lefts, downs)
        bad |= set([(x, y, i) for (x, y) in ups | rights | lefts | downs])

    bad = frozenset(bad)

    start = (lines[0].index('.'), 0)
    goal = (lines[-1].index('.'), len(lines)-1)

    return width, height, bad, start, goal

def getLines(filename: str) -> list:
    lines = []
    with open(filename) as f:
        for l in f:
            l = l.rstrip('\n')
            lines += [l]
    return lines

if __name__ == '__main__':
    import os.path
    print(partA(get_data_file_path('input.txt')))
    print(partB(get_data_file_path('input.txt')))
