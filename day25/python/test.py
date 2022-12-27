import os
import unittest
try:
    from .prod import partA, partB, snafuToDecimal, decimalToSnafu
except ImportError:
    from prod import partA, partB, snafuToDecimal, decimalToSnafu

class DayTestCase(unittest.TestCase):
    def testPartA(self):
        self.assertEqual(partA(os.path.dirname(__file__) + '/../data/sample.txt'), '2=-1=0')

    def testDecimalToSnafu(self):
        self.assertEqual(decimalToSnafu(1), '1')
        self.assertEqual(decimalToSnafu(2), '2')
        self.assertEqual(decimalToSnafu(3), '1=')
        self.assertEqual(decimalToSnafu(4), '1-')
        self.assertEqual(decimalToSnafu(5), '10')
        self.assertEqual(decimalToSnafu(20), '1-0')
        self.assertEqual(decimalToSnafu(25), '100')
        self.assertEqual(decimalToSnafu(5), '10')
        self.assertEqual(decimalToSnafu(2022), '1=11-2')
        self.assertEqual(decimalToSnafu(314159265), '1121-1110-1=0')

    def testSnafuToDecimal(self):
        self.assertEqual(snafuToDecimal('1'), 1)
        self.assertEqual(snafuToDecimal('2'), 2)
        self.assertEqual(snafuToDecimal('1='), 3)
        self.assertEqual(snafuToDecimal('1-'), 4)
        self.assertEqual(snafuToDecimal('10'), 5)
        self.assertEqual(snafuToDecimal('11'), 6)
        self.assertEqual(snafuToDecimal('12'), 7)
        self.assertEqual(snafuToDecimal('2='), 8)
        self.assertEqual(snafuToDecimal('2='), 8)
        self.assertEqual(snafuToDecimal('2-'), 9)
        self.assertEqual(snafuToDecimal('20'), 10)
        self.assertEqual(snafuToDecimal('1=0'), 15)
        self.assertEqual(snafuToDecimal('1-0'), 20)
        self.assertEqual(snafuToDecimal('1=11-2'), 2022)
        self.assertEqual(snafuToDecimal('1-0---0'), 12345)
        self.assertEqual(snafuToDecimal('1121-1110-1=0'), 314159265)

    def testPartB(self):
        self.assertEqual(partB(os.path.dirname(__file__) + '/../data/sample.txt'), 0)

if __name__ == '__main__':
    unittest.main()