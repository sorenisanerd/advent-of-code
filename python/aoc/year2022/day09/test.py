import os
import unittest
from aoc.utils import *
from .prod import partA, partB, track

class DayTestCase(unittest.TestCase):
    def testPartA(self):
        self.assertEqual(partA(get_data_file_path('sample.txt')), 13)
        self.assertEqual(partA(get_data_file_path('input.txt')), 6642)

    def testTrack(self):
        self.assertEquals(track(V(0,0), V(0,0)), V(0,0))
        self.assertEquals(track(V(2,0), V(0,0)), V(1,0))
        self.assertEquals(track(V(0,2), V(0,0)), V(0,1))

    def testPartB(self):
        self.assertEqual(partB(get_data_file_path('sample.txt')), 1)
        self.assertEqual(partB(get_data_file_path('sample2.txt')), 36)
        self.assertEqual(partB(get_data_file_path('input.txt')), 2765)

if __name__ == '__main__':
    unittest.main()

