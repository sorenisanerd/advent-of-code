import string
import re

def partA(filename: str) -> str:
    moveLines, stacks = parseFile(filename)

    def move(stacks, from_stack, to_stack):
        from_stack -= 1
        to_stack -= 1
        stacks[to_stack] += [stacks[from_stack].pop()]
        return stacks

    regex = re.compile('move (\d+) from (\d+) to (\d+)')
    for l in moveLines:
        matches = regex.match(l)
        count, from_stack, to_stack = list(map(int, matches.groups()))

        for i in range(count):
            stacks = move(stacks, from_stack, to_stack)

    return ''.join([s[-1] for s in stacks])

def parseFile(filename):
    lines = getLines(filename)

    beforeLines = []
    moveLines = []
    state = 'READING_STATE'
    for l in lines:
        if l == '':
            if state == 'READING_STATE':
                state = 'READING_MOVES'
            continue
        if state == 'READING_STATE':
            beforeLines += [l]
        elif state == 'READING_MOVES':
            moveLines += [l]
        else:
            assert False

    stacks = parseStacks(beforeLines)
    return moveLines,stacks

def parseStacks(beforeLines):
    numbers = list(map(lambda x:int(x), filter(lambda s:len(s.strip())>0, re.split(r'\s+', beforeLines[-1]))))
    number_of_stacks = numbers[-1]
    stacks = []
    i = 0
    for x in range(number_of_stacks):
        stacks += [[]]

    for l in beforeLines[-2::-1]:
        for x in range(number_of_stacks):
            idx = 1+x*4
            if idx > len(l)-1:
                continue
            if l[idx] in string.ascii_uppercase:
                stacks[x] += [l[idx]]
    return stacks


def partB(filename: str) -> int:
    moveLines, stacks = parseFile(filename)

    def move(stacks, count, from_stack, to_stack):
        from_stack -= 1
        to_stack -= 1
        stacks[to_stack] += stacks[from_stack][-count:]
        stacks[from_stack] = stacks[from_stack][:-count]
        return stacks

    for l in moveLines:
        matches = re.match('move (\d+) from (\d+) to (\d+)', l)
        count, from_stack, to_stack = list(map(int, matches.groups()))
        stacks = move(stacks, count, from_stack, to_stack)

    return ''.join([s[-1] for s in stacks])

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