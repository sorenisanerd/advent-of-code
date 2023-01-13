package day12

import (
	"fmt"
	"os"
	"strings"

	aoc "github.com/sorenisanerd/adventofcode/utils"
	"github.com/sorenisanerd/adventofcode/utils/graph"
)

func getGrid(filename string) (aoc.DynamicGrid[int], []aoc.V2, aoc.V2) {
	data := string(aoc.Must(os.ReadFile, filename))
	grid := aoc.NewDynamicGrid(0)
	starts := []aoc.V2{}
	goal := aoc.V2{}
	for y, l := range strings.Split(data, "\n") {
		if x := strings.Index(l, "S"); x != -1 {
			starts = append(starts, aoc.V2{x, y})
		}
		if x := strings.Index(l, "E"); x != -1 {
			goal = aoc.V2{x, y}
		}
		grid.AddRow(
			aoc.Map(func(s string) int {
				return int(
					strings.ReplaceAll(
						strings.ReplaceAll(s, "S", "a"),
						"E", "z")[0])
			}, strings.Split(l, "")))
	}

	return grid, starts, goal
}

func getGetNeighbors(grid aoc.DynamicGrid[int]) func(aoc.V2) []graph.NeighborAndCost[aoc.V2] {
	return func(p aoc.V2) []graph.NeighborAndCost[aoc.V2] {
		cur := grid.Get(p)

		rv := []graph.NeighborAndCost[aoc.V2]{}

		for _, d := range aoc.FourDirections {
			p_ := p.AddV(d)

			if grid.InsideBounds(p_) {
				if grid.Get(p_) <= cur+1 {
					rv = append(rv,
						graph.NeighborAndCost[aoc.V2]{Neighbor: p_, Cost: 1})
				}
			}
		}
		return rv
	}
}

func PartA(filename string) int {
	grid, starts, goal := getGrid(filename)

	getNeighbors := getGetNeighbors(grid)

	dist, _ := graph.Dijkstra(starts, goal, getNeighbors)
	return dist[fmt.Sprint(goal)]
}

func PartB(filename string) int {
	grid, starts, goal := getGrid(filename)

	for p := range grid.AllPoints() {
		if grid.Get(p) == 'a' {
			starts = append(starts, p)
		}
	}

	getNeighbors := getGetNeighbors(grid)

	dist, _ := graph.Dijkstra(starts, goal, getNeighbors)
	return dist[fmt.Sprint(goal)]
}
