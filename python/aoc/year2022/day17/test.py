import os
import unittest
from aoc.utils import get_data_file_path
from .prod import partA, partB, addShapeToSilo, wouldOverlap

class DayTestCase(unittest.TestCase):
    def testPartA(self):
        self.assertEqual(partA(get_data_file_path('sample.txt')), 3068)
        self.assertEqual(partA(get_data_file_path('input.txt')), 3186)

    def testWouldOverLap(self):
        self.assertEqual(wouldOverlap([], ['####'], 0, 0), False)
        self.assertEqual(wouldOverlap([], ['####'], 2, 0), False)
        self.assertEqual(wouldOverlap([], ['####'], 3, 0), False)
        self.assertEqual(wouldOverlap(['#      '], ['####'], 0, 0), True)
        self.assertEqual(wouldOverlap(['#      '], ['####'], 1, 0), False)
        self.assertEqual(wouldOverlap(['    #  '], ['####'], 1, 0), True)

        self.assertEqual(wouldOverlap([], ['##', '##'], 0, 0), True)
        self.assertEqual(wouldOverlap([], ['##', '##'], 0, 1), False)
        self.assertEqual(wouldOverlap([], ['##', '##'], 5, 1), False)
        self.assertEqual(wouldOverlap(['  #    ']*3, ['##', '##'], 0, 1), False)
        self.assertEqual(wouldOverlap(['  #    ']*3, ['##', '##'], 1, 1), True)
        self.assertEqual(wouldOverlap(['  #    ']*3, ['##', '##'], 5, 1), False)
        self.assertEqual(wouldOverlap(['  #    ']*3, ['##', '##'], 5, 1), False)

    def testPartB(self):
        self.assertEqual(partB(get_data_file_path('sample.txt')), 1514285714288)
        self.assertEqual(partB(get_data_file_path('input.txt')), 1566376811584)

if __name__ == '__main__':
    unittest.main()
