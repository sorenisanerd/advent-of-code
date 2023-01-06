package day09

import (
	"fmt"
	"os"
	"strings"

	aoc "github.com/sorenisanerd/adventofcode/utils"
)

type V = aoc.V

type move struct {
	dir   string
	count int
}

var moveDir = map[string]V{
	"R": {1, 0},
	"L": {-1, 0},
	"D": {0, 1},
	"U": {0, -1}}

func PartA(filename string) int {
	return PartAB(filename, 2)
}

func PartAB(filename string, knotCount int) int {
	var moves []move
	data := string(aoc.Must(os.ReadFile, filename))
	for _, line := range strings.Split(data, "\n") {
		parts := strings.Split(line, " ")
		dir, count := parts[0], aoc.Atoi(parts[1])
		moves = append(moves, move{dir, count})
	}

	knots := []aoc.V{}
	for i := 0; i < knotCount; i++ {
		knots = append(knots, aoc.V{0, 0})
	}

	moveFunc := func(p aoc.V, move string) aoc.V {
		return p.AddV(moveDir[move])
	}
	trackFunc := func(head, tail aoc.V) aoc.V {
		if aoc.Abs(head[0]-tail[0]) > 1 || aoc.Abs(head[1]-tail[1]) > 1 {
			return tail.AddV(aoc.V{aoc.Sign(head[0] - tail[0]), aoc.Sign(head[1] - tail[1])})
		}
		return tail
	}

	seenPositions := aoc.NewSet("")
	seenPositions.Add(fmt.Sprintf("%v", aoc.V{0, 0}))
	for _, move := range moves {
		for i := 0; i < move.count; i++ {
			knots[0] = moveFunc(knots[0], move.dir)
			for j := 1; j < knotCount; j++ {
				knots[j] = trackFunc(knots[j-1], knots[j])
			}
			seenPositions.Add(fmt.Sprintf("%v", aoc.GetByIdx(knots, -1)))
		}
	}
	return len(seenPositions)
}

func PartB(filename string) int {
	return PartAB(filename, 10)
}
