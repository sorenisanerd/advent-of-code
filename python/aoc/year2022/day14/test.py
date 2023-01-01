import os
import unittest
from .prod import partA, partB

class DayTestCase(unittest.TestCase):
    def testPartA(self):
        self.assertEqual(partA(os.path.dirname(__file__) + '/../data/sample.txt'), 25)
        self.assertEqual(partA(os.path.dirname(__file__) + '/../data/input.txt'), 738)

    def testPartB(self):
        self.assertEqual(partB(os.path.dirname(__file__) + '/../data/sample.txt'), 93)
        self.assertEqual(partB(os.path.dirname(__file__) + '/../data/input.txt'), 28145)

if __name__ == '__main__':
    unittest.main()
