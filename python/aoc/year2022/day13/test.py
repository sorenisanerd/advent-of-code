import os
import unittest
from aoc.utils import get_data_file_path
from .prod import partA, partB, areInOrder

class DayTestCase(unittest.TestCase):
    def testPartA(self):
        self.assertEqual(partA(get_data_file_path('sample.txt')), 13)
        self.assertEqual(partA(get_data_file_path('input.txt')), 5340)

    def testIsInOrder(self):
        self.assertEqual(areInOrder([1], [2]), True)
        self.assertEqual(areInOrder([2], [1]), False)
        self.assertEqual(areInOrder([[2]], [[1]]), False)
        self.assertEqual(areInOrder([[2]], [[1, 3]]), False)
        self.assertEqual(areInOrder([[2]], [[2, 3]]), True)


    def testPartB(self):
        self.assertEqual(partB(get_data_file_path('sample.txt')), 140)
        self.assertEqual(partB(get_data_file_path('input.txt')), 21276)

if __name__ == '__main__':
    unittest.main()
