package day18

import (
	"os"
	"strings"

	"github.com/sorenisanerd/adventofcode/utils"
)

type side struct {
	P utils.V3 // The "point"
	D string   // The direction (either x, y, or z)
}

func getAllSides(p utils.V3) []side {
	rv := []side{}

	X := map[string]utils.V3{
		"x": {-1, 0, 0},
		"y": {0, -1, 0},
		"z": {0, 0, -1},
	}

	for _, d := range []string{"x", "y", "z"} {
		rv = append(rv, side{p, d})
		rv = append(rv, side{p.AddV(X[d]), d})
	}
	return rv
}

func getBlocks(filename string) utils.Set[utils.V3, utils.V3] {
	data := string(utils.Must(os.ReadFile, filename))
	blocks := []utils.V3{}
	for _, l := range utils.SplitLines(data) {
		coords := utils.Map(utils.Atoi, strings.Split(l, ","))
		blocks = append(blocks, utils.V3{coords[0], coords[1], coords[2]})
	}
	return utils.NewSetFromComparableSlice(blocks)
}

func PartA(filename string) int {
	blocks := getBlocks(filename)
	sides := utils.NewSet(side{}, utils.Id[side])
	duplicateSides := utils.NewSet(side{}, utils.Id[side])
	blocks.Apply(func(b *utils.V3) {
		for _, s := range getAllSides(*b) {
			if sides.Contains(s) {
				duplicateSides.Add(s)
			}
			sides.Add(s)
		}
	})

	return sides.Len() - duplicateSides.Len()
}

func PartB(filename string) int {
	blocks := getBlocks(filename)
	sides := utils.NewSet(side{}, utils.Id[side])
	blocks.Apply(func(b *utils.V3) {
		sides.AddMany(getAllSides(*b))
	})

	minCoord := 0
	maxCoord := 0
	blocks.Apply(func(b *utils.V3) {
		minCoord = utils.Min(minCoord, b[0:3]...)
		maxCoord = utils.Max(maxCoord, b[0:3]...)
	})

	AlreadyVisited := utils.NewSet(utils.V3{}, utils.Id[utils.V3])
	ToVisit := utils.NewSet(utils.V3{}, utils.Id[utils.V3])
	VisibleSides := utils.NewSet(side{}, utils.Id[side])

	minCoord -= 1
	maxCoord += 1

	ToVisit.Add(utils.V3{minCoord, minCoord, minCoord})

	for ToVisit.Len() > 0 {
		p, _ := ToVisit.Pop()

		AlreadyVisited.Add(p)

		for _, d := range utils.Six3DAdjecencies {
			pp := p.AddV(d)
			if !AlreadyVisited.Contains(pp) && !blocks.Contains(pp) {
				if utils.All(utils.BoolOp(">=", minCoord), pp[:3]) &&
					utils.All(utils.BoolOp("<=", maxCoord), pp[:3]) {
					ToVisit.Add(pp)
				}
			}
		}
		VisibleSides.AddMany(getAllSides(p))
	}
	return VisibleSides.Intersection(sides).Len()
}
