import unittest

from aoc.utils import *

class UtilsTestCase(unittest.TestCase):
    def testPrefixes(self):
        self.assertEqual(list(prefixes([])), [[]])
        self.assertEqual(list(prefixes(["foo"])), [[], ["foo"]])
        self.assertEqual(list(prefixes(["foo", "bar"])), [[], ["foo"], ["foo", "bar"]])
        self.assertEqual(list(prefixes('abc')), ['', 'a', 'ab', 'abc'])
        self.assertEqual(list(prefixes(tuple('abc'))),
                         [(), ('a',), ('a', 'b'), ('a', 'b', 'c')])

    def testSign(self):
        self.assertEqual(sign(1), 1)
        self.assertEqual(sign(0), 0)
        self.assertEqual(sign(-1), -1)

    def testCmp(self):
        # a > b -> 1
        self.assertEqual(cmp(2, 1), 1)

        # a < b -> -1
        self.assertEqual(cmp(1, 2), -1)

        # a == b -> 0
        self.assertEqual(cmp(1, 1), 0)

class MapTestCase(unittest.TestCase):
    classUnderTest = Map
    def testConstructor(self):
        self.assertRaises(Exception, self.classUnderTest)
        self.classUnderTest('')
        self.classUnderTest([' ', ' '])

    def testGet(self):
        m = self.classUnderTest([' ', 'M'])
        self.assertEqual(m[V(0, 0)], ' ')
        self.assertEqual(m[V(0, 1)], 'M')
        self.assertEqual(m[V(0, 2)], OutOfBounds)
        self.assertEqual(m[V(-1, 0)], OutOfBounds)
        self.assertEqual(m[V(0, -1)], OutOfBounds)

    def testStr(self):
        m = self.classUnderTest([' ', 'M'])
        self.assertEqual(str(m), ' \nM')

    def testFind(self):
        m = self.classUnderTest([' ', 'M'])
        self.assertEqual(m.find(' '), (0, 0))
        self.assertEqual(m.find('M'), (0, 1))
        self.assertEqual(m.find('X'), None)

class SparseMapTestCase(MapTestCase):
    classUnderTest = SparseMap

    def testConstructor(self):
        self.classUnderTest('')
        self.classUnderTest([' ', ' '])

    def testGet(self):
        m = self.classUnderTest([' ', 'M'])
        self.assertEqual(m[V(0, 0)], ' ')
        self.assertEqual(m[V(0, 1)], 'M')