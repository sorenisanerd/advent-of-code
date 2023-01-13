package day17

import (
	"fmt"
	"os"
	"strings"

	"github.com/sorenisanerd/adventofcode/utils"
)

var shapes = [][]utils.V2{
	// ####
	{{0, 0}, {1, 0}, {2, 0}, {3, 0}},
	// .#.
	// ###
	// .#.
	{{1, 0}, {0, 1}, {1, 1}, {2, 1}, {1, 2}},
	// ..#
	// ..#
	// ###
	{{0, 0}, {1, 0}, {2, 0}, {2, 1}, {2, 2}},
	// #
	// #
	// #
	// #
	{{0, 0}, {0, 1}, {0, 2}, {0, 3}},
	// ##
	// ##
	{{0, 0}, {1, 0}, {0, 1}, {1, 1}},
}

// Floor is at level -1
type Chamber [][]bool

// Get returns true if the chamber has a block at the given position
// false otherwise
func (c Chamber) Get(v utils.V2) bool {
	// Walls!
	if v[0] < 0 || v[0] >= 7 {
		return true
	}

	// Floor!
	if v[1] < 0 {
		return true
	}

	// Above top is always clear
	if v[1] >= len(c) {
		return false
	}

	// Let's have a look-see
	return c[v[1]][v[0]]
}

func (c *Chamber) Set(v utils.V2) {
	for len(*c) < v[1]+1 {
		*c = append(*c, make([]bool, 7))
	}
	(*c)[v[1]][v[0]] = true
}

var instToV2 = map[string]utils.V2{
	"<": {-1, 0},
	">": {1, 0},
}

func PartA(filename string) int {
	data := string(utils.Must(os.ReadFile, filename))
	data = strings.TrimSpace(data)

	c := Chamber{}

	instCounter := 0
	for i := 0; i < 2022; i++ {
		instCounter += doRock(&c, data, instCounter, shapes[i%len(shapes)])
	}
	return len(c)
}

func doRock(c *Chamber, instructions string, instCounter int, shape []utils.V2) int {
	savedInstCounter := instCounter
	shapePos := utils.V2{2, len(*c) + 3}
	for {
		v := instToV2[string(instructions[instCounter%len(instructions)])]
		instCounter++

		maybePos := shapePos.AddV(v)

		// If they're all clear
		if utils.All(func(p utils.V2) bool {
			return !c.Get(maybePos.AddV(p))
		}, shape) {
			shapePos = maybePos
		}

		// Move one down
		maybePos = shapePos.AddV(utils.V2{0, -1})
		if utils.All(func(p utils.V2) bool {
			return !c.Get(maybePos.AddV(p))
		}, shape) {
			shapePos = maybePos
		} else {
			for _, s := range shape {
				c.Set(s.AddV(shapePos))
			}
			break
		}
	}
	return instCounter - savedInstCounter
}

func PartB(filename string) int {
	data := string(utils.Must(os.ReadFile, filename))
	data = strings.TrimSpace(data)
	rv := 0

	c := Chamber{}

	foundPeriod := false

	lastSeenPc := -1
	possiblePeriods := make(map[string][2]int)

	instCounter := 0
	stopAt := 100000
	for i := 0; i < stopAt; i++ {
		shapeIdx := i % len(shapes)
		instCounter += doRock(&c, data, instCounter, shapes[shapeIdx])

		// If we haven't discovered the period yet
		if !foundPeriod {
			// Let's make sure we're at least a few rounds into the
			// instructions.
			if instCounter > len(data)*2 {
				// Did we just wrap around?
				if instCounter%len(data) < lastSeenPc {
					k := fmt.Sprintf("%d %d", instCounter%len(data), shapeIdx)
					// If we've seen this shapeIdx/instCounter%len(instructions)
					// tuple before, we found our period.
					if v, ok := possiblePeriods[k]; ok {
						foundPeriod = true

						// Last time we saw this combo was at v[0]
						period := i - v[0]

						// One period ago, the height was v[1]
						heightPerPeriod := len(c) - v[1]

						// The elephants wanted to know about this many rocks
						wantedRocks := 1_000_000_000_000

						// ...which is a lot more than we have...
						moreRocksNeeded := (wantedRocks - i)

						// ..there are moreRocksNeeded/period full periods from
						// i to wantedRocks, so add the height that they represent
						rv += heightPerPeriod * (moreRocksNeeded / period)

						// Keep going until we can work out the remainder using
						// the periods.
						stopAt = i + moreRocksNeeded%period
					} else {
						possiblePeriods[k] = [2]int{i, len(c)}
					}
				}
				lastSeenPc = instCounter % len(data)
			}
		}
	}
	return len(c) + rv
}
