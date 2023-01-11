package day04

import (
	"os"
	"strings"

	aoc "github.com/sorenisanerd/adventofcode/utils"
)

func PartA(filename string) int {
	return PartAB(filename)[0]
}

func PartAB(filename string) []int {
	data := string(aoc.Must(os.ReadFile, filename))
	rvA := 0
	rvB := 0
	for _, l := range strings.Split(data, "\n") {
		if len(strings.TrimSpace(l)) < 1 {
			break
		}

		ints := aoc.ExtractInts(strings.ReplaceAll(l, "-", " "))
		if (ints[0] <= ints[2]) && (ints[2] <= ints[3]) && (ints[3] <= ints[1]) ||
			(ints[2] <= ints[0]) && (ints[0] <= ints[1]) && (ints[1] <= ints[3]) {
			rvA++
		}

		if !(ints[1] < ints[2]) && !(ints[3] < ints[0]) {
			rvB++
		}
	}
	return []int{rvA, rvB}
}

func PartB(filename string) int {
	return PartAB(filename)[1]
}
