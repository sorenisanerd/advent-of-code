import os
import unittest
from .prod import partA, partB, parseStacks

class Day1TestCase(unittest.TestCase):
    def testPartA(self):
        self.assertEqual(partA(os.path.dirname(__file__) + '/../data/sample.txt'), 'CMZ')

    def testParseStacks(self):
        self.assertEqual(parseStacks(['    [D]    ',
                                      '[N] [C]    ',
                                      '[Z] [M] [P]',
                                      ' 1   2   3 ']), [['Z', 'N'], ['M', 'C', 'D'], ['P']])
    def testPartB(self):
        self.assertEqual(partB(os.path.dirname(__file__) + '/../data/sample.txt'), 'MCD')