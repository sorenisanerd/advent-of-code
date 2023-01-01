directions = dict()
directions['N'] = (0, -1)
directions['NE'] = (1, -1)
directions['E'] = (1, 0)
directions['SE'] = (1, 1)
directions['S'] = (0, 1)
directions['SW'] = (-1, 1)
directions['W'] = (-1, 0)
directions['NW'] = (-1, -1)

all_directions = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']

def partA(filename: str, rounds=10) -> int:
    lines = getLines(filename)

    elves = set()
    for y, l in enumerate(lines):
        for x, c in enumerate(l):
            if c == '#':
                elves.add((x,y))

    preferences = [('N', 'NE', 'NW'), ('S', 'SE', 'SW'), ('W', 'NW', 'SW'), ('E', 'NE', 'SE')]

    round = 0
    while round < rounds:
        elves, preferences = doRound(elves, preferences)
        round += 1

    minx = min([e[0] for e in elves])
    miny = min([e[1] for e in elves])
    maxx = max([e[0] for e in elves])
    maxy = max([e[1] for e in elves])

    return (maxx - minx + 1) * (maxy - miny + 1) - len(elves)

def doRound(elves, preferences):
    moves = set()
    elves = set(elves)
    for elf in elves:
        if not set(getNeighbors(elf, all_directions)) & elves:
            continue

        for pref in preferences:
            overlap = set(getNeighbors(elf, pref)) & elves
            if not overlap:
                moves.add((elf, getNeighbor(elf, pref[0])))
                break

    all_destinations = set()
    invalid_destinations = set()
    for elf, dest in moves:
            # If we see the same destination more than
            # once, no one gets to move there.
        if dest in all_destinations:
            invalid_destinations.add(dest)
            continue
        all_destinations.add(dest)

    for move in moves:
        if move[1] in invalid_destinations:
            continue
        elves.remove(move[0])
        elves.add(move[1])

    return elves, (preferences[1:] + [preferences[0]])

def printMap(elves, border=3):
    minx = min([e[0] for e in elves])
    miny = min([e[1] for e in elves])
    maxx = max([e[0] for e in elves])
    maxy = max([e[1] for e in elves])

    for y in range(miny-border, maxy + 1 + border):
        for x in range(minx-border, maxx + 1 + border):
            if (x, y) in elves:
                print('#', end='')
            else:
                print('.', end='')
        print()

def getNeighbors(elf, dirs):
    for d in dirs:
        yield getNeighbor(elf, d)

def getNeighbor(elf, dir):
    return (elf[0] + directions[dir][0], elf[1] + directions[dir][1])

def partB(filename: str, rounds=10) -> int:
    lines = getLines(filename)

    elves = set()
    for y, l in enumerate(lines):
        for x, c in enumerate(l):
            if c == '#':
                elves.add((x,y))

    preferences = [('N', 'NE', 'NW'), ('S', 'SE', 'SW'), ('W', 'NW', 'SW'), ('E', 'NE', 'SE')]

    round = 0
    while True:
        round += 1
        newelves, preferences = doRound(elves, preferences)
        if elves == newelves:
            return round
        elves = newelves


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