import os
import unittest
from aoc.utils import get_data_file_path
from .prod import partA, partB

class DayTestCase(unittest.TestCase):
    def testPartA(self):
        self.assertEqual(partA(get_data_file_path('sample.txt')), 21)
        self.assertEqual(partA(get_data_file_path('input.txt')), 1812)

    def testPartB(self):
        self.assertEqual(partB(get_data_file_path('sample.txt')), 8)
        self.assertEqual(partB(get_data_file_path('input.txt')), 315495)