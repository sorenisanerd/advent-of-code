import os
import unittest
from .prod import partA, partB

class DayTestCase(unittest.TestCase):
    def testPartA(self):
        self.assertEqual(partA(os.path.dirname(__file__) + '/../data/sample.txt'), 152)
        self.assertEqual(partA(os.path.dirname(__file__) + '/../data/input.txt'), 152479825094094)

    def testPartB(self):
        self.assertEqual(partB(os.path.dirname(__file__) + '/../data/sample.txt'), 301)
        self.assertEqual(partB(os.path.dirname(__file__) + '/../data/input.txt'), 3360561285172)

if __name__ == '__main__':
    unittest.main()
