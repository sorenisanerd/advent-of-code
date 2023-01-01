import os
import unittest
from aoc.utils import get_data_file_path
from .prod import partA, partB, buildTranslationMap, getData, parseData, getNeighborDirections, getPossibleCornerEdges, getAllNeighborEdges, isCornerConcave

class DayTestCase(unittest.TestCase):
    def testPartA(self):
        self.assertEqual(partA(get_data_file_path('sample.txt')), 6032)
        self.assertEqual(partA(get_data_file_path('input.txt')), 93226)

    def testPartB(self):
        self.assertEqual(partB(get_data_file_path('sample.txt'), cubeSize=4), 5031)
        self.assertEqual(partB(get_data_file_path('input.txt')), 37415)

    def testIsCornerConcave(self):
        # Consider these four configurations:
        #
        #  0123   0123   0123   0123
        # 0....  0....  0....  0....
        # 1.##.  1..#.  1.#..  1.##.
        # 2..#.  2.##.  2.##.  2.#..
        # 3....  3....  3....  3....
        #
        # Each one has a concave (inner) and a convex (outer) corner.
        #
        # Valid regions in the first:  (1, 1), (2, 1), and (2, 2)
        # Valid regions in the second: (2, 1), (1, 2), and (2, 2)
        # Valid regions in the third:  (1, 1), (1, 2), and (2, 2)
        # Valid regions in the fourth: (1, 1), (2, 1), and (1, 2)
        #
        # Concave corners:
        # First one is comprised of (1, 2, (1, 0)) and (1, 1, (0, 1))
        # Second is comprised of    (1, 1, (1, 0)) and (1, 1, (0, 1))
        # Third is comprised of     (1, 1, (1, 0)) and (2, 1, (0, 1))
        # Fourth is comprised of    (1, 2, (1, 0)) and (2, 1, (0, 1))
        #
        # max(x1, x2), max(y1, y2)
        # First:  (1, 2) (not in regions)
        # Second: (1, 1) (not in regions)
        # Third:  (2, 1) (not in regions)
        # Fourth: (2, 2) (not in regions)

        # Convex corners corners:
        # The first one is (2, 1, (1, 0)) and (2, 0, (0, 1))
        # The second is    (2, 2, (1, 0)) and (2, 2, (0, 1))
        # The third is     (0, 2, (1, 0)) and (1, 2, (0, 1))
        # The fourth is    (0, 1, (1, 0)) and (1, 0, (0, 1))
        #
        # max(x1, x2), max(y1, y2)
        # First:  (2, 2) (in regions)
        # Second: (2, 2) (in regions)
        # Third:  (1, 2) (in regions)
        # Fourth: (1, 1) (in regions)

        regionss = [set([(1, 1), (2, 1), (2, 2)]),
                    set([(2, 1), (1, 2), (2, 2)]),
                    set([(1, 1), (1, 2), (2, 2)]),
                    set([(1, 1), (2, 1), (1, 2)])]

        concaveCorners = [frozenset([(1, 2, (1, 0)), (1, 1, (0, 1))]),
                          frozenset([(1, 1, (1, 0)), (1, 1, (0, 1))]),
                          frozenset([(1, 1, (1, 0)), (2, 1, (0, 1))]),
                          frozenset([(1, 2, (1, 0)), (2, 1, (0, 1))])]

        convexCorners = [frozenset([(2, 1, (1, 0)), (2, 0, (0, 1))]),
                         frozenset([(2, 2, (1, 0)), (2, 2, (0, 1))]),
                         frozenset([(0, 2, (1, 0)), (1, 2, (0, 1))]),
                         frozenset([(0, 1, (1, 0)), (1, 0, (0, 1))])]

        for regions, concaveCorner, convexCorner in zip(regionss, concaveCorners, convexCorners):
            edge1, edge2 = concaveCorner
            self.assertTrue(isCornerConcave(regions, *edge1, *edge2))

            edge1, edge2 = convexCorner
            self.assertFalse(isCornerConcave(regions, *edge1, *edge2))

    def testBuildTranslationMap(self):
        for f in ['sample.txt', 'sample2.txt']:
            with open(get_data_file_path(f), 'r') as fp:
                M, _, _ = parseData(fp.read())

            assert(buildTranslationMap(M, 4))

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
