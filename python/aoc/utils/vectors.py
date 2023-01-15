class V2(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, int):
            return V2(self.x + other, self.y + other)
        return V2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        if isinstance(other, int):
            return V2(self.x - other, self.y - other)
        return V2(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if isinstance(other, int):
            return V2(self.x * other, self.y * other)
        raise Exception("Not sure what to do here")

    def __truediv__(self, other):
        return V2(self.x / other, self.y / other)

    def __floordiv__(self, other):
        return V2(self.x // other, self.y // other)

    def __eq__(self, other):
        if isinstance(other, V2):
            return self.x == other.x and self.y == other.y
        return False

    def __ne__(self, other):
        return self.x != other.x or self.y != other.y

    def __lt__(self, other):
        return self.x < other.x and self.y < other.y

    def __le__(self, other):
        return self.x <= other.x and self.y <= other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __ge__(self, other):
        return self.x >= other.x and self.y >= other.y

    def __str__(self):
        return f"V2({self.x}, {self.y})"

    def __repr__(self):
        return f"V2({self.x}, {self.y})"

    def __hash__(self):
        return hash((self.x, self.y))

    def __iter__(self):
        yield self.x
        yield self.y

    def __getitem__(self, key):
        if key == 0:
            return self.x
        elif key == 1:
            return self.y
        else:
            raise IndexError(f"V2 index out of range: {key}")

    def __setitem__(self, key, value):
        raise Exception("V2 is immutable")

    def __len__(self):
        return 2

import unittest
class TestV2(unittest.TestCase):
    def test_equality(self):
        self.assertEqual(V2(1,1), V2(1,1))
        self.assertNotEqual(V2(1,1), V2(1,2))

    def test_add_integer(self):
        self.assertEqual(V2(-5, 5) + 10, V2(5, 15))
        self.assertEqual(V2(5, -5) - 10, V2(-5, -15))

    def test_add_v2(self):
        self.assertEqual(V2(-12, 98) + V2(10, -8), V2(-2, 90))

    def test_mult_integer(self):
        self.assertEqual(V2(-3, 7) * (-2), V2(6, -14))

    def test_div_integer(self):
        self.assertEqual(V2(-3, 7) / 2, V2(-1.5, 3.5))

if __name__ == "__main__":
    import timeit
    unittest.main(exit=False, verbosity=3)
    for expr in ['V2(1,2) + V2(3,4)',
                 'V2(1,2) + 3',
                 'V2(1,2) * 3']:
        def p(number, time_taken, expr=expr):
            print(f'  Runs: {number:,}')
            print(f'  Total time: {time_taken*1000:.{5}}ms')
            print(f'  Mean time: {time_taken*1_000_000/number:.{5}}us = {time_taken*1_000_000_000/number:.{5}}ns')

        print('Benchmarking expression: ', expr)
        t = timeit.Timer(expr, setup="from __main__ import V2")
        p(*t.autorange())