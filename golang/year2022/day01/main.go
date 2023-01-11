package day01

import (
	"os"
	"sort"
	"strings"

	aoc "github.com/sorenisanerd/adventofcode/utils"
)

func PartA(filename string) int {
	data := string(aoc.Must(os.ReadFile, filename))
	sums := getSums(data)
	return getHighest(sums)
}

func PartB(filename string) int {
	data := string(aoc.Must(os.ReadFile, filename))
	sums := getSums(data)
	sort.Ints(sums)
	return sums[len(sums)-3] + sums[len(sums)-2] + sums[len(sums)-1]
}

func getHighest(sums []int) int {
	highest := 0
	for _, sum := range sums {
		if sum > highest {
			highest = sum
		}
	}
	return highest
}

func getSums(data string) []int {
	sums := []int{}
	for _, elf := range strings.Split(data, "\n\n") {
		sum := 0
		for _, i := range aoc.ExtractInts(elf) {
			sum += i
		}
		sums = append(sums, sum)
	}
	return sums
}
