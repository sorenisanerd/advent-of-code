import os
import unittest
from aoc.utils import *
from .prod import partA, partB

class DayXXTestCase(unittest.TestCase):
    def testPartA(self):
        self.assertEqual(partA(get_data_file_path('sample.txt')), 0)
        self.assertEqual(partA(get_data_file_path('input.txt')), 0)

    def testPartB(self):
        self.assertEqual(partB(get_data_file_path('sample.txt')), 0)
        self.assertEqual(partB(get_data_file_path('input.txt')), 0)