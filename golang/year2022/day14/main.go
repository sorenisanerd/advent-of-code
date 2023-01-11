package day14

import (
	"fmt"
	"os"
	"strings"

	aoc "github.com/sorenisanerd/adventofcode/utils"
)

func PartA(filename string) int {
	M, _ := loadMap(filename)

	resting := 0
	for {
		sand := addSand(M)
		if sand[1] > 900 {
			return resting
		} else {
			M[sand] = 'o'
		}
		resting++
	}
}

func loadMap(filename string) (map[aoc.V2]rune, int) {
	data := string(aoc.Must(os.ReadFile, filename))
	M := make(map[aoc.V2]rune)
	maxy := 0
	for _, l := range strings.Split(data, "\n") {
		points := aoc.ExtractInts(l)

		cur := aoc.V2{points[0], points[1]}
		for _, p := range aoc.ChunkBySize(points[2:], 2) {
			if p[1] > maxy {
				maxy = p[1]
			}
			next := aoc.V2{p[0], p[1]}
			for _, pp := range aoc.StraightLine(cur, next) {
				M[pp] = '#'
			}
			cur = next
		}
	}
	return M, maxy
}

func printMapSection(M map[aoc.V2]rune, min, max aoc.V2) {
	for y := min[1]; y <= max[1]; y++ {
		for x := min[0]; x <= max[0]; x++ {
			if v, ok := M[aoc.V2{x, y}]; ok {
				fmt.Printf("%c", v)
			} else {
				fmt.Printf(" ")
			}
		}
		fmt.Println()
	}
}

func addSand(M map[aoc.V2]rune) aoc.V2 {
	cur := aoc.V2{500, 0}
	for {
		moved := false
		for _, d := range []aoc.V2{{0, 1}, {-1, 1}, {1, 1}} {
			next := cur.AddV(d)
			if M[next] == 0 {
				cur = next
				moved = true
				break
			}
		}
		if !moved || cur[1] > 1000 {
			return cur
		}
	}
}

func PartB(filename string) int {
	M, maxy := loadMap(filename)

	for _, pp := range aoc.StraightLine(aoc.V2{0, maxy + 2}, aoc.V2{1000, maxy + 2}) {
		M[pp] = '#'
	}

	startPos := aoc.V2{500, 0}
	resting := 0
	for {
		sand := addSand(M)
		resting++
		if sand == startPos {
			return resting
		}
		M[sand] = 'o'
	}
}
