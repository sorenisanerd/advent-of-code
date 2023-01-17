package day20

import (
	"os"

	"github.com/sorenisanerd/adventofcode/utils"
	aoc "github.com/sorenisanerd/adventofcode/utils"
	"golang.org/x/exp/slices"
)

func calcMove(pos, val, size int) int {
	if val == 0 {
		return pos
	} else if val > 0 {
		return (pos + val) % (size - 1)
	} else {
		p := aoc.Mod(pos+val, (size - 1))
		if p == 0 {
			return size - 1
		} else {
			return p
		}
	}
}

func PartA(filename string) int {
	return doStuff(filename, 1, 1)
}

func doStuff(filename string, iterations, key int) int {
	data := string(aoc.Must(os.ReadFile, filename))
	originalOrder := utils.Enumerate(aoc.Map(func(x int) int {
		return x * key
	}, utils.ExtractInts(data)))

	currentOrder := make([]aoc.EnumeratedSliceItem[int], len(originalOrder))
	copy(currentOrder, originalOrder)

	for iteration := 0; iteration < iterations; iteration++ {
		for i := 0; i < len(originalOrder); i++ {
			num := originalOrder[i]
			curPos := slices.Index(currentOrder, num)

			utils.Move(currentOrder, curPos, calcMove(curPos, num.Val, len(currentOrder)))
		}
	}
	idxOfZero := slices.IndexFunc(currentOrder, func(a aoc.EnumeratedSliceItem[int]) bool { return a.Val == 0 })
	getVal := func(i int) int {
		return currentOrder[i%len(currentOrder)].Val
	}
	return getVal(idxOfZero+1000) + getVal(idxOfZero+2000) + getVal(idxOfZero+3000)
}

func PartB(filename string) int {
	return doStuff(filename, 10, 811589153)
}
