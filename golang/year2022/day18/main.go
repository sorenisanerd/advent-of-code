package day18

import (
	"fmt"
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

func PartA(filename string) int {
	rv := 0
	data := string(utils.Must(os.ReadFile, filename))
	blocks := []utils.V3{}
	for _, l := range utils.SplitLines(data) {
		coords := utils.Map(utils.Atoi, strings.Split(l, ","))
		blocks = append(blocks, utils.V3{coords[0], coords[1], coords[3]})
	}
	fmt.Println(data)
	return rv
}

func PartB(filename string) int {
	rv := 0
	data := string(utils.Must(os.ReadFile, filename))
	fmt.Println(data)
	return rv
}
