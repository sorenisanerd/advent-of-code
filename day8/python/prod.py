def partA(filename: str) -> int:
    lines = getLines(filename)

    visible = set()
    counter = 0
    for x in range(len(lines[0])):
        z = -1
        for y in range(len(lines)):
            val = int(lines[y][x])
            if val > z:
                visible.add((x, y))
                z = val

        z = -1
        for y in range(len(lines)-1, -1, -1):
            val = int(lines[y][x])
            if val > z:
                visible.add((x, y))
                z = val

    for y in range(len(lines)-1, -1, -1):
        z = -1
        for x in range(len(lines[0])):
            val = int(lines[y][x])
            if val > z:
                visible.add((x, y))
                z = val

        z = -1
        for x in range(len(lines[0])-1, -1, -1):
            val = int(lines[y][x])
            if val > z:
                visible.add((x, y))
                z = int(lines[y][x])


    return len(visible)

def partB(filename: str) -> int:
    lines = getLines(filename)

    def consider(lines, start_x, start_y):
        start_value = int(lines[start_y][start_x])
        rv = 1

        # left
        counter = 0
        for x in range(start_x-1, -1, -1):
            counter += 1
            if int(lines[start_y][x]) >= start_value:
                break
        rv *= counter

        # right
        counter = 0
        for x in range(start_x+1, len(lines[0])):
            counter += 1
            if int(lines[start_y][x]) >= start_value:
                break
        rv *= counter

        # up
        counter = 0
        for y in range(start_y-1, -1, -1):
            counter += 1
            if int(lines[y][start_x]) >= start_value:
                break
        rv *= counter

        # down
        counter = 0
        for y in range(start_y+1, len(lines)):
            counter += 1
            if int(lines[y][start_x]) >= start_value:
                break
        rv *= counter
        return rv

    rv = 0
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            rv = max(rv, consider(lines, x, y))

    return rv

def getLines(filename: str) -> list:
    lines = []
    with open(filename) as f:
        for l in f:
            l = l.rstrip('\n')
            lines += [l]
    return lines

if __name__ == '__main__':
    import os.path
    print(partA(os.path.dirname(__file__) + '/../data/input.txt'))
    print(partB(os.path.dirname(__file__) + '/../data/input.txt'))