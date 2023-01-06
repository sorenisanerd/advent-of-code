import timeit

from aoc.utils import *

a = V(1,0)
b = V(0,1)

c = (1,0)
d = (1,0)

def addV() -> V:
    return a + b

def addT():
    return (c[0]+d[0], c[1]+d[1])

if __name__ == '__main__':
     print(timeit.timeit(stmt=addV, number=10_219_247, globals=None))
     print(timeit.timeit(stmt=addT, number=10_219_247, globals=None))