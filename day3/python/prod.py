def getScore(s: str) -> int:
    assert len(s) == 1
    v = ord(s)
    if ord('a') <= v <= ord('z'):
        return v-ord('a')+1
    if ord('A') <= v <= ord('Z'):
        return v-ord('A')+27

def partA(filename: str) -> int:
    lines = getData(filename)
    score = 0
    for l in lines:
        comp1 = l[:len(l)//2]
        comp2 = l[len(l)//2:]
        whoopsie = set(comp1).intersection(set(comp2)).pop()
        score += getScore(whoopsie)
    return score

def partB(filename: str) -> int:
    lines = getData(filename)
    score = 0
    x = 0
    while x < len(lines):
        l1 = lines[x]
        l2 = lines[x+1]
        l3 = lines[x+2]
        x += 3
        whoopsie = set(l1).intersection(set(l2)).intersection(set(l3)).pop()
        score += getScore(whoopsie)
    return score


def getData(filename: str) -> list:
    lines = []
    with open(filename) as f:
        for l in f:
            l = l.strip()
            lines += [l]
    return lines

if __name__ == '__main__':
    import os.path
    print(partA(os.path.dirname(__file__) + '/../data/input.txt'))
    print(partB(os.path.dirname(__file__) + '/../data/input.txt'))