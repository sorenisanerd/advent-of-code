package utils

import (
	"strings"
)

type InOutMapFunc[T comparable] func(rune) T

type Grid[T comparable] struct {
	data     [][]T
	origData []string
	mapFunc  InOutMapFunc[T]
}

func NewGrid[T comparable](mapFunc InOutMapFunc[T]) Grid[T] {
	var rv Grid[T]
	rv.data = make([][]T, 0)
	rv.origData = make([]string, 0)
	rv.mapFunc = mapFunc
	return rv
}

func (g *Grid[T]) Get(p V2) T {
	if len(p) != 2 {
		panic("Grid only supports 2D")
	}
	return g.data[p[1]][p[0]]
}

func (g *Grid[T]) AddLine(line string) *Grid[T] {
	var row []T
	for _, c := range line {
		row = append(row, g.mapFunc(c))
	}

	g.data = append(g.data, row)
	g.origData = append(g.origData, line)

	return g
}

func (g *Grid[T]) ToString() string {
	return strings.Join(g.origData, "\n")
}

func (g *Grid[T]) Dimensions() V2 {
	return V2{len(g.data[0]), len(g.data)}
}

func (g *Grid[T]) InsideBounds(p V2) bool {
	if len(p) != 2 {
		panic("Grid only supports 2D")
	}

	dim := g.Dimensions()
	if p[0] < 0 || p[1] < 0 || p[0] >= dim[0] || p[1] >= dim[1] {
		return false
	}
	return true
}

func (g *Grid[T]) AllPoints() <-chan V2 {
	ch := make(chan V2)
	dim := g.Dimensions()
	go func(ch chan V2) {
		for y := 0; y < dim[1]; y++ {
			for x := 0; x < dim[0]; x++ {
				ch <- V2{x, y}
			}
		}
		close(ch)
	}(ch)
	return ch
}

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
