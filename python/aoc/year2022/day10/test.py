import os
import unittest
from .prod import partA, partB

class DayTestCase(unittest.TestCase):
    def testPartA(self):
        self.assertEqual(partA(os.path.dirname(__file__) + '/../data/sample.txt'), 13140)
        self.assertEqual(partA(os.path.dirname(__file__) + '/../data/input.txt'), 14520)

    def testPartB(self):
        self.assertEqual(partB(os.path.dirname(__file__) + '/../data/sample.txt'),
                         "##..##..##..##..##..##..##..##..##..##..\n"
                         "###...###...###...###...###...###...###.\n"
                         "####....####....####....####....####....\n"
                         "#####.....#####.....#####.....#####.....\n"
                         "######......######......######......####\n"
                         "#######.......#######.......#######.....")
        self.assertEqual(partB(os.path.dirname(__file__) + '/../data/input.txt'),
                         "###..####.###...##..####.####...##.###..\n"
                         "#..#....#.#..#.#..#....#.#.......#.#..#.\n"
                         "#..#...#..###..#......#..###.....#.###..\n"
                         "###...#...#..#.#.##..#...#.......#.#..#.\n"
                         "#....#....#..#.#..#.#....#....#..#.#..#.\n"
                         "#....####.###...###.####.####..##..###..")

if __name__ == '__main__':
    unittest.main()

