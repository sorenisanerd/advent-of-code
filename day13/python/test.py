import os
import unittest
from .prod import partA, partB, areInOrder

class DayTestCase(unittest.TestCase):
    def testPartA(self):
        self.assertEqual(partA(os.path.dirname(__file__) + '/../data/sample.txt'), 13)
        self.assertEqual(partA(os.path.dirname(__file__) + '/../data/input.txt'), 5340)

    def testIsInOrder(self):
        self.assertEqual(areInOrder([1], [2]), True)
        self.assertEqual(areInOrder([2], [1]), False)
        self.assertEqual(areInOrder([[2]], [[1]]), False)
        self.assertEqual(areInOrder([[2]], [[1, 3]]), False)
        self.assertEqual(areInOrder([[2]], [[2, 3]]), True)


    def testPartB(self):
        self.assertEqual(partB(os.path.dirname(__file__) + '/../data/sample.txt'), 140)
        self.assertEqual(partB(os.path.dirname(__file__) + '/../data/input.txt'), 21276)

if __name__ == '__main__':
    unittest.main()
