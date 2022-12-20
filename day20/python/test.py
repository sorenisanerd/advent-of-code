import os
import unittest
try:
    from .prod import partA, partB, shift
except ImportError:
    from prod import partA, partB, shift

class Day1TestCase(unittest.TestCase):
    def testPartA(self):
        self.assertEqual(partA(os.path.dirname(__file__) + '/../data/sample.txt'), 3)

    def testShift(self):
        def t(l, idx):
            l_ = list(enumerate(l))
            return [x[1] for x in shift(l_, l_[idx])]

        self.assertEqual(t([4, 5, 6, 1, 7, 8, 9], 3), [4, 5, 6, 7, 1, 8, 9])
        self.assertEqual(t([4, 5, 6, 2, 7, 8, 9], 3), [4, 5, 6, 7, 8, 2, 9])
        self.assertEqual(t([4, 5, 6, 3, 7, 8, 9], 3), [3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(t([4, 5, 6, 4, 7, 8, 9], 3), [4, 4, 5, 6, 7, 8, 9])
        self.assertEqual(t([4, -2, 5, 6, 7, 8, 9], 1), [4, 5, 6, 7, 8, -2, 9])

    def testPartB(self):
        self.assertEqual(partB(os.path.dirname(__file__) + '/../data/sample.txt'), 1623178306)

if __name__ == '__main__':
    unittest.main()