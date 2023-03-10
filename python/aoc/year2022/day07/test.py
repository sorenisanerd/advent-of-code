import os
import unittest
from aoc.utils import *
from .prod import partA, partB

class DayTestCase(unittest.TestCase):
    def testPartA(self):
        self.assertEqual(partA(get_data_file_path('sample.txt')), 95437)
        self.assertEqual(partA(get_data_file_path('input.txt')), 1611443)

    def testPartB(self):
        self.assertEqual(partB(get_data_file_path('sample.txt')), 24933642)
        self.assertEqual(partB(get_data_file_path('input.txt')), 2086088)

if __name__ == '__main__':
    unittest.main()

