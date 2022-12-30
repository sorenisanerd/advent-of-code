import os
import unittest
from .prod import partA, partB

class DayTestCase(unittest.TestCase):
    def testPartA(self):
        self.assertEqual(partA(os.path.dirname(__file__) + '/../data/sample.txt'), 110)
        self.assertEqual(partA(os.path.dirname(__file__) + '/../data/input.txt'), 4070)

    def testPartB(self):
        self.assertEqual(partB(os.path.dirname(__file__) + '/../data/sample.txt'), 20)
        self.assertEqual(partB(os.path.dirname(__file__) + '/../data/input.txt'), 881)

if __name__ == '__main__':
    unittest.main()
