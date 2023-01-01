import os
import unittest
from aoc.utils import get_data_file_path
from .prod import partA, partB

class DayTestCase(unittest.TestCase):
    def testPartA(self):
        self.assertEqual(partA(get_data_file_path('sample.txt')), 110)
        self.assertEqual(partA(get_data_file_path('input.txt')), 4070)

    def testPartB(self):
        self.assertEqual(partB(get_data_file_path('sample.txt')), 20)
        self.assertEqual(partB(get_data_file_path('input.txt')), 881)

if __name__ == '__main__':
    unittest.main()
