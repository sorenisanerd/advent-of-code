package day07

import (
	"os"
	"strings"

	aoc "github.com/sorenisanerd/adventofcode/utils"
)

func PartA(filename string) int {
	var rv = 0
	dirSizes := getDirSizes(filename)
	for k := range dirSizes {
		if dirSizes[k] <= 100000 {
			rv += dirSizes[k]
		}
	}
	return rv
}

func getDirSizes(filename string) map[string]int {
	data := string(aoc.Must(os.ReadFile, filename))
	dirSizes := make(map[string]int)
	curDir := []string{}
	for _, l := range strings.Split(data, "\n") {
		if strings.HasPrefix(l, "$ cd /") {
			curDir = []string{}
		} else if strings.HasPrefix(l, "$ cd ..") {
			curDir = curDir[:len(curDir)-1]
		} else if strings.HasPrefix(l, "$ cd") {
			curDir = append(curDir, aoc.GetByIdx(strings.Split(l, " "), -1))
		} else if !strings.HasPrefix(l, "$") {
			if strings.HasPrefix(l, "dir") {
				continue
			}
			for _, p := range aoc.GetPrefixes(curDir) {
				key := strings.Join(p, "/")
				if _, ok := dirSizes[key]; !ok {
					dirSizes[key] = 0
				}
				dirSizes[key] += aoc.ExtractInts(l)[0]
			}
		}
	}
	return dirSizes
}

func PartB(filename string) int {
	var rv = 1000000000000000
	dirSizes := getDirSizes(filename)
	total_capacity := 70_000_000
	available_capacity := total_capacity - dirSizes[""]
	need_to_clear := 30_000_000 - available_capacity
	for k := range dirSizes {
		if dirSizes[k] >= need_to_clear {
			if dirSizes[k] < rv {
				rv = dirSizes[k]
			}
		}
	}
	return rv
}
