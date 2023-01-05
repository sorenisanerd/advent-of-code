package utils

import "regexp"

// Extract all numbers from a string.
func ExtractInts(s string) []int {
	p := regexp.MustCompile(`-?\d+`)
	rv := []int{}
	for _, n := range p.FindAllString(s, -1) {
		rv = append(rv, Atoi(n))
	}
	return rv
}

// func Must calls a function that takes a single argument and returns
// a value and an error. If err is not nil, it panics, otherwise it
// returns the value.
func Must[OT any, IT any](f func(IT) (OT, error), arg IT) OT {
	rv, err := f(arg)
	if err != nil {
		panic(err)
	}
	return rv
}

const LowerCaseLetters = `abcdefghijklmnopqrstuvwxyz`
const UpperCaseLetters = `ABCDEFGHIJKLMNOPQRSTUVWXYZ`
const LowerAndUpperCaseLetters = LowerCaseLetters + UpperCaseLetters

func ChunkArrayBySize(s []string, size int) [][]string {
	rv := [][]string{}
	for i := 0; i < len(s); i += size {
		rv = append(rv, s[i:i+size])
	}
	return rv
}

func ChunkBySize[T string](s T, size int) []T {
	rv := []T{}
	for i := 0; i < len(s); i += size {
		rv = append(rv, s[i:i+size])
	}
	return rv
}

func ChunkByCount[T string](s T, count int) []T {
	rv := []T{}
	size := len(s) / count
	for i := 0; i < len(s); i += size {
		rv = append(rv, s[i:i+size])
	}
	return rv
}

func MaxInts(ints ...int) int {
	rv := ints[0]
	for _, i := range ints {
		if i > rv {
			rv = i
		}
	}
	return rv
}

func GetByIdx[T any](s []T, i int) T {
	if i < 0 {
		i += len(s)
	}
	return s[i]
}
