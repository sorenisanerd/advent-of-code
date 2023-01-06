package day08

import (
	"fmt"
	"os"
	"strings"

	aoc "github.com/sorenisanerd/adventofcode/utils"
)

func PartA(filename string) int {
	rv := 0
	grid := parseGrid(filename)
	for p := range grid.AllPoints() {
		if isVisible(grid, p) {
			rv++
		}
	}
	return rv
}

func parseGrid(filename string) aoc.Grid[int] {
	data := string(aoc.Must(os.ReadFile, filename))
	grid := aoc.NewGrid[int](func(r rune) int { return aoc.Atoi(string(r)) })
	for _, l := range strings.Split(data, "\n") {
		grid.AddLine(l)
	}
	return grid
}

func isVisible(grid aoc.Grid[int], p aoc.V) bool {
	t := grid.Get(p)
	dim := grid.Dimensions()
	for _, d := range aoc.FourDirections {
		p_ := p
		for {
			p_ = p_.AddV(d)
			if p_[0] < 0 || p_[1] < 0 || p_[0] >= dim[0] || p_[1] >= dim[1] {
				return true
			}
			if grid.Get(p_) >= t {
				break
			}
		}
	}
	return false
}

func scenicFactor(grid aoc.Grid[int], p aoc.V, dir aoc.V) int {
	rv := 0
	t := grid.Get(p)
	for {
		p = p.AddV(dir)

		if !grid.InsideBounds(p) {
			break
		}

		rv++

		if grid.Get(p) >= t {
			break
		}
	}
	return rv
}

func PartB(filename string) int {
	rv := 0
	grid := parseGrid(filename)
	for p := range grid.AllPoints() {
		t := 1
		for _, d := range aoc.FourDirections {
			sf := scenicFactor(grid, p, d)
			fmt.Println(sf)
			t *= sf
		}
		if t > rv {
			fmt.Println(p, t)
			rv = t
		}
	}
	return rv
}
