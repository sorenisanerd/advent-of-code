import os
import unittest
from .prod import partA, partB

class DayTestCase(unittest.TestCase):
    def testPartA(self):
        self.assertEqual(partA(os.path.dirname(__file__) + '/../data/sample.txt'), 24000)
        self.assertEqual(partA(os.path.dirname(__file__) + '/../data/input.txt'), 69528)

    def testPartB(self):
        self.assertEqual(partB(os.path.dirname(__file__) + '/../data/sample.txt'), 45000)
        self.assertEqual(partB(os.path.dirname(__file__) + '/../data/input.txt'), 206152)
if __name__ == '__main__':
    unittest.main()

