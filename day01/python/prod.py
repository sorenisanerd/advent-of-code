def partA(filename: str) -> int:
    sums = getSums(filename)
    return max(sums)

def partB(filename: str) -> int:
    sums = getSums(filename)
    sums = sorted(sums)
    return sum(sums[-3:])

def getSums(filename: str) -> list:
    with open(filename) as f:
        sums = []
        sum = 0
        for l in f:
            l = l.strip()
            if l == '':
                sums.append(sum)
                sum = 0
                continue
            sum += int(l)
        sums.append(sum)
    return sums

if __name__ == '__main__':
    import os.path
    print(partA(os.path.dirname(__file__) + '/../data/input.txt'))
    print(partB(os.path.dirname(__file__) + '/../data/input.txt'))