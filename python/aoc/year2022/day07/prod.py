from aoc.utils import *

def partA(filename: str) -> int:
    return partAB(filename)[0]

def partB(filename: str) -> int:
    return partAB(filename)[1]

def partAB(filename: str) -> tuple[int, int]:
    lines = getLines(filename)

    assert lines[0] == '$ cd /'

    curdir = []
    dirs = {}
    dirs[()] = 0
    for l in lines:
        words = l.split(' ')
        if words[0] == '$':
            if words[1] == 'cd':
                if words[2] == '..':
                    curdir.pop()
                elif words[2][0] == '/':
                    curdir = []
                else:
                    curdir += [words[2]]
                    dirs[tuple(curdir)] = 0
            elif words[1] == 'ls':
                assert len(words) == 2
            else:
                assert False
        elif words[0] == 'dir':
            pass
        else:
            for p in prefixes(curdir):
                dirs[tuple(p)] += int(words[0])

    needed_capacity = 30_000_000
    current_capacity = 70_000_000 - dirs[()]

    ansA = sum([v for v in dirs.values() if v < 100_000])
    ansB: int = min([v for k, v in dirs.items() if (current_capacity + v) > needed_capacity])

    return ansA, ansB