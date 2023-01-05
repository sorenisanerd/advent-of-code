package day05

import (
	"os"
	"strings"

	aoc "github.com/sorenisanerd/adventofcode/utils"
)

func PartA(filename string) string {
	stackCount, stacks, moves := parseData(filename)
	for i := 0; i < len(moves); i++ {
		ints := aoc.ExtractInts(moves[i])
		count := ints[0]
		fromStack := ints[1] - 1
		toStack := ints[2] - 1
		for j := 0; j < count; j++ {
			stacks[toStack] = append(stacks[toStack], stacks[fromStack][len(stacks[fromStack])-1])
			stacks[fromStack] = stacks[fromStack][:len(stacks[fromStack])-1]
		}
	}
	rv := ""
	for i := 0; i < stackCount; i++ {
		rv += aoc.GetByIdx(stacks[i], -1)
	}
	return rv
}

func parseData(filename string) (int, [][]string, []string) {
	data := string(aoc.Must(os.ReadFile, filename))
	parts := strings.Split(data, "\n\n")
	stackData := strings.Split(parts[0], "\n")
	stackCount := aoc.GetByIdx(aoc.ExtractInts(stackData[len(stackData)-1]), -1)
	stacks := make([][]string, stackCount)
	for i := len(stackData) - 2; i >= 0; i-- {
		for j := 0; j < stackCount; j++ {
			idx := j*4 + 2

			if idx >= len(stackData[i]) {
				continue
			}

			c := stackData[i][(j*4 + 1):(j*4 + 2)]
			if c != " " {
				stacks[j] = append(stacks[j], c)
			}
		}
	}
	moves := strings.Split(parts[1], "\n")
	return stackCount, stacks, moves
}

func PartB(filename string) string {
	stackCount, stacks, moves := parseData(filename)
	for i := 0; i < len(moves); i++ {
		ints := aoc.ExtractInts(moves[i])
		count := ints[0]
		fromStack := ints[1] - 1
		toStack := ints[2] - 1

		elems := stacks[fromStack][len(stacks[fromStack])-count:]

		stacks[fromStack] = stacks[fromStack][:len(stacks[fromStack])-count]
		stacks[toStack] = append(stacks[toStack], elems...)
	}
	rv := ""
	for i := 0; i < stackCount; i++ {
		rv += aoc.GetByIdx(stacks[i], -1)
	}
	return rv
}
