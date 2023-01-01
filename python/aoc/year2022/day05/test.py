import os
import unittest
from aoc.utils import get_data_file_path
from .prod import partA, partB, parseStacks

class DayTestCase(unittest.TestCase):
    def testPartA(self):
        self.assertEqual(partA(get_data_file_path('sample.txt')), 'CMZ')
        self.assertEqual(partA(get_data_file_path('input.txt')), 'FWSHSPJWM')

    def testParseStacks(self):
        self.assertEqual(parseStacks(['    [D]    ',
                                      '[N] [C]    ',
                                      '[Z] [M] [P]',
                                      ' 1   2   3 ']), [['Z', 'N'], ['M', 'C', 'D'], ['P']])
    def testPartB(self):
        self.assertEqual(partB(get_data_file_path('sample.txt')), 'MCD')
        self.assertEqual(partB(get_data_file_path('input.txt')), 'PWPWHGFZS')

if __name__ == '__main__':
    unittest.main()

