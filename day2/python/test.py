import os
import unittest
from .prod import partA, partB, roundScore

class Day2TestCase(unittest.TestCase):
    def testRoundscore(self):
        self.assertEqual(roundScore('Rock', 'Rock'), 4)
        self.assertEqual(roundScore('Paper', 'Rock'), 1)
        self.assertEqual(roundScore('Scissors', 'Rock'), 7)
        self.assertEqual(roundScore('Rock', 'Scissors'), 3)
        self.assertEqual(roundScore('Scissors', 'Scissors'), 6)

    def testPartA(self):
        self.assertEqual(partA(os.path.dirname(__file__) + '/../data/sample.txt'), 15)

    def testPartB(self):
        self.assertEqual(partB(os.path.dirname(__file__) + '/../data/sample.txt'), 12)