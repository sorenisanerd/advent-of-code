from aoc.utils import *

def myCmp(left, right):
    if type(left) == int and type(right) == int:
        return cmp(left, right)
    elif left == [] and right == []:
        return 0
    elif left == [] and type(right) == list:
        return -1
    elif type(left) == list and right == []:
        return 1
    elif type(left) == list and type(right) == list:
        return myCmp(left[0], right[0]) or myCmp(left[1:], right[1:])
    elif type(left) == list and type(right) == int:
        return myCmp(left, [right])
    elif type(left) == int and type(right) == list:
        return myCmp([left], right)
    assert False

def partA(filename: str) -> int:
    lines = getLines(filename)
    counter = 0
    for idx, ls in enumerate(chunkBySize(lines, 3)):
        left, right = map(eval, ls[:2])
        if myCmp(left, right) == -1:
            counter += idx + 1

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
    ordered = sorted(elems, key=cmp_to_key(myCmp))

    return (ordered.index([[2]])+1) * (ordered.index([[6]])+1)
