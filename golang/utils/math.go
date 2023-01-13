package utils

import "strconv"

// Atoi turns a string into an int,
// panicking if it fails.
func Atoi(s string) int {
	return Must(strconv.Atoi, s)
}

// Abs returns the absolute value of x.
func Abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

// Sign returns 1 for x > 0, -1 for x < 0
// and 0 for x == 0.
func Sign(x int) int {
	if x == 0 {
		return 0
	}
	return x / Abs(x)
}

// Mod returns the remainder of x/y.
// The return value is always between 0 and y, so if y is
// negative, so is the return value.
// This is the same as Python's % operator, but unlike
// Go's ditto.
//
// A few examples:
// | x  |  y | x % y (python) | x % y (Go) | Mod(x, y)
// |---------------------------------------------------
// |  1 |  1 |       0        |     0      |     0
// | -1 |  1 |       0        |     0      |     0
// | 10 |  3 |       1        |     1      |     1
// |-10 |  3 |       2        |    -1      |     2
// | 10 | -3 |      -2        |     1      |    -2
// |-10 | -3 |      -1        |    -1      |    -1
//
// The utility of this function can be seen from this
// table:
// | x  |  y | x % y (python) | x % y (Go) | Mod(x, y)
// |---------------------------------------------------
// | -5 |  3 |       1        |    -2      |     1
// | -4 |  3 |       2        |    -1      |     2
// | -3 |  3 |       0        |     0      |     0
// | -2 |  3 |       1        |    -2      |     1
// | -1 |  3 |       2        |    -1      |     2
// |  0 |  3 |       0        |     0      |     0
// |  1 |  3 |       1        |     1      |     1
// |  2 |  3 |       2        |     2      |     2
// |  3 |  3 |       0        |     0      |     0
// |  4 |  3 |       1        |     1      |     1
//
// Regardless of x's sign, we know that Mod(x, 3)
// goes 0, 1, 2, 0, 1, 2, 0, 1, 2 with no sign
// changes or surprises. This is especially handy if
// you want to use x % y as an index into a slice.
func Mod(x, y int) int {
	rv := x % y
	if rv != 0 && Sign(rv) != Sign(y) {
		rv += y
	}
	return rv
}
