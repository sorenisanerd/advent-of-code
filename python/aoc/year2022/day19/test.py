import os
import unittest
from aoc.utils import get_data_file_path
from .prod import partA, partB, addVectors

class DayTestCase(unittest.TestCase):
    def testPartA(self):
        self.assertEqual(partA(get_data_file_path('sample.txt')), 33)
        self.assertEqual(partA(get_data_file_path('input.txt')), 1199)

    def testAddVectors(self):
        self.assertEqual(addVectors(tuple(), tuple()), tuple())
        self.assertEqual(addVectors(tuple((3,4,5)), tuple()), tuple((3,4,5)))
        self.assertEqual(addVectors(tuple(), tuple((3,4,5))), tuple((3,4,5)))
        self.assertEqual(addVectors(tuple((3,4,5)), tuple((10,11,12))), tuple((13,15,17)))
        self.assertEqual(addVectors(tuple(), tuple((3,4,5))), tuple((3,4,5)))

    def testPartB(self):
        self.assertEqual(partB(get_data_file_path('sample.txt')), 62*56)
        self.assertEqual(partB(get_data_file_path('input.txt')), 3510)

if __name__ == '__main__':
    unittest.main()
