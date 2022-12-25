import os
import unittest
try:
    from .prod import partA, partB, buildTranslationMap, getData, parseData, getNeighborDirections, getPossibleCornerEdges, getAllNeighborEdges
except ImportError:
    from prod import partA, partB, buildTranslationMap, getData, parseData, getNeighborDirections, getPossibleCornerEdges, getAllNeighborEdges

class Day1TestCase(unittest.TestCase):
    def testPartA(self):
        self.assertEqual(partA(os.path.dirname(__file__) + '/../data/sample.txt'), 6032)
        self.assertEqual(partA(os.path.dirname(__file__) + '/../data/input.txt'), 93226)

    def testPartB(self):
        self.assertEqual(partB(os.path.dirname(__file__) + '/../data/sample.txt', cubeSize=4), 5031)
        self.assertEqual(partB(os.path.dirname(__file__) + '/../data/input.txt'), 37415)

    def testGetPossibleCornerEdges(self):
        self.assertEqual(set(getPossibleCornerEdges(1, 1, (0, 1))), set([(1, 2, (1, 0)),
                                                                         (1, 1, (1, 0)),
                                                                         (0, 1, (1, 0)),
                                                                         (0, 2, (1, 0))]))

    def testGetNeighborDirections(self):
        self.assertEqual(set(getNeighborDirections(( 0,  1))), set([( 1,  1),  (-1,  1)]))
        self.assertEqual(set(getNeighborDirections(( 0, -1))), set([( 1, -1),  (-1, -1)]))
        self.assertEqual(set(getNeighborDirections(( 1,  0))), set([( 1,  1),  ( 1, -1)]))
        self.assertEqual(set(getNeighborDirections((-1,  0))), set([(-1,  1),  (-1,  -1)]))

    def testGetAllNeighborEdges(self):
        self.assertEqual(set(getAllNeighborEdges(3,  1, (0, 1))),
                         set([(2,  1, (1, 0)),
                              (2,  1, (0, 1)),
                              (2,  2, (1, 0)),
                              (3,  1, (1, 0)),
                              (3,  2, (1, 0)),
                              (4,  1, (0, 1))]))

if __name__ == '__main__':
    unittest.main()