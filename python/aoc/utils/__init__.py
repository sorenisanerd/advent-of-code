import importlib
import inspect
import re
import os
from functools import cache, total_ordering
from itertools import zip_longest

from .vectors import V2

four_directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
eight_directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

def get_year_day_module(year, day):
    return importlib.import_module(f"aoc.year{year}.day{day:02}")

def get_year_day_test_module(year, day):
    return importlib.import_module(f"aoc.year{year}.day{day:02}.test")

def caller_filename():
    # get the stack frame for the function that called this function
    caller_frame = inspect.stack()[2]

    # get the filename from the frame object
    filename = caller_frame.filename

    return filename

def get_data_file_path(fname=''):
    filename = caller_filename()
    year = filename.split('/')[-3][-4:]
    day = filename.split('/')[-2][-2:]
    return os.path.abspath(os.path.dirname(__file__) + f"/../../../data/{year}/{day}/{fname}")

intRegex = re.compile(r"-?\d+")

def ints(s) -> list[int]:
    return [int(x) for x in re.findall(r'-?\d+', s)]

def getLines(filename: str) -> list[str]:
    return getData(filename).splitlines()

def getData(filename: str) -> str:
    with open(filename) as f:
        return f.read()

def chunkBySize(l, n:int):
    """Yield successive n-sized chunks from l."""

    for i in range(0, len(l), n):
        yield l[i:i + n]

