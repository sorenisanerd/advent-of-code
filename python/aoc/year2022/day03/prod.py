import string

def getScore(s: str) -> int:
    assert len(s) == 1
    assert s in string.ascii_letters
    return string.ascii_letters.find(s)+1

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
        l1, l2, l3 = lines[x:x+3]
        x += 3
        whoopsie = set(l1).intersection(l2).intersection(l3).pop()
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