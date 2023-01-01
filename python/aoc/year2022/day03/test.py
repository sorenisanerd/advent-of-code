import os
import unittest
from .prod import partA, partB, getScore

class DayTestCase(unittest.TestCase):
    def testPartA(self):
        self.assertEqual(partA(os.path.dirname(__file__) + '/../data/sample.txt'), 157)
        self.assertEqual(partA(os.path.dirname(__file__) + '/../data/input.txt'), 8039)

    def testScore(self):
        self.assertEqual(getScore('a'), 1)
        self.assertEqual(getScore('z'), 26)
        self.assertEqual(getScore('A'), 27)
        self.assertEqual(getScore('Z'), 52)

    def testPartB(self):
        self.assertEqual(partB(os.path.dirname(__file__) + '/../data/sample.txt'), 70)
        self.assertEqual(partB(os.path.dirname(__file__) + '/../data/input.txt'), 2510)
if __name__ == '__main__':
    unittest.main()

