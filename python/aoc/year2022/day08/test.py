import os
import unittest
from .prod import partA, partB

class DayTestCase(unittest.TestCase):
    def testPartA(self):
        self.assertEqual(partA(os.path.dirname(__file__) + '/../data/sample.txt'), 21)
        self.assertEqual(partA(os.path.dirname(__file__) + '/../data/input.txt'), 1812)

    def testPartB(self):
        self.assertEqual(partB(os.path.dirname(__file__) + '/../data/sample.txt'), 8)
        self.assertEqual(partB(os.path.dirname(__file__) + '/../data/input.txt'), 315495)

if __name__ == '__main__':
    unittest.main()
