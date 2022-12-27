import os
import unittest
try:
    from .prod import partA, partB
except ImportError:
    from prod import partA, partB

class DayTestCase(unittest.TestCase):
    def testPartA(self):
        self.assertEqual(partA(os.path.dirname(__file__) + '/../data/sample.txt'), 0)

    def testPartB(self):
        self.assertEqual(partB(os.path.dirname(__file__) + '/../data/sample.txt'), 0)

if __name__ == '__main__':
    unittest.main()