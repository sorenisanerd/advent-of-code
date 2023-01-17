package utils

import (
	"fmt"
	"regexp"
	"strings"

	"golang.org/x/exp/constraints"
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

// ChunkBySliceSize splits a slice into a slice of slices,
// each of which has at most size elements.
// Every element of the original slice will be in the result.
func ChunkBySliceSize[T any](s []T, size int) [][]T {
	if size <= 0 {
		panic(fmt.Sprintf("ChunkBySliceSize(s []%T, %d) called, but size must be > 0", s[0], size))
	}
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

// ChunkByTotalCount splits a slice into a slice of count
// slices. If the slice cannot be split evenly, the last
// slice will be truncated.
func ChunkByTotalCount[T any](s []T, count int) [][]T {
	rv := make([][]T, count)
	size := len(s) / count
	if len(s)%count != 0 {
		panic(fmt.Sprintf("ChunkByTotalCount(s []%T, %d) called, but len(s) = %d, and %d %% %d = %d",
			s[0], count, len(s), len(s), count, len(s)%count))
	}
	for i := 0; i < count; i++ {
		low, high := i*size, (i+1)*size
		rv[i] = s[low:high]
	}
	return rv
}

func Min[T constraints.Ordered](e0 T, en ...T) T {
	rv := e0
	for _, ei := range en {
		if ei < rv {
			rv = ei
		}
	}
	return rv
}

func Max[T constraints.Ordered](e0 T, en ...T) T {
	rv := e0
	for _, ei := range en {
		if ei > rv {
			rv = ei
		}
	}
	return rv
}

// MaxInts returns the maximum of a list of ints.
// If the list is empty, it panics.
func MaxInts(ints ...int) int {
	if len(ints) == 0 {
		panic("no ints")
	}
	return Max(ints[0], ints[1:]...)
}

// MinInts returns the minimum of a list of ints.
// If the list is empty, it panics.
func MinInts(ints ...int) int {
	if len(ints) == 0 {
		panic("no ints")
	}
	return Min(ints[0], ints[1:]...)
}

func Bound(i, low, high int) int {
	if low > high {
		panic("low > high")
	}
	if i < low {
		return low
	}
	if i > high {
		return high
	}
	return i
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

// ChooseOne takes a slice and returns a bunch more slices!
// Given e.g. [1, 2, 3], it returns:
// [1, [2, 3]]
// [2, [1, 3]]
// [3, [1, 2]]
// It is extremely handy when doing depth first searches
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

// ChooseOneCallback is like ChooseOne, but instead of
// creating all the slices ahead of time, it calls a
// callback function with each slice as it is created.
//
// This is MUCH more efficient, but the caveat is that
// the cdr part is reused for each call, so if you need
// to keep it around, you need to copy it. Otherwise,
// you'll get weird results.
func ChooseOneCallBack[T any](l []T, f func(T, []T)) {
	if len(l) == 0 {
		return
	}
	var cdr = make([]T, len(l)-1)
	for i := 0; i < len(l); i++ {
		for j := 0; j < i; j++ {
			cdr[j] = l[j]
		}
		for j := i; j < len(l)-1; j++ {
			cdr[j] = l[j+1]
		}
		f(l[i], cdr)
	}
}

// ChooseOneGenerator is like ChooseOne, but instead of
// creating all the slices ahead of time, it launches
// a goroutine that generates the slices as they are
// consumed. The are consumed by ranging over the
// returned channel.
func ChooseOneGenerator[T any](l []T) <-chan ChooseOneTuple[T] {
	ch := make(chan ChooseOneTuple[T])
	go func(l []T, ch chan ChooseOneTuple[T]) {
		// We have two of them, so once we return one,
		// we construct the next one, ready for consumption
		// We can't just use a single one, since it would get
		// overwritten on the next iteration which happens immediately
		// after consumption and before consumption of the next.
		if len(l) > 0 {
			cdr := make([]T, len(l)-1)
			otherCdr := make([]T, len(l)-1)
			for i := 0; i < len(l); i++ {
				car := l[i]
				for j := 0; j < i; j++ {
					cdr[j] = l[j]
				}
				for j := i; j < len(l)-1; j++ {
					cdr[j] = l[j+1]
				}
				ch <- ChooseOneTuple[T]{car, cdr}
				cdr, otherCdr = otherCdr, cdr
			}
		}
		close(ch)
	}(l, ch)
	return ch
}

type EnumeratedSliceItem[T any] struct {
	Idx int
	Val T
}

func Enumerate[T any](s []T) []EnumeratedSliceItem[T] {
	rv := []EnumeratedSliceItem[T]{}
	for i, v := range s {
		rv = append(rv, EnumeratedSliceItem[T]{
			Idx: i,
			Val: v})
	}
	return rv
}

func Swap[T any](s []T, i, j int) {
	s[i], s[j] = s[j], s[i]
}

func Move[T any](s []T, from, to int) {
	if from == to {
		return
	}
	if from < to {
		for i := from; i < to; i++ {
			Swap(s, i, i+1)
		}
	} else {
		for i := from; i > to; i-- {
			Swap(s, i, i-1)
		}
	}
}
