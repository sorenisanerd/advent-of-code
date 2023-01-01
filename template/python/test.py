import os
import unittest
try:
    from .prod import partA, partB
except ImportError:
    from prod import partA, partB

class DayTestCase(unittest.TestCase):
    def testPartA(self):
        self.assertEqual(partA(get_data_file_path('sample.txt')), 0)

    def testPartB(self):
        self.assertEqual(partB(get_data_file_path('sample.txt')), 0)

if __name__ == '__main__':
    unittest.main()