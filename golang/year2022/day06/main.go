package day06

import (
	"os"
	"strings"

	aoc "github.com/sorenisanerd/adventofcode/utils"
)

func PartA(filename string) int {
	return PartAB(filename, 4)
}

func PartAB(filename string, n int) int {
	data := string(aoc.Must(os.ReadFile, filename))
	for _, l := range strings.Split(data, "\n") {
		for idx := n; idx < len(l); idx++ {
			if aoc.NewSet("", aoc.Id[string]).AddMany(strings.Split(l[idx-n:idx], "")).Len() == n {
				return idx
			}
		}
	}
	return 0
}

func PartB(filename string) int {
	return PartAB(filename, 14)
}
