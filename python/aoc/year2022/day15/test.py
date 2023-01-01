import os
import unittest
from .prod import partA, partB, followEdge

class DayTestCase(unittest.TestCase):
    def testPartA(self):
        self.assertEqual(partA(os.path.dirname(__file__) + '/../data/sample.txt', 10), 26)
        self.assertEqual(partA(os.path.dirname(__file__) + '/../data/input.txt', 2000000), 4737443)

    def testFollowEdge(self):
        self.assertEqual(list(followEdge(5, 5, 5, 7)), [(2, 5), (3, 6), (4, 7), (5, 8), (6, 7), (7, 6), (8, 5), (7, 4), (6, 3), (5, 2), (4, 3), (3, 4)])

    def testPartB(self):
        self.assertEqual(partB(os.path.dirname(__file__) + '/../data/sample.txt', 0, 0, 20, 20), 56000011)
        self.assertEqual(partB(os.path.dirname(__file__) + '/../data/input.txt', 0, 0, 4000000, 4000000), 11482462818989)

if __name__ == '__main__':
    unittest.main()
