import os
import unittest
try:
    from .prod import partA, partB, followEdge
except ImportError:
    from prod import partA, partB, followEdge


class Day1TestCase(unittest.TestCase):
    def testPartA(self):
        self.assertEqual(partA(os.path.dirname(__file__) + '/../data/sample.txt', 10), 26)

    def testFollowEdge(self):
        self.assertEqual(list(followEdge(5, 5, 5, 7)), [(2, 5), (3, 6), (4, 7), (5, 8), (6, 7), (7, 6), (8, 5), (7, 4), (6, 3), (5, 2), (4, 3), (3, 4)])

    def testPartB(self):
        self.assertEqual(partB(os.path.dirname(__file__) + '/../data/sample.txt', 0, 0, 20, 20), 56000011)

if __name__ == '__main__':
    unittest.main()