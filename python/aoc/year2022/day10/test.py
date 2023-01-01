import os
import unittest
from aoc.utils import get_data_file_path
from .prod import partA, partB

class DayTestCase(unittest.TestCase):
    def testPartA(self):
        self.assertEqual(partA(get_data_file_path('sample.txt')), 13140)
        self.assertEqual(partA(get_data_file_path('input.txt')), 14520)

    def testPartB(self):
        self.assertEqual(partB(get_data_file_path('sample.txt')),
                         "##..##..##..##..##..##..##..##..##..##..\n"
                         "###...###...###...###...###...###...###.\n"
                         "####....####....####....####....####....\n"
                         "#####.....#####.....#####.....#####.....\n"
                         "######......######......######......####\n"
                         "#######.......#######.......#######.....")
        self.assertEqual(partB(get_data_file_path('input.txt')),
                         "###..####.###...##..####.####...##.###..\n"
                         "#..#....#.#..#.#..#....#.#.......#.#..#.\n"
                         "#..#...#..###..#......#..###.....#.###..\n"
                         "###...#...#..#.#.##..#...#.......#.#..#.\n"
                         "#....#....#..#.#..#.#....#....#..#.#..#.\n"
                         "#....####.###...###.####.####..##..###..")

if __name__ == '__main__':
    unittest.main()

