package utils

import "strconv"

func Atoi(s string) int {
	n, err := strconv.Atoi(s)
	if err != nil {
		panic(err)
	}
	return n
}

func Abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func Sign(x int) int {
	if x == 0 {
		return 0
	}
	return x / Abs(x)
}

func Mod(x, y int) int {
	rv := x % y
	if rv != 0 && Sign(rv) != Sign(y) {
		rv += y
	}
	return rv
}
