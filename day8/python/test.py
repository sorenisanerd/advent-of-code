import os
import unittest
from prod import partA, partB

class Day1TestCase(unittest.TestCase):
    def testPartA(self):
        self.assertEqual(partA(os.path.dirname(__file__) + '/../data/sample.txt'), 21)

    def testPartB(self):
        self.assertEqual(partB(os.path.dirname(__file__) + '/../data/sample.txt'), 8)

if __name__ == '__main__':
    unittest.main()