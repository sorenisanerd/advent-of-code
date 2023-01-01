import importlib
import inspect
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

def ints(s) -> list[int]:
    return [int(x) for x in s.split()]

def getLines(filename: str) -> list[str]:
    return getData(filename).splitlines()

def getData(filename: str) -> str:
    with open(filename) as f:
        return f.read()