import os
import unittest
from .prod import partA, partB, whoWins

class Day2TestCase(unittest.TestCase):
    def testWhoWins(self):
        self.assertEqual(whoWins('Rock', 'Paper'), 1)
        self.assertEqual(whoWins('Rock', 'Rock'), 0)
        self.assertEqual(whoWins('Rock', 'Scissors'), -1)
        self.assertEqual(whoWins('Paper', 'Paper'), 0)
        self.assertEqual(whoWins('Paper', 'Rock'), -1)
        self.assertEqual(whoWins('Paper', 'Scissors'), 1)
        self.assertEqual(whoWins('Scissors', 'Paper'), -1)
        self.assertEqual(whoWins('Scissors', 'Rock'), 1)
        self.assertEqual(whoWins('Scissors', 'Scissors'), 0)

    def testPartA(self):
        self.assertEqual(partA(os.path.dirname(__file__) + '/../data/sample.txt'), 15)

    def testPartB(self):
        self.assertEqual(partB(os.path.dirname(__file__) + '/../data/sample.txt'), 12)