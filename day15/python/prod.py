import re
def partA(filename: str, target_row=20) -> int:
    lines = getLines(filename)
    pattern = re.compile('Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)')
    pairs = []
    for l in lines:
        sx, sy, bx, by = list(map(int, pattern.match(l).groups()))
        pairs += [(sx, sy, bx, by)]

    cols = set()
    for pair in pairs:
        sx, sy, bx, by = pair
        distance = abs(sx - bx) + abs(sy - by)
        radius = distance - abs(target_row - sy)
        for x in range(sx-radius, sx+radius):
            cols.add(x)

    return len(cols)

def partB(filename: str, minx, miny, maxx, maxy) -> int:
    lines = getLines(filename)
    pattern = re.compile('Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)')
    pairs = []
    for l in lines:
        sx, sy, bx, by = list(map(int, pattern.match(l).groups()))
        pairs += [(sx, sy, bx, by)]

    def within_same_distance(sx, sy, bx, by, cx, cy):
        return abs(sx - bx) + abs(sy - by) >= abs(sx - cx) + abs(sy - cy)

    def isCovered(x, y):
        for pair in pairs:
            sx, sy, bx, by = pair
            if within_same_distance(sx, sy, bx, by, x, y):
                return True
        return False

    for target_row in range(miny, maxy+1):
        spans = []
        for pair in pairs:
            sx, sy, bx, by = pair
            distance = abs(sx - bx) + abs(sy - by)
            radius = distance - abs(target_row - sy)
            if radius < 0:
                continue
            spans += [(max(minx, sx-radius), min(maxx, sx+radius))]

        start_ordered_taken_spans = sorted(spans, key=lambda x:x[0])
        x = minx
        for (x1, x2) in start_ordered_taken_spans:
            if x < x1:
                return target_row+x*4000000
            x = max(x, x2+1)
        if x <= maxx:
            return target_row+x*4000000

    return 0

    for x in range(minx, maxx+1):
        for y in range(miny, maxy+1):
            if x == 14 and y == 11:
                print('here')
            if isCovered(x, y):
                continue
            return x*4000000+y

    return 0

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
#    print(partA(os.path.dirname(__file__) + '/../data/input.txt', 2000000))
    print(partB(os.path.dirname(__file__) + '/../data/sample.txt', 0, 0, 20, 20))
    print(partB(os.path.dirname(__file__) + '/../data/input.txt', 0, 0, 4000000, 4000000))