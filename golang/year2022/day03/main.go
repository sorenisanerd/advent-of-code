package day03

import (
	"os"
	"strings"

	aoc "github.com/sorenisanerd/adventofcode/utils"
)

func PartA(filename string) int {
	data := string(aoc.Must(os.ReadFile, filename))
	rv := 0
	for _, l := range strings.Split(data, "\n") {
		if len(strings.TrimSpace(l)) < 1 {
			break
		}
		comps := aoc.ChunkByCount(l, 2)
		s1 := aoc.NewSet("")
		s2 := aoc.NewSet("")
		for _, c := range comps[0] {
			s1.Add(string(c))
		}
		for _, c := range comps[1] {
			s2.Add(string(c))
		}
		dupe, _ := s1.Intersection(s2).Pop()
		rv += strings.Index(aoc.LowerAndUpperCaseLetters, dupe) + 1
	}
	return rv
}

func PartB(filename string) int {
	data := string(aoc.Must(os.ReadFile, filename))
	rv := 0
	for _, l := range aoc.ChunkArrayBySize(strings.Split(data, "\n"), 3) {
		dupe, _ := aoc.NewSet("").AddMany(strings.Split(l[0], "")).
			Intersection(aoc.NewSet("").AddMany(strings.Split(l[1], ""))).
			Intersection(aoc.NewSet("").AddMany(strings.Split(l[2], ""))).Pop()
		rv += strings.Index(aoc.LowerAndUpperCaseLetters, dupe) + 1
	}

	return rv
}