def chunkByCount(l, n):
    """Yield n chunks from l."""

    rv = list(chunkBySize(l, len(l)//n))
    assert len(rv) == n
    return rv

def prefixes(s):
    """Yield all prefixes of s."""

    for i in range(len(s)+1):
        yield s[:i]

def sign(x):
    if x == 0:
        return 0
    return int(x/abs(x))

class V(object):
    def __init__(self, *args):
        if len(args) == 1 and isinstance(args[0], (list, tuple)):
            args = args[0]
        self.val = args

    def __eq__(self, other):
        if isinstance(other, V):
            return self.val == other.val
        else:
            return self.val == other

    def __mul__(self, other):
        if isinstance(other, int):
            return V(*[a*other for a in self.val])
        elif isinstance(other, V):
            return V(*[a*b for a,b in zip_longest(self.val, other.val)])
        else:
            raise Exception(f"Can't multiply V by {other}")

    def __add__(self, other):
        if isinstance(other, int):
            return V(*[a+other for a in self.val])
        if isinstance(other, tuple):
            other = V(*other)
        return V(*[self.val[i]+other.val[i] for i in range(len(self.val))])

    def __str__(self) -> str:
        return str(self.val)

    def __repr__(self) -> str:
        return 'V' + repr(self.val)

    def __lt__(self, other) -> int:
        return self.val < other.val

    def __getitem__(self, key):
        if isinstance(key, slice):
            return V(*self.val[key])
        return self.val[key]

    def __getattr__(self, name) -> int:
        if name in 'xyz':
            return self.val[ord(name)-ord('x')]
        raise AttributeError(name)

    def __hash__(self):
        return hash(self.val)

def MD2(a:V, b:V) -> int:
    return abs(a.val[0]-b.val[0]) + abs(a.val[1]-b.val[1])

def line(p1, p2):
    if not (p1.x == p2.x or p1.y == p2.y or abs(p1.x-p2.x) == abs(p1.y-p2.y)):
        raise Exception("Not a horizontal, vertical, or perfectly diagonal line")

    d = V2(sign(p2.x - p1.x), sign(p2.y - p1.y))
    p = p1
    while True:
        yield p
        if p == p2:
            break
        p += d

class Map(object):
    def __init__(self, data, mapFunc=lambda x:x, fill=None):
        self.data = []
        maxlen = 0
        for row in data:
            self.data += [list(map(mapFunc, row))]
            maxlen = max(maxlen, len(row))

        if fill is not None:
            for row in self.data:
                row += [fill] * (maxlen - len(row))

        self.minx, self.miny, self.maxx, self.maxy = 0, 0, maxlen-1, len(self.data)-1

    def _boundsCheck(self, x, y) -> bool:
        return 0 <= y and y <= self.maxy and 0 <= x and x < len(self.data[y])

    def boundsCheck(self, p) -> bool:
        if isinstance(p, V):
            return self._boundsCheck(p.x, p.y)
        elif isinstance(p, tuple) and len(p) == 2:
            return self._boundsCheck(p[0], p[1])
        else:
            raise Exception(f"Can't bounds check {p}")

    def find(self, val):
        try:
            return next(self.findAll(val))
        except StopIteration:
            return None

    def findAll(self, val):
        for y, row in enumerate(self.data):
            for x, v in enumerate(row):
                if v == val:
                    yield V(x, y)

    def getXY(self, x, y):
        if not self._boundsCheck(x, y):
            return OutOfBounds
        return self.data[y][x]

    def __getitem__(self, key):
        return self.getXY(key.x, key.y)

    def setXY(self, x, y, val):
        if not self._boundsCheck(x, y):
            return OutOfBounds
        self.data[y][x] = val

    def __setitem__(self, key, val):
        if isinstance(key, V2):
            return self.setXY(key.x, key.y, val)
        if isinstance(key, V):
            return self.setXY(key.val[0], key.val[1], val)
        elif isinstance(key, tuple) and len(key) == 2:
            return self.setXY(key[0], key[1], val)
        assert False

    def __str__(self, minx=None, maxx=None, miny=None, maxy=None):
        return '\n'.join([''.join(row[minx:maxx]) for row in self.data[miny:maxy]])

    @property
    def minmaxx(self):
        return self.minx, self.maxx

    @property
    def minmaxy(self):
        return self.miny, self.maxy

    def xrange(self):
        return range(self.minx, self.maxx+1)

    def yrange(self):
        return range(self.miny, self.maxy+1)

    def __iter__(self):
        for y in self.yrange():
            for x in self.xrange():
                yield V(x, y)

OutOfBounds = Exception('Out of bounds')

def dijkstra(starts, end, generateNeighbors):
    from queue import PriorityQueue
    q = PriorityQueue()

    for s in starts:
        q.put((0, s))

    visited = set()
    while not q.empty():
        cost, p = q.get()

        if p == end:
            return cost

        if p in visited:
            continue

        visited.add(p)

        for (cost_, neighbor) in generateNeighbors(p):
            if neighbor not in visited:
                q.put((cost+cost_, neighbor))
    assert False

def cmp(a, b):
    return (a > b) - (a < b)

def createEmptyMap(width, height, fill=None) -> Map:
    return Map([[fill] * width for _ in range(height)])


class SparseMap(Map):
    def __init__(self, data=None, mapFunc=lambda x:x, unset=None):
        """A map that only stores non-unset values.
        @unset is the value that is considered unset
        @mapFunc is a function that is called on each input value before storing it. int is a good candidate"""
        self.data = dict()

        minx, miny, maxx, maxy = None, None, None, None

        if data is None:
            data = []

        self.unset = unset

        for y, row in enumerate(data):
            for x, val in enumerate(row):
                val = mapFunc(val)
                if val != unset:
                    self.data[V(x,y)] = val

                    if minx is None:
                        minx, maxx, miny, maxy = x, x, y, y
                    else:
                        minx = min(minx, x)
                        maxx = max(maxx, x)
                        miny = min(miny, y)
                        maxy = max(maxy, y)

        self.minx, self.miny, self.maxx, self.maxy = miny, miny, maxx, maxy

    def _boundsCheck(self, x, y) -> bool:
        return self.miny <= y and y < self.maxy and self.minx <= x and x < self.maxx

    def getXY(self, x, y):
        return self.data.get((x, y), self.unset)

    def setXY(self, x, y, val):
        if self.minx is None:
            self.minx = self.maxx = x
            self.miny = self.maxy = y
        else:
            self.miny = min(self.miny, y)
            self.maxx = max(self.maxx, x)
            self.miny = min(self.miny, y)
            self.maxy = max(self.maxy, y)

        self.data[V(x, y)] = val

    def findAll(self, val):
        for k, v in self.data.items():
            if v == val:
                yield V(*k)

    def __str__(self):
        rv:str = ''
        first = True
        for y in self.yrange():
            if not first:
                rv += '\n'
            for x in self.xrange():
                rv += self.getXY(x, y)
            first = False
        return rv

# Takes a list and returns a generator returning
# 2-tuples like so:
# choose_one([1,2,3]):
# (1, [2,3])
# (2, [1,3])
# (3, [1,2])
# So first element of the tuple iterates over the list
# and the second element is the list without the first element
def choose_one(l):
    for i in range(len(l)):
        yield (l[i], l[:i] + l[i+1:])

