import os
import unittest
from aoc.utils import get_data_file_path
from .prod import partA, partB, getScore

class DayTestCase(unittest.TestCase):
    def testPartA(self):
        self.assertEqual(partA(get_data_file_path('sample.txt')), 157)
        self.assertEqual(partA(get_data_file_path('input.txt')), 8039)

    def testScore(self):
        self.assertEqual(getScore('a'), 1)
        self.assertEqual(getScore('z'), 26)
        self.assertEqual(getScore('A'), 27)
        self.assertEqual(getScore('Z'), 52)

    def testPartB(self):
        self.assertEqual(partB(get_data_file_path('sample.txt')), 70)
        self.assertEqual(partB(get_data_file_path('input.txt')), 2510)
if __name__ == '__main__':
    unittest.main()

