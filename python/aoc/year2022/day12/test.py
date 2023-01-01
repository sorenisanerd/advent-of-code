import os
import unittest
from aoc.utils import get_data_file_path
from .prod import partA, partB

class DayTestCase(unittest.TestCase):
    def testPartA(self):
        self.assertEqual(partA(get_data_file_path('sample.txt')), 31)
        self.assertEqual(partA(get_data_file_path('input.txt')), 420)

    def testPartB(self):
        self.assertEqual(partB(get_data_file_path('sample.txt')), 29)
        self.assertEqual(partB(get_data_file_path('input.txt')), 414)

if __name__ == '__main__':
    unittest.main()

