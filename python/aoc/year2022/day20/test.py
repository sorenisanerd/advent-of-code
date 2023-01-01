import os
import unittest
from aoc.utils import get_data_file_path
from .prod import partA, partB, shift

class DayTestCase(unittest.TestCase):
    def testPartA(self):
        self.assertEqual(partA(get_data_file_path('sample.txt')), 3)
        self.assertEqual(partA(get_data_file_path('input.txt')), 7584)

    def testShift(self):
        def t(l, idx):
            l_ = list(enumerate(l))
            return [x[1] for x in shift(l_, l_[idx])]

        self.assertEqual(t([4, 5, 6, 1, 7, 8, 9], 3), [4, 5, 6, 7, 1, 8, 9])
        self.assertEqual(t([4, 5, 6, 2, 7, 8, 9], 3), [4, 5, 6, 7, 8, 2, 9])
        self.assertEqual(t([4, 5, 6, 3, 7, 8, 9], 3), [3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(t([4, 5, 6, 4, 7, 8, 9], 3), [4, 4, 5, 6, 7, 8, 9])
        self.assertEqual(t([4, -2, 5, 6, 7, 8, 9], 1), [4, 5, 6, 7, 8, -2, 9])

    def testPartB(self):
        self.assertEqual(partB(get_data_file_path('sample.txt')), 1623178306)
        self.assertEqual(partB(get_data_file_path('input.txt')), 4907679608191)
if __name__ == '__main__':
    unittest.main()
