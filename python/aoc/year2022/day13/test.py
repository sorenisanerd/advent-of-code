import os
import unittest
from aoc.utils import get_data_file_path
from .prod import partA, partB, myCmp

class DayTestCase(unittest.TestCase):
    def testPartA(self):
        self.assertEqual(partA(get_data_file_path('sample.txt')), 13)
        self.assertEqual(partA(get_data_file_path('input.txt')), 5340)

    def testIsInOrder(self):
        self.assertEqual(myCmp([1,1,3,1,1], [1,1,5,1,1]), -1)
        self.assertEqual(myCmp([[1],[2,3,4]], [[1],4]), -1)
        self.assertEqual(myCmp([9], [[8,7,6]]), 1)
        self.assertEqual(myCmp([[4,4],4,4], [[4,4],4,4,4]), -1)
        self.assertEqual(myCmp([7,7,7,7], [7,7,7]), 1)
        self.assertEqual(myCmp([], [3]),  -1)
        self.assertEqual(myCmp([[[]]], [[]]), 1)
        self.assertEqual(myCmp([1,[2,[3,[4,[5,6,7]]]],8,9], [1,[2,[3,[4,[5,6,0]]]],8,9]),  1)


    def testPartB(self):
        self.assertEqual(partB(get_data_file_path('sample.txt')), 140)
        self.assertEqual(partB(get_data_file_path('input.txt')), 21276)

if __name__ == '__main__':
    unittest.main()
