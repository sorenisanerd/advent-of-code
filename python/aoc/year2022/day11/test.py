import os
import unittest
from .prod import partA, partB

class DayTestCase(unittest.TestCase):
    def testPartA(self):
        self.assertEqual(partA(os.path.dirname(__file__) + '/../data/sample.txt'), 10605)
        self.assertEqual(partA(os.path.dirname(__file__) + '/../data/input.txt'), 316888)

    def testPartB(self):
        self.assertEqual(partB(os.path.dirname(__file__) + '/../data/sample.txt'), 2501150060)
        self.assertEqual(partB(os.path.dirname(__file__) + '/../data/input.txt'), 128543043840)

if __name__ == '__main__':
    unittest.main()

