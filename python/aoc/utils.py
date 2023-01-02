import importlib
import inspect
import re
import os
from functools import cache

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
    return os.path.abspath(os.path.dirname(__file__) + f"/../../data/{year}/{day}/{fname}")

intRegex = re.compile(r"-?\d+")

def ints(s) -> list[int]:
    return [int(x) for x in s.split() if intRegex.match(x)]

def getLines(filename: str) -> list[str]:
    return getData(filename).splitlines()

def getData(filename: str) -> str:
    with open(filename) as f:
        return f.read()

def chunkSize(l, n):
    """Yield successive n-sized chunks from l."""

    for i in range(0, len(l), n):
        yield l[i:i + n]

def chunkCount(l, n):
    """Yield n chunks from l."""

    rv = list(chunkSize(l, len(l)//n))
    assert len(rv) == n
    return rv

def prefixes(s):
    """Yield all prefixes of s."""

    for i in range(len(s)+1):
        yield s[:i]