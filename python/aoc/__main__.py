import argparse
import os
import sys

from aoc.utils import get_year_day_module, get_year_day_test_module

years = [2022]
days = range(1, 26)

def run(args, years=years, days=days):
    if args.year is not None:
        years = [args.year]

    if args.day is not None:
        days = [args.day]

    parts = ['A', 'B']
    if args.part is not None:
        if args.part in ['A', 'a', '1']:
            parts = ['A']
        else:
            parts = ['B']

    benchmarkData = {}
    for year in years:
        benchmarkData[year] = {}
        for day in days:
            benchmarkData[year][day] = {}
            dayModule = get_year_day_module(year, day)

            if args.input is not None:
                inputFile = args.input
            else:
                inputFile = "{}/{:04}/{:02}/input.txt".format(args.input_dir, year, day)

            for part in parts:
                if hasattr(dayModule, f"part{part}"):
                    if args.bench:
                        import timeit
                        ti = timeit.Timer(lambda: getattr(dayModule, f"part{part}")(filename=inputFile))
                        numCalls, totTime = ti.autorange()
                        benchmarkData[year][day][f'part{part}'] = {'time_ms': 1000*totTime, 'calls': numCalls}
                        rv = '%05fms (averaged over %d runs)' % (1000*totTime / numCalls, numCalls)
                    else:
                        rv = getattr(dayModule, f"part{part}")(filename=inputFile)
                else:
                    rv = 'Not implemented'

                s = "Year {year:d}, day {day:d}, part {part}:".format(year=year, day=day, part=part)

                if type(rv) == str and '\n' in rv:
                    sep = '\n'
                else:
                    sep = ' '

                print(s, rv, sep=sep)
                if args.bench:
                    import json
                    json.dump(benchmarkData, open('benchmark.json', 'w'), indent=2)

def test(args):
    import unittest

    discover_path = 'aoc'
    if args.year is not None:
        discover_path += '.year{}'.format(args.year)
        if args.day is not None:
            discover_path += '.day{:02}'.format(args.day)

    suite = unittest.defaultTestLoader.discover(discover_path)

    # create a test runner and run the test suite
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    # print the result of the test run
    print(f'Tests run: {result.testsRun}')
    print(f'Errors: {len(result.errors)}')
    print(f'Failures: {len(result.failures)}')


def main(argv):
    parser = argparse.ArgumentParser(prog="aoc", description="Advent of Code")
    subparsers = parser.add_subparsers(dest="subcommand")

    testParser = subparsers.add_parser("test", help="Run tests")
    runParser = subparsers.add_parser("run", help="Run prod code")

    for p in [testParser, runParser]:
        p.add_argument("year", type=int, nargs='?', choices=years, help="Year of the challenge")
        p.add_argument("day", type=int, nargs='?', choices=days, help="Day of the challenge")
        p.add_argument("--input-dir", type=str, metavar='DIR',
                        default=(os.path.abspath(os.path.dirname(__file__)) + '/../../data'),
                        help="Directory structure holding input files in YYYY/DD/input.txt")

    runParser.add_argument("part", type=str, nargs='?',
                           choices=['A', 'B', 'a', 'b', '1', '2'],
                           help="Part of the challenge")

    runParser.add_argument("-i", "--input", type=str, help="Input file")
    runParser.add_argument("-b", "--bench", action='store_true', help="Run code in benchmark mode")

    runParser.set_defaults(func=run)
    testParser.set_defaults(func=test)

    args = parser.parse_args(argv)

    if args.subcommand is None:
        parser.print_help()
        return

    args.func(args)

if __name__ == "__main__":
    main(sys.argv[1:])
