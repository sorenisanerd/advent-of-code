import os
import unittest
try:
    from .prod import partA, partB, getAdjacentSurfaces
except ImportError:
    from prod import partA, partB, getAdjacentSurfaces

class DayTestCase(unittest.TestCase):
    def testPartA(self):
        self.assertEqual(partA(os.path.dirname(__file__) + '/../data/sample.txt'), 64)

    def testGetAdjacentSurfaces(self):
        self.assertEqual(set(getAdjacentSurfaces(0, 0, 0, 'x')),
                         set([(0, 0, 0, 'y'),
                              (0, 0, 0, 'z'),
                              (1, 0, 0, 'y'),
                              (1, 0, 0, 'z'),
                              (0, -1, 0, 'y'),
                              (0, 0, -1, 'z'),
                              (1, -1, 0, 'y'),
                              (1, 0, -1, 'z')]))

    def testPartB(self):
        self.assertEqual(partB(os.path.dirname(__file__) + '/../data/sample.txt'), 58)

if __name__ == '__main__':
    unittest.main()