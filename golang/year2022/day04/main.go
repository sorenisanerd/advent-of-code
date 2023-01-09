package day04

import (
	"fmt"
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

		elf1 := aoc.NewSet("", aoc.Id[string])
		for i := ints[0]; i <= ints[1]; i++ {
			elf1.Add(fmt.Sprintf("%d", i))
		}

		elf2 := aoc.NewSet("", aoc.Id[string])
		for i := ints[2]; i <= ints[3]; i++ {
			elf2.Add(fmt.Sprintf("%d", i))
		}
		if elf1.IsSubSetOf(elf2) || elf2.IsSubSetOf(elf1) {
			rvA++
		}
		if elf1.Intersection(elf2).Len() > 0 {
			rvB++
		}
	}
	return []int{rvA, rvB}
}

func PartB(filename string) int {
	return PartAB(filename)[1]
}
