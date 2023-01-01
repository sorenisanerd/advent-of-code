import argparse
import importlib
import os
import sys

def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("year", type=int, help="Year of the challenge")
    parser.add_argument("day", type=int, help="Day of the challenge")
    parser.add_argument("part", type=str, nargs='?', choices=['A', 'B', 'a', 'b', '1', '2'], help="Part of the challenge")
    parser.add_argument("-i", "--input", type=str, help="Input file")
    args = parser.parse_args(argv)

    year = args.year
    day = args.day
    part = args.part

    parts = ['A', 'B']
    if part in ['A', 'a', '1']:
        parts = ['A']
    elif part in ['B', 'b', '2']:
        parts = ['B']

    module = importlib.import_module("aoc.year{}.day{:02}".format(year, day))

    if args.input:
        inputFile = args.input
    else:
        inputDirectory = os.path.abspath(os.path.dirname(__file__)) + '/../../data'
        inputFile = "{}/{:04}/{:02}/input.txt".format(inputDirectory, year, day)

    for part in parts:
        print(getattr(module, f"part{part}")(filename=inputFile))