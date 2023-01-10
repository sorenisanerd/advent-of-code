package day12

import (
	"fmt"
	"os"
	"strings"

	aoc "github.com/sorenisanerd/adventofcode/utils"
	"github.com/sorenisanerd/adventofcode/utils/graph"
)

func getGrid(filename string) (aoc.Grid[int], []aoc.V, aoc.V) {
	data := string(aoc.Must(os.ReadFile, filename))
	grid := aoc.NewGrid(func(c rune) int {
		return int(strings.ReplaceAll(strings.ReplaceAll(string(c), "S", "a"), "E", "z")[0])
	})
	starts := []aoc.V{}
	goal := aoc.V{}
	for y, l := range strings.Split(data, "\n") {
		if x := strings.Index(l, "S"); x != -1 {
			starts = append(starts, aoc.V{x, y})
		}
		if x := strings.Index(l, "E"); x != -1 {
			goal = aoc.V{x, y}
		}
		grid.AddLine(l)
	}

	return grid, starts, goal
}

func getGetNeighbors(grid aoc.Grid[int]) func(aoc.V) []graph.NeighborAndCost[aoc.V] {
	return func(p aoc.V) []graph.NeighborAndCost[aoc.V] {
		cur := grid.Get(p)

		rv := []graph.NeighborAndCost[aoc.V]{}

		for _, d := range aoc.FourDirections {
			p_ := p.AddV(d)

			if grid.InsideBounds(p_) {
				if grid.Get(p_) <= cur+1 {
					rv = append(rv,
						graph.NeighborAndCost[aoc.V]{Neighbor: p_, Cost: 1})
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