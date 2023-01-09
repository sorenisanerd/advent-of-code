package graph

import (
	"fmt"

	"github.com/sorenisanerd/adventofcode/utils"
)

type equalable[T any] interface {
	Equals(T) bool
}

type NeighborAndCost[T any] struct {
	Neighbor T
	Cost     int
}

type getNeighborFunc[T any] func(T) []NeighborAndCost[T]

func Dijkstra[T any](starts []T, goal T, getNeighbors getNeighborFunc[T]) (dist map[string]int, prev map[string]T) {

	dist = make(map[string]int)
	prev = make(map[string]T)

	getDist := func(v T) int {
		if d, ok := dist[fmt.Sprint(v)]; ok {
			return d
		}
		// Somewhere in the neighborhood of infinity
		return 1 << 30
	}

	Q := utils.NewPriorityQueue(getDist)
	Q.Ascending(true)

	setDist := func(v T, d int) {
		dist[fmt.Sprint(v)] = d
	}

	for _, s := range starts {
		setDist(s, 0)
		Q.Push(s)
	}

	visited := utils.NewSet(goal, func(v T) string { return fmt.Sprint(v) })

	eq := func(a, b interface{}) bool {
		if aa, ok := a.(equalable[T]); ok {
			return aa.Equals(b.(T))
		}
		return a == b
	}

	for Q.Len() > 0 {
		vertex := Q.Pop()

		if eq(*vertex, goal) {
			return dist, prev
		}

		if visited.Contains(*vertex) {
			fmt.Println("Already visited", *vertex)
			continue
		}

		visited.Add(*vertex)

		for _, n := range getNeighbors(*vertex) {
			if !visited.Contains(n.Neighbor) {
				alt := getDist(*vertex) + n.Cost
				if alt < getDist(n.Neighbor) {
					setDist(n.Neighbor, alt)
					prev[fmt.Sprint(n.Neighbor)] = *vertex

					Q.Push(n.Neighbor)
				}
			}
		}
	}
	return dist, prev
}
