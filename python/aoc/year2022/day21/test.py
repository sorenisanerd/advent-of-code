import os
import unittest
from aoc.utils import get_data_file_path
from .prod import partA, partB

class DayTestCase(unittest.TestCase):
    def testPartA(self):
        self.assertEqual(partA(get_data_file_path('sample.txt')), 152)
        self.assertEqual(partA(get_data_file_path('input.txt')), 152479825094094)

    def testPartB(self):
        self.assertEqual(partB(get_data_file_path('sample.txt')), 301)
        self.assertEqual(partB(get_data_file_path('input.txt')), 3360561285172)

if __name__ == '__main__':
    unittest.main()
