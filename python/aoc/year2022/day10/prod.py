from typing import Any
from aoc.utils import *

def partA(filename: str) -> int:
    lines = getLines(filename)
    history = calculateHistory(lines)

    counter = 0
    for x in range(19, len(history), 40):
        counter += (x+1)*history[x]

    return counter

def calculateHistory(lines: list[str]):
    history = [1]
    for l in lines:
        args = l.split(' ')
        history += history[-1:]

        if args[0] == 'noop':
            continue

        _, val = l.split()
        history += [history[-1] + int(val)]
    return history

def partB(filename: str) -> str:
    lines = getLines(filename)
    history: list[Any] = calculateHistory(lines)

    for h in range(len(history)):
        sprite_position = history[h]
        col = h % 40
        if abs(col-sprite_position) < 2:
            history[h] = '#'
        else:
            history[h] = '.'

    rv = []
    for i in range(0, 240, 40):
        rv += [''.join(history[i:i+40])]

    return '\n'.join(rv)