import os
import unittest
from .prod import partA, partB

class DayTestCase(unittest.TestCase):
    def testPartA(self):
        self.assertEqual(partA(os.path.dirname(__file__) + '/../data/sample.txt'), 10)
        self.assertEqual(partA(os.path.dirname(__file__) + '/../data/sample2.txt'), 18)
        self.assertEqual(partA(os.path.dirname(__file__) + '/../data/input.txt'), 295)

    def testPartB(self):
        self.assertEqual(partB(os.path.dirname(__file__) + '/../data/sample.txt'), 30)
        self.assertEqual(partB(os.path.dirname(__file__) + '/../data/sample2.txt'), 54)
        self.assertEqual(partB(os.path.dirname(__file__) + '/../data/input.txt'), 851)

if __name__ == '__main__':
    unittest.main()
