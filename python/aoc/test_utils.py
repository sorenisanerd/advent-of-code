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

    def testMD(self):
        self.assertEqual(MD(V(0,0), V(0, 0)), 0)
        self.assertEqual(MD(V(50,40), V(50, 40)), 0)
        self.assertEqual(MD(V(0,0), V(1, 1)), 2)
        self.assertEqual(MD(V(0,0), V(1, 10)), 11)
        self.assertEqual(MD(V(10,5), V(87, 4)), 78)

class VectorTestCase(unittest.TestCase):
    def assertArraysEqual(self, a, b):
        assert all(a == b)

    def assertArraysNotEqual(self, a, b):
        assert not all(a == b)

    def testConstructor(self):
        V(1)
        V(1, 2)
        V(1, 2, 3)

    def testEquality(self):
        self.assertArraysEqual(V(1), V(1))
        self.assertArraysEqual(V(1, 2), V(1, 2))
        self.assertArraysEqual(V(1, 2, 3), V(1, 2, 3))

        self.assertArraysNotEqual(V(1), V(2))
        self.assertArraysNotEqual(V(1, 2), V(1, 3))
        self.assertArraysNotEqual(V(1, 2, 3), V(1, 2, 4))

    def testMultiply(self):
        self.assertArraysEqual(V(1) * 2, V(2))
        self.assertArraysEqual(V(1, 2) * 2, V(2, 4))
        self.assertArraysEqual(V(1, 2, 3) * 2, V(2, 4, 6))

    def testAdd(self):
        self.assertArraysEqual(V(1) + 2, V(3))
        self.assertArraysEqual(V(1, 2) + 2, V(3, 4))
        self.assertArraysEqual(V(1, 2, 3) + 2, V(3, 4, 5))

        self.assertArraysEqual(V(1) + V(2), V(3))
        self.assertArraysEqual(V(1, 2) + V(2, 3), V(3, 5))
        self.assertArraysEqual(V(1, 2, 3) + V(2, 3, 4), V(3, 5, 7))

    def testSlice(self):
        self.assertEqual(V(1, 2, 3)[0], 1)
        self.assertEqual(V(1, 2, 3)[1], 2)
        self.assertEqual(V(1, 2, 3)[2], 3)
        self.assertArraysEqual(V(1, 2, 3)[0:2], V(1, 2))

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

    def testGet(self):
        m = self.classUnderTest([' ', 'M'])
        self.assertEqual(m[V(0, 0)], ' ')
        self.assertEqual(m[V(0, 1)], 'M')