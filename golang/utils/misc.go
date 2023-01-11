package utils

import (
	"regexp"
	"strings"
)

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

func SplitLines(s string) []string {
	return strings.Split(s, "\n")
}

const LowerCaseLetters = `abcdefghijklmnopqrstuvwxyz`
const UpperCaseLetters = `ABCDEFGHIJKLMNOPQRSTUVWXYZ`
const LowerAndUpperCaseLetters = LowerCaseLetters + UpperCaseLetters

func ChunkArrayBySize(s []string, size int) [][]string {
	rv := [][]string{}
	for i := 0; i < len(s); i += size {
		low, high := i, i+size
		if high > len(s) {
			high = len(s)
		}
		rv = append(rv, s[low:high])
	}
	return rv
}

func ChunkBySize[T any](s []T, size int) [][]T {
	rv := [][]T{}
	for i := 0; i < len(s); i += size {
		low, high := i, i+size
		if high > len(s) {
			high = len(s)
		}
		rv = append(rv, s[low:high])
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

func GetPrefixes[T any](s []T) [][]T {
	rv := [][]T{}
	for i := 0; i <= len(s); i++ {
		rv = append(rv, s[:i])
	}
	return rv
}

func ExampleGenerator[T any]() chan T {
	ch := make(chan T)
	go func() {
		for i := 0; i < 100; i++ {
			var v T
			ch <- v
			i++
		}
	}()
	return ch
}

func Map[T1, T2 any](f func(T1) T2, s []T1) []T2 {
	rv := []T2{}
	for _, v := range s {
		rv = append(rv, f(v))
	}
	return rv
}

func Filter[T any](f func(T) bool, s []T) []T {
	rv := []T{}
	for _, v := range s {
		if f(v) {
			rv = append(rv, v)
		}
	}
	return rv
}

func Reduce[T1, T2 any](f func(T1, T2) T1, s []T2, init T1) T1 {
	rv := init
	for _, v := range s {
		rv = f(rv, v)
	}
	return rv
}

func All[T any](f func(T) bool, s []T) bool {
	for _, v := range s {
		if !f(v) {
			return false
		}
	}
	return true
}

type ChooseOneTuple[T any] struct {
	Val  T   // car
	Rest []T // cdr
}

func ChooseOneGenerator[T any](l []T) <-chan ChooseOneTuple[T] {
	ch := make(chan ChooseOneTuple[T])
	go func(l []T, ch chan ChooseOneTuple[T]) {
		var cdr []T
		for i := 0; i < len(l); i++ {
			car := l[i]
			cdr = make([]T, len(l)-1)
			for j := 0; j < i; j++ {
				cdr[j] = l[j]
			}
			for j := i; j < len(l)-1; j++ {
				cdr[j] = l[j+1]
			}
			ch <- ChooseOneTuple[T]{car, cdr}
		}
		close(ch)
	}(l, ch)
	return ch
}

func ChooseOne[T any](l []T) []ChooseOneTuple[T] {
	rv := make([]ChooseOneTuple[T], len(l))
	for i := 0; i < len(l); i++ {
		car := l[i]
		cdr := make([]T, len(l)-1)
		for j := 0; j < i; j++ {
			cdr[j] = l[j]
		}
		for j := i; j < len(l)-1; j++ {
			cdr[j] = l[j+1]
		}
		rv[i] = ChooseOneTuple[T]{car, cdr}
	}
	return rv
}
