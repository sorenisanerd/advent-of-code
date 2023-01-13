package utils

import (
	"fmt"
	"strings"
)

// A Grid is a 2D array of values
// that can be indexed by a V2.
type Grid[T any] interface {
	// Gets the value at point given by p
	Get(V2) T
	Set(V2, T)
	InsideBounds(V2) bool
	Dimensions() V2
}

type InOutMapFunc[T comparable] func(rune) T

// DynamicGrid is a Grid that can added to
// on the fly. Rows are guaranteed to be the
// same length.
type DynamicGrid[T any] [][]T

// NewDynamicGrid creates a new DynamicGrid.
// The argument value is not used, but its
// type defines the type of the grid.
func NewDynamicGrid[T any](x T) DynamicGrid[T] {
	return DynamicGrid[T]{}
}

// Gets the value at point given by p
// Will panic if p is out of bounds.
func (dg DynamicGrid[T]) Get(p V2) T {
	return dg[p[1]][p[0]]
}

// Convenience function for adding a line of input
// to the grid.
func (dg *DynamicGrid[T]) AddRow(row []T) *DynamicGrid[T] {
	*dg = append(*dg, row)
	return dg
}

// ToString returns a string representation of the grid.
// f is called on each element of the grid to get its
// print representation.  f may be nil, in which case
// Sprintf("%v", x) is called on each element of the grid.
// In either case, only the first rune of the result is
// used.
func (dg *DynamicGrid[T]) ToString(f *func(T) rune) string {
	if f == nil {
		ff := func(x T) rune {
			return []rune(fmt.Sprintf("%v", x))[0]
		}
		f = &ff
	}
	rv := strings.Builder{}
	for y, row := range *dg {
		if y > 0 {
			rv.WriteString("\n")
		}
		for _, c := range row {
			rv.WriteRune((*f)(c))
		}
	}
	return rv.String()
}

// Dimensions returns the dimensions of the grid. Caveat:
// Since the grid is dynamic, a) the dimensions may change,
// and b) not all lines are the same length, so the width
// is the length of the FIRST line.
func (dg *DynamicGrid[T]) Dimensions() V2 {
	if len(*dg) == 0 {
		return V2{0, 0}
	}
	return V2{len((*dg)[0]), len(*dg)}
}

// InsideBounds returns true if p is defined in the grid.
// It is different from simply checking if the value is
// within {0,0} and DynamicGrid.Dimensions(), since not
// lines do not have to be the same length.
// If InsideBounds returns true, then Get(p) will not panic.
func (dg DynamicGrid[T]) InsideBounds(p V2) bool {
	if p[0] < 0 || p[1] < 0 {
		return false
	}
	if p[1] < len(dg) && p[0] < len(dg[p[1]]) {
		return true
	}
	return false
}

// MinX returns 0 if at least one row is non-empty,
// otherwise it returns -1
func (dg DynamicGrid[T]) MinX() int {
	if len(dg) == 0 {
		return -1
	}
	for _, row := range dg {
		if len(row) > 0 {
			return 0
		}
	}
	return -1
}

// MinY returns 0 if the grid is non-empty,
// otherwise it returns -1
func (dg DynamicGrid[T]) MinY() int {
	if len(dg) == 0 {
		return -1
	}
	return 0
}

// MaxX returns the column (0-indexed) of
// the longest row in the grid. If the grid
// is empty, or consists of only empty rows,
// it returns -1.
func (dg DynamicGrid[T]) MaxX() int {
	if len(dg) == 0 {
		return -1
	}
	return MaxInts(Map(func(r []T) int { return len(r) }, dg)...) - 1
}

// MaxY returns the row (0-indexed) of
// the last row in the grid. If the grid
// is empty, it returns -1.
func (dg DynamicGrid[T]) MaxY() int {
	return len(dg) - 1
}

// AllPoints returns a channel that will yield
// every defined point in the grid.
func (dg DynamicGrid[T]) AllPoints() <-chan V2 {
	ch := make(chan V2)
	go func(ch chan V2) {
		for y := 0; y < len(dg); y++ {
			for x := 0; x < len(dg[y]); x++ {
				ch <- V2{x, y}
			}
		}
		close(ch)
	}(ch)
	return ch
}

// StraightLine returns a slice of points representing
// each point on a horizontal, vertical, or 45-degree
// line between a and b, inclusive.
// If a and b do not form a line as described, this
// function will panic.
func StraightLine(a, b V2) []V2 {
	var rv []V2
	if !(a[0] == b[0] || a[1] == b[1] || Abs(a[0]-b[0]) == Abs(a[1]-b[1])) {
		panic("Not a horizontal, vertical, or perfectly diagonal line")
	}

	d := V2{Sign(b[0] - a[0]), Sign(b[1] - a[1])}
	for p := a; ; p = p.AddV(d) {
		rv = append(rv, p)
		if p == b {
			break
		}
	}
	return rv
}
