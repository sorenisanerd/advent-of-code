package day10

import (
	"os"
	"strings"

	aoc "github.com/sorenisanerd/adventofcode/utils"
)

func PartA(filename string) int {
	rv := 0
	history := getHistory(filename)

	for i := 19; i < 221; i += 40 {
		rv += (i + 1) * history[i]
	}
	return rv
}

func getHistory(filename string) []int {
	history := []int{1}
	data := string(aoc.Must(os.ReadFile, filename))
	for _, line := range aoc.Map(strings.TrimSpace, strings.Split(data, "\n")) {
		if line == "noop" {
			history = append(history, aoc.GetByIdx(history, -1))
		} else if strings.HasPrefix(line, "addx") {
			curval := aoc.GetByIdx(history, -1)
			history = append(history, curval)
			curval += aoc.ExtractInts(line)[0]
			history = append(history, curval)
		}
	}
	return history
}

func PartB(filename string) string {
	rv := ""
	history := getHistory(filename)
	for i := 0; i < 240; i++ {
		if i > 0 && (i%40 == 0) {
			rv += "\n"
		}
		if aoc.Abs(history[i]-(i%40)) <= 1 {
			rv += "#"
		} else {
			rv += "."
		}
	}
	return rv
}
