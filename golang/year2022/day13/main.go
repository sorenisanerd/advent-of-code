package day13

import (
	"encoding/json"
	"fmt"
	"os"
	"strings"

	aoc "github.com/sorenisanerd/adventofcode/utils"
	"golang.org/x/exp/slices"
)

type num = float64

func isNum(v any) bool {
	if _, ok := v.(num); ok {
		return true
	}
	return false
}

func isSlice(v any) bool {
	if _, ok := v.([]any); ok {
		return true
	}
	return false
}

func cmp(left, right any) int {
	if isNum(left) && isNum(right) {
		if int(left.(num)) < int(right.(num)) {
			return -1
		} else if int(left.(num)) > int(right.(num)) {
			return 1
		} else {
			return 0
		}
	} else if isSlice(left) && isSlice(right) {
		if len(left.([]any)) == 0 && len(right.([]any)) == 0 {
			return 0
		} else if len(left.([]any)) == 0 && len(right.([]any)) != 0 {
			return -1
		} else if len(left.([]any)) != 0 && len(right.([]any)) == 0 {
			return 1
		} else {
			if r := cmp(left.([]any)[0], right.([]any)[0]); r != 0 {
				return r
			} else {
				return cmp(left.([]any)[1:], right.([]any)[1:])
			}
		}
	} else if isSlice(left) && isNum(right) {
		return cmp(left, []any{right.(num)})
	} else if isNum(left) && isSlice(right) {
		return cmp([]any{left.(num)}, right)
	} else {
		panic("")
	}
}

func parseLine(s string) any {
	var v any
	if err := json.Unmarshal([]byte(s), &v); err != nil {
		panic(err)
	}
	return v
}

func PartA(filename string) int {
	rv := 0
	data := string(aoc.Must(os.ReadFile, filename))
	idx := 1
	for _, lines := range aoc.ChunkBySliceSize(strings.Split(data, "\n"), 3) {
		// -1 means they are in correct order
		if r := cmp(parseLine(lines[0]), parseLine(lines[1])); r < 0 {
			rv += idx
		}
		idx++
	}
	return rv
}

func PartB(filename string) int {
	data := string(aoc.Must(os.ReadFile, filename))
	elems := make([]any, 0)
	for _, l := range strings.Split(data, "\n") {
		if l == "" {
			continue
		}
		elems = append(elems, parseLine(l))
	}
	elems = append(elems, parseLine("[[2]]"), parseLine("[[6]]"))
	slices.SortFunc(elems, func(a, b any) bool {
		return cmp(a, b) < 0
	})

	s := func(elem any) string {
		return fmt.Sprint(elem)
	}

	asStrings := aoc.Map(s, elems)
	p := slices.Index(asStrings, fmt.Sprint(parseLine("[[2]]")))
	q := slices.Index(asStrings, fmt.Sprint(parseLine("[[6]]")))
	return (p + 1) * (q + 1)
}
