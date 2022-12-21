def partA(filename: str) -> int:
    lines = getLines(filename)

    knowns, unknowns = parseLines(lines)

    while True:
        if 'root' in knowns:
            return int(knowns['root'])
        for k in unknowns:
            v1, op, v2 = unknowns[k].split(' ')
            if v1 in knowns and v2 in knowns:
                v1 = knowns[v1]
                v2 = knowns[v2]
                knowns[k] = eval(' '.join(map(str, (v1, op, v2))))
                break
        del unknowns[k]

def parseLines(lines):
    knowns = dict()
    unknowns = dict()
    for l in lines:
        k, expr = l.split(': ')
        if all([x in '0123456789' for x in expr]):
            knowns[k] = float(expr)
        else:
            unknowns[k] = expr
    return knowns,unknowns

def partB(filename: str) -> int:
    lines = getLines(filename)
    knowns, unknowns = parseLines(lines)

    def tryGuess(guess, knowns=knowns, unknowns=unknowns):
        knowns = dict(knowns)
        unknowns = dict(unknowns)
        knowns['humn'] = guess
        while True:
            found = False
            for k in unknowns:
                v1, op, v2 = unknowns[k].split(' ')
                if v1 in knowns and v2 in knowns:
                    v1 = knowns[v1]
                    v2 = knowns[v2]
                    if k == 'root':
                        return round(v1 - v2, 3)

                    expr = '%f %s %f' % (v1, op, v2)
                    knowns[k] = eval(expr)
                    found = True
                    break
            if found:
                del unknowns[k]

    prev = 0
    def newtonApproximation(tryGuess=tryGuess, start=0.0, goal=0.0):
        prevResult = tryGuess(start)
        prevGuess = start
        dx = 1
        curGuess = prevGuess + dx

        while True:
            newResult = tryGuess(curGuess)

            if newResult == goal:
                return int(curGuess)

#            if newResult == prevResult:
#                curGuess += dx//abs(dx)
#                continue

            dx = (curGuess - prevGuess) * (newResult/(prevResult-newResult))

            prevGuess = curGuess
            curGuess += dx

    return newtonApproximation()

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