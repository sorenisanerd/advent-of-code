def partA(filename: str) -> int:
    lines = getLines(filename)
    return 0

def partB(filename: str) -> int:
    lines = getLines(filename)
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
    print(partA(os.path.dirname(__file__) + '/../data/input.txt'))
    print(partB(os.path.dirname(__file__) + '/../data/input.txt'))