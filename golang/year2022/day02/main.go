package day02

import (
	"os"
	"strings"

	aoc "github.com/sorenisanerd/adventofcode/utils"
)

var Hands = []string{"rock", "paper", "scissors"}

func PartA(filename string) int {
	scoreA, _ := partAB(filename)
	return scoreA
}

func PartB(filename string) int {
	_, scoreB := partAB(filename)
	return scoreB
}

func partAB(filename string) (int, int) {
	data, err := os.ReadFile(filename)
	if err != nil {
		panic(err)
	}

	scoreA := 0
	scoreB := 0

	for _, b := range strings.Split(string(data), "\n") {
		if len(strings.TrimSpace(b)) < 1 {
			break
		}

		parts := strings.Split(b, " ")
		them := strings.Index("ABC", parts[0])
		me := strings.Index("XYZ", parts[1])

		// Ties are worth 3 points
		if them == me {
			scoreA += 3
		} else if aoc.Mod(me-them, 3) == 1 {
			// me and them are indexes into [rock, paper, scissors]
			// so if me is 1 ahead of them, then me wins
			scoreA += 6
		}

		// Hand score (rock = 1, paper = 2, scissors = 3)
		scoreA += me + 1

		// Outcome score (me = 0 is lose, me = 1 is tie, me = 2 is win)
		scoreB += me * 3

		// Hand score for part B. We start with their hand,
		// and depending on `me`, we add -1, 0, or 1, to
		// get the hand that would have won, tied, or lost,
		// respectively. Then we add 1 to get the score.
		scoreB += aoc.Mod(them+[]int{-1, 0, 1}[me], 3) + 1
	}
	return scoreA, scoreB
}
