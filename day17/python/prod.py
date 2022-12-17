import zlib

shapes = (
['####'],
[' # ',
 '###',
 ' # '],
['  #',
 '  #',
 '###'],
['#', '#', '#', '#'],
['##', '##'])

tube_width = 7

def wouldOverlap(silo, shape, x, y):
    if x + max(len(s) for s in shape) > tube_width:
        return True

    for i, s in enumerate(shape):
        if len(silo) <= y-i:
            continue

        if y-i < 0:
            return True

        l = silo[y-i]
        for j, c in enumerate(s):
            if c != ' ' and l[x+j] != ' ':
                return True
    return False

# Assumes everything has already been checked
def addShapeToSilo(silo, shape, x, y):
    for _ in range(len(silo), y+1):
        silo.append(' ' * tube_width)

    for i, s in enumerate(shape):
        for j, c in enumerate(s):
            if c == '#':
                silo[y-i] = silo[y-i][:j+x] + c + silo[y-i][j+x+1:]

    return silo

def printSilo(silo):
    print('Silo:')
    print()
    for l in silo[::-1]:
        print('|%s|' % (l,))
    print('=========')

def partA(filename: str, total_shapes=2022) -> int:
    return len(doTheStuff(filename, total_shapes)[0])

def doTheStuff(filename: str, total_shapes=2022, levels=None) -> int:
    lines = getLines(filename)

    moves = lines[0]
    tube_width = 7
    seen_crcs = dict()

    prev = 0
    # This will represent the silo
    if levels is None:
        levels = []

    i = 0
    j = 0
    previ = 0

    from collections import defaultdict
    while i < total_shapes:
        shape = shapes[i % len(shapes)]
        # x,y is the top left of the shape (both 0-indexed)
        x = 2
        y = len(levels) + 3 + len(shape) - 1

        while True:
            if len(levels) > 20:
                crc = zlib.crc32(bytes(str(i % len(shapes)) + str(j % len(moves)) + ''.join(lines[-5:]), 'ascii'))

                if crc in seen_crcs:
                    seen_crcs[crc] += [i]
                else:
                    seen_crcs[crc] = [i]

            action = moves[j % len(moves)]
            j += 1

            if action == '<':
                new_x = max(x-1, 0)
            elif action == '>':
                new_x = min(x+1, tube_width-1)

            if not wouldOverlap(levels, shape, new_x, y):
                x = new_x

            if not wouldOverlap(levels, shape, x, y-1):
                y -= 1
            else:
                levels = addShapeToSilo(levels, shape, x, y)
                break

        i += 1
    return levels, seen_crcs

def partB(filename: str) -> int:
    lines = getLines(filename)
    levels, seen_crcs = doTheStuff(filename, total_shapes=10000)
    most = 0
    winner = None

    period = None
    for k in seen_crcs:
        if len(seen_crcs[k]) > most:
            most = len(seen_crcs[k])
            winner = seen_crcs[k]

    for x in range(1, 5):
        found = True
        prev = None
        prev_diff = None
        for w in winner[1::x]:
            if prev is None:
                prev = w
                continue

            diff = w - prev
            if prev_diff is not None:
                if diff != prev_diff:
                    found = False
                    print('nope')
                    break
            prev_diff = diff
            prev = w
        if found:
            period = diff
            print('found period:', diff)
            break

    assert period is not None

    base = partA(filename, 10000)
    next = partA(filename, 10000+period)
    assert partA(filename, 10000+period*2) == next + (next - base)

    desired_pieces = 1_000_000_000_000
    # That is approx this many periods:
    periods = (desired_pieces // period)-10

    # So we first get the result for some base number whose
    # difference to desired_pieces is a multiple of the period
    base = partA(filename, desired_pieces - period*periods)
    # Then we figure out how much higher it when we move one period forward:
    next = partA(filename, desired_pieces - period*(periods-1))
    return base+(next-base)*periods

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
    print(partB(os.path.dirname(__file__) + '/../data/sample.txt'))
    print(partB(os.path.dirname(__file__) + '/../data/input.txt'))