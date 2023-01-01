import os
import unittest
from .prod import partA, partB

class DayTestCase(unittest.TestCase):
    def testPartA(self):
        self.assertEqual(partA(os.path.dirname(__file__) + '/../data/sample.txt'), 31)
        self.assertEqual(partA(os.path.dirname(__file__) + '/../data/input.txt'), 420)

    def testPartB(self):
        self.assertEqual(partB(os.path.dirname(__file__) + '/../data/sample.txt'), 29)
        self.assertEqual(partB(os.path.dirname(__file__) + '/../data/input.txt'), 414)

if __name__ == '__main__':
    unittest.main()

