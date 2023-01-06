import os
import unittest
from aoc.utils import *

from .prod import partA, partB, followEdge

class DayTestCase(unittest.TestCase):
    def testPartA(self):
        self.assertEqual(partA(get_data_file_path('sample.txt'), 10), 26)
        self.assertEqual(partA(get_data_file_path('input.txt'), 2000000), 4737443)

    def testFollowEdge(self):
        self.assertEqual(list(followEdge(V(5, 5), V(5, 7))),
                        [V(2, 5), V(3, 6), V(4, 7), V(5, 8), V(6, 7), V(7, 6), V(8, 5), V(7, 4), V(6, 3), V(5, 2), V(4, 3), V(3, 4)])

    def testPartB(self):
        self.assertEqual(partB(get_data_file_path('sample.txt'), 0, 0, 20, 20), 56000011)
        self.assertEqual(partB(get_data_file_path('input.txt'), 0, 0, 4000000, 4000000), 11482462818989)

if __name__ == '__main__':
    unittest.main()
