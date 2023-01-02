import unittest

from aoc.utils import *

class UtilsTestCase(unittest.TestCase):
    def testPrefixes(self):
        self.assertEqual(list(prefixes('abc')), ['', 'a', 'ab', 'abc'])
        self.assertEqual(list(prefixes(tuple('abc'))),
                         [(), ('a',), ('a', 'b'), ('a', 'b', 'c')])