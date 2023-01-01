import os
import unittest
from aoc.utils import get_data_file_path
from .prod import partA, partB

class DayTestCase(unittest.TestCase):
    def testPartA(self):
        self.assertEqual(partA(get_data_file_path('sample.txt')), 10)
        self.assertEqual(partA(get_data_file_path('sample2.txt')), 18)
        self.assertEqual(partA(get_data_file_path('input.txt')), 295)

    def testPartB(self):
        self.assertEqual(partB(get_data_file_path('sample.txt')), 30)
        self.assertEqual(partB(get_data_file_path('sample2.txt')), 54)
        self.assertEqual(partB(get_data_file_path('input.txt')), 851)

if __name__ == '__main__':
    unittest.main()
