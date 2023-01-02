from aoc.utils import *

import string
import re

def partA(filename: str) -> str:
    moves, stacks = parseFile(filename)

    def move(stacks, from_stack, to_stack):
        from_stack -= 1
        to_stack -= 1
        stacks[to_stack] += [stacks[from_stack].pop()]
        return stacks

    for count, from_stack, to_stack in moves:
        for i in range(count):
            stacks = move(stacks, from_stack, to_stack)

    return ''.join([s[-1] for s in stacks])

def parseFile(filename):
    stackData, moveData = getData(filename).split('\n\n')

    stackLines = stackData.splitlines()[::-1]
    stackCount = max(ints(stackLines[0]))

    stacks = [[] for _ in range(stackCount)]
    for l in stackLines[1:]:
        for i in range(stackCount):
            idx = 1+i*4

            if idx > len(l)-1:
                continue

            if l[idx] in string.ascii_uppercase:
                stacks[i] += [l[idx]]

    return [ints(s) for s in moveData.splitlines()], stacks

def partB(filename: str) -> str:
    moves, stacks = parseFile(filename)

    def move(stacks, count, from_stack, to_stack):
        from_stack -= 1
        to_stack -= 1
        stacks[to_stack] += stacks[from_stack][-count:]
        stacks[from_stack] = stacks[from_stack][:-count]
        return stacks

    for count, from_stack, to_stack in moves:
        stacks = move(stacks, count, from_stack, to_stack)

    return ''.join([s[-1] for s in stacks])

if __name__ == '__main__':
    import os.path
    print(partA(get_data_file_path('input.txt')))
    print(partB(get_data_file_path('input.txt')))