import os
import unittest
from aoc.utils import get_data_file_path
from .prod import partA, partB, getAdjacentSurfaces

class DayTestCase(unittest.TestCase):
    def testPartA(self):
        self.assertEqual(partA(get_data_file_path('sample.txt')), 64)
        self.assertEqual(partA(get_data_file_path('input.txt')), 4460)

    def testGetAdjacentSurfaces(self):
        self.assertEqual(set(getAdjacentSurfaces(0, 0, 0, 'x')),
                         set([(0, 0, 0, 'y'),
                              (0, 0, 0, 'z'),
                              (1, 0, 0, 'y'),
                              (1, 0, 0, 'z'),
                              (0, -1, 0, 'y'),
                              (0, 0, -1, 'z'),
                              (1, -1, 0, 'y'),
                              (1, 0, -1, 'z')]))

    def testPartB(self):
        self.assertEqual(partB(get_data_file_path('sample.txt')), 58)
        self.assertEqual(partB(get_data_file_path('input.txt')), 2498)

if __name__ == '__main__':
    unittest.main()
