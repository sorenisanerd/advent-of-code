import os
import unittest
from aoc.utils import get_data_file_path
from .prod import partA, partB

class DayTestCase(unittest.TestCase):
    def testPartA(self):
        self.assertEqual(partA(get_data_file_path('sample.txt')), 7)
        self.assertEqual(partA(get_data_file_path('input.txt')), 1794)

    def testPartB(self):
        self.assertEqual(partB(get_data_file_path('sample.txt')), 19)
        self.assertEqual(partB(get_data_file_path('input.txt')), 2851)

if __name__ == '__main__':
    unittest.main()

