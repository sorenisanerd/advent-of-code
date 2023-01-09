package graph

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestDijkstra(t *testing.T) {
	// Graph:
	// a - b - c - d - e - f - g
	// |   |   |   |   |
	// h   i   j   k   l - m   n
	// |                   |   |
	//  \-- (cost=10) ---- o - p

	getNeighbors := func(x string) []NeighborAndCost[string] {
		switch x {
		case "a":
			return []NeighborAndCost[string]{
				{"b", 1},
				{"h", 1},
			}
		case "h":
			return []NeighborAndCost[string]{
				{"a", 1},
				{"o", 10},
			}
		case "b":
			return []NeighborAndCost[string]{
				{"a", 1},
				{"i", 1},
				{"c", 1},
			}
		case "i":
			return []NeighborAndCost[string]{
				{"b", 1},
			}
		case "c":
			return []NeighborAndCost[string]{
				{"b", 1},
				{"j", 1},
				{"d", 1},
			}
		case "j":
			return []NeighborAndCost[string]{
				{"c", 1},
			}
		case "d":
			return []NeighborAndCost[string]{
				{"c", 1},
				{"k", 1},
				{"e", 1},
			}
		case "k":
			return []NeighborAndCost[string]{
				{"d", 1},
			}
		case "e":
			return []NeighborAndCost[string]{
				{"d", 1},
				{"f", 1},
				{"l", 1},
			}
		case "f":
			return []NeighborAndCost[string]{
				{"e", 1},
				{"g", 1},
			}
		case "g":
			return []NeighborAndCost[string]{
				{"f", 1},
			}
		case "l":
			return []NeighborAndCost[string]{
				{"e", 1},
				{"m", 1},
			}
		case "m":
			return []NeighborAndCost[string]{
				{"l", 1},
				{"o", 1},
			}
		case "o":
			return []NeighborAndCost[string]{
				{"m", 1},
				{"p", 1},
			}
		case "p":
			return []NeighborAndCost[string]{
				{"o", 1},
				{"n", 1},
			}
		case "n":
			return []NeighborAndCost[string]{
				{"p", 1},
			}
		}
		return []NeighborAndCost[string]{}
	}

	x, y := Dijkstra([]string{"a"}, "n", getNeighbors)
	assert.Equal(t, 9, x["n"])
	assert.Equal(t, "p", string(y["n"]))
	assert.Equal(t, "o", string(y["p"]))
	assert.Equal(t, "m", string(y["o"]))
	assert.Equal(t, "l", string(y["m"]))
	assert.Equal(t, "e", string(y["l"]))
	assert.Equal(t, "e", string(y["l"]))
}
