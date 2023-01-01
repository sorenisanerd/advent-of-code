import zlib
from collections import defaultdict

shapes = [

   ['####'],

   [' # ',
    '###',
    ' # '],

   ['  #',
    '  #',
    '###'],

   ['#',
    '#',
    '#',
    '#'],

  ['##',
   '##']
]

siloWidth = 7

def partA(filename: str, total_shapes=2022) -> int:
    return len(doTheStuff(filename, total_shapes)[0])

def doTheStuff(filename: str, total_shapes=2022, silo=None) -> int:
    lines = getLines(filename)

    # The moves are just one lo(ooooooooooooo)ng line
    moves = lines[0]

    if silo is None:
        silo = []

    # Bookkeeping
    i = 0 # For the shapes
    j = 0 # For the moves

    # For part 2
    seen = dict()
    possible_period = None

    while i < total_shapes:
        # Loop through the shapes in order
        shape = shapes[i % len(shapes)]

        # See if we find a pattern
        if possible_period is None and len(silo) > 200:
            # Increase this until we reliably find the period
            number_of_matching_lines = 35
            key = (i % len(shapes), j % len(moves), ''.join(lines[-number_of_matching_lines:]))

            if key in seen:
                period = i-seen[key]
                possible_period = (period, seen[key])

            seen[key] = i

        # Per instructions:
        #   Each rock appears so that its left edge is two units away
        #   from the left wall and its bottom edge is three units above
        #   the highest rock in the room (or the floor, if there isn't one).
        x = 2
        y = len(silo) + 3 + len(shape) - 1

        while True:
            action = moves[j % len(moves)]
            j += 1

            if action == '<':
                new_x = max(x-1, 0)
            elif action == '>':
                new_x = min(x+1, siloWidth-1)

            # If the move wouldn't cause overlap, move the piece
            # otherwise do nothing
            if not wouldOverlap(silo, shape, new_x, y):
                x = new_x

            # Move down
            if not wouldOverlap(silo, shape, x, y-1):
                y -= 1
            else:
                # If we can't move down, add the shape to the silo
                # and start over
                silo = addShapeToSilo(silo, shape, x, y)
                break
        i += 1

    return silo, possible_period

def wouldOverlap(silo, shape, x, y):
    # If we'd stick out on the right which is just as bad
    if x + max(len(s) for s in shape) > siloWidth:
        return True

    # Go through each line of the shape
    for i, s in enumerate(shape):
        # We don't extend the silo until we
        # finally add the shape to it, so
        # if the line is above the highest
        # known line, it's bound to be clear
        if len(silo) <= y-i:
            continue

        # We've reached the bottom
        if y-i < 0:
            return True

        # Finally, grab the line and...
        l = silo[y-i]

        # go through each character of the incoming
        # shape and see if the #'s target position
        # is already taken
        for j, c in enumerate(s):
            if c != ' ' and l[x+j] != ' ':
                return True
    return False

# Assumes everything has already been checked
def addShapeToSilo(silo, shape, x, y):
    # Ensure we have the space up top
    for _ in range(len(silo), y+1):
        silo.append([' '] * siloWidth)

    for i, s in enumerate(shape):
        for j, c in enumerate(s):
            if c == '#':
                silo[y-i][j+x] = c

    return silo

def printSilo(silo):
    print('Silo:')
    print()
    for l in silo[::-1]:
        print('|%s|' % (l,))
    print('=========')


def partB(filename: str) -> int:
    lines = getLines(filename)

    # 10000 rounds should be enough to find a period, right? *fingers crossed*
    _, possible_period = doTheStuff(filename, total_shapes=10000)

    # verify that the period is correct
    period, base = possible_period
    a = partA(filename, base)
    b = partA(filename, base+period)
    c = partA(filename, base+period*2)
    assert c-b == b-a

    # Ok, soooo....
    def cheatingPartA(desired_pieces=1_000_000_000_000, base=base, period=period):
        periods = (desired_pieces - base) // period
        new_base = desired_pieces - (periods*period)

        # Repitition starts at base, so make sure we're past that
        assert new_base > base

        base = new_base
        a = partA(filename, base)
        b = partA(filename, base+period)

        # So, say, after 10 periods, we should get:
        assert a+(b-a)*10 == partA(filename, base+10*period)

        return a+(b-a)*periods


    return cheatingPartA()

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
