import os
import unittest
from .prod import partA, partB

class DayTestCase(unittest.TestCase):
    def testPartA(self):
        self.assertEqual(partA(os.path.dirname(__file__) + '/../data/sample.txt'), 95437)
        self.assertEqual(partA(os.path.dirname(__file__) + '/../data/input.txt'), 1611443)

    def testPartB(self):
        self.assertEqual(partB(os.path.dirname(__file__) + '/../data/sample.txt'), 24933642)
        self.assertEqual(partB(os.path.dirname(__file__) + '/../data/input.txt'), 2086088)

if __name__ == '__main__':
    unittest.main()

