import os
import unittest
from .prod import partA, partB

class DayTestCase(unittest.TestCase):
    def testPartA(self):
        self.assertEqual(partA(os.path.dirname(__file__) + '/../data/sample.txt'), 13)
        self.assertEqual(partA(os.path.dirname(__file__) + '/../data/input.txt'), 6642)

    def testPartB(self):
        self.assertEqual(partB(os.path.dirname(__file__) + '/../data/sample.txt'), 1)
        self.assertEqual(partB(os.path.dirname(__file__) + '/../data/sample2.txt'), 36)
        self.assertEqual(partB(os.path.dirname(__file__) + '/../data/input.txt'), 2765)

if __name__ == '__main__':
    unittest.main()

