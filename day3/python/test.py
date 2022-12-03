import os
import unittest
from .prod import partA, partB

class Day3TestCase(unittest.TestCase):
    def testPartA(self):
        self.assertEqual(partA(os.path.dirname(__file__) + '/../data/sample.txt'), 157)

    def testScore(self):
        self.assertEqual(getScore('a'), 1)
        self.assertEqual(getScore('z'), 26)
        self.assertEqual(getScore('A'), 27)
        self.assertEqual(getScore('Z'), 52)

    def testPartB(self):
        self.assertEqual(partB(os.path.dirname(__file__) + '/../data/sample.txt'), 70)