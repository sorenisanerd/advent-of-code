def partA(filename: str) -> int:
    lines = getLines(filename)
    return partB(filename, n=2)

def partB(filename: str, n=10) -> int:
    lines = getLines(filename)

    visited = set()
    knots = [(0,0)]*n
    def move(hx, hy, move_dir):
        dx, dy = {'U': (0,1),
                    'D': (0,-1),
                    'R': (1,0),
                    'L': (-1,0)}[move_dir]
        hx, hy = hx+dx, hy+dy
        return hx, hy

    def track(hx, hy, tx, ty):
        if abs(hx-tx) == 2 and (hy == ty):
            tx += (hx-tx)//2
        elif abs(hy-ty) == 2 and (hx == tx):
            ty += (hy-ty)//2
        elif abs(hy-ty)>1 or abs(hx-tx)>1:
            tx += (hx-tx)//abs(hx-tx)
            ty += (hy-ty)//abs(hy-ty)
        return tx, ty

    for l in lines:
        direction, length = l.split(' ')
        length = int(length)
        for _ in range(length):
            knots[0] = move(knots[0][0], knots[0][1], direction)
            for i in range(len(knots)-1):
                knots[i+1] = track(knots[i][0], knots[i][1], knots[i+1][0], knots[i+1][1])

            visited.add((knots[-1][0], knots[-1][1]))

    return len(visited)

def getLines(filename: str) -> list:
    lines = []
    with open(filename) as f:
        for l in f:
            l = l.rstrip('\n')
            lines += [l]
    return lines

if __name__ == '__main__':
    import os.path
    print(partA(os.path.dirname(__file__) + '/../data/sample.txt'))
    print(partA(os.path.dirname(__file__) + '/../data/input.txt'))
    print(partB(os.path.dirname(__file__) + '/../data/sample.txt'))
    print(partB(os.path.dirname(__file__) + '/../data/input.txt'))