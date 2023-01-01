def areInOrder(left, right):
    for i in range(0, max(len(left), len(right))):
        if i >= len(left):
            return True
        if i >= len(right):
            return False

        l = left[i]
        r = right[i]

        if type(l) == type(r) == int:
            if r == l:
                continue
            if r < l:
                return False
            if l < r:
                return True

        if type(l) == type(r) == list:
            inOrder = areInOrder(l, r)
            if inOrder is not None:
                return inOrder

        if type(l) != type(r):
            if type(r) == int:
                r = [r]
            if type(l) == int:
                l = [l]
            inOrder = areInOrder(l, r)
            if inOrder is not None:
                return inOrder

    # Could not determine order
    return None

def compare(left, right):
    x = areInOrder(left, right)
    if x:
        return -1
    else:
        return 1

def partA(filename: str) -> int:
    lines = getLines(filename)
    counter = 0
    for i in range(0, len(lines), 3):
        left = eval(lines[i])
        right = eval(lines[i+1])
        if areInOrder(left, right):
            counter += i//3 + 1

    return counter

def partB(filename: str) -> int:
    lines = getLines(filename)

    elems = []
    elems += [[[2]]]
    elems += [[[6]]]

    for l in lines:
        if l == '':
            continue
        elems += [eval(l)]

    from functools import cmp_to_key
    ordered = sorted(elems, key=cmp_to_key(compare))

    return (ordered.index([[2]])+1) * (ordered.index([[6]])+1)

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
