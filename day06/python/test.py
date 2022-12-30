import os
import unittest
from .prod import partA, partB

class DayTestCase(unittest.TestCase):
    def testPartA(self):
        self.assertEqual(partA(os.path.dirname(__file__) + '/../data/sample.txt'), 7)
        self.assertEqual(partA(os.path.dirname(__file__) + '/../data/input.txt'), 1794)

    def testPartB(self):
        self.assertEqual(partB(os.path.dirname(__file__) + '/../data/sample.txt'), 19)
        self.assertEqual(partB(os.path.dirname(__file__) + '/../data/input.txt'), 2851)

if __name__ == '__main__':
    unittest.main()

