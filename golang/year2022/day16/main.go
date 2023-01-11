package day16

import (
	"os"
	"regexp"
	"strconv"
	"strings"

	aoc "github.com/sorenisanerd/adventofcode/utils"
	"golang.org/x/exp/slices"
)

var lr = regexp.MustCompile(`Valve (\S+) has flow rate=(\d+); tunnels? leads? to valves? (.*)`)

type valve struct {
	name      string
	rate      int
	neighbors []string
}

var cache1 = make(map[string]int)
var cache2 = make(map[string]int)

func dfs2(V map[string]valve, curPos string, rest []string, dm DistanceMatrix[string], timeRemaining int) int {
	k := curPos + strings.Join(rest, "") + strconv.Itoa(timeRemaining)
	if v, ok := cache2[k]; ok {
		return v
	}

	if timeRemaining == 0 {
		return dfs(V, "AA", rest, dm, 26)
	}

	// How much the elephant will be able to do
	elephant := dfs(V, "AA", rest, dm, 26)

	rv := elephant

	aoc.ChooseOneCallBack(rest, func(next string, next_rest []string) {
		dist := dm.Get(curPos, next)
		if dist < (timeRemaining - 1) {
			this := (timeRemaining - dist - 1) * V[next].rate
			res := dfs2(V, next, next_rest, dm, timeRemaining-dist-1)
			if (this + res) > rv {
				rv = this + res
			}
		}
	})

	cache2[k] = rv
	return rv
}

func dfs(V map[string]valve, curPos string, rest []string, dm DistanceMatrix[string], timeRemaining int) int {
	k := curPos + strings.Join(rest, "") + strconv.Itoa(timeRemaining)
	if v, ok := cache1[k]; ok {
		return v
	}
	rv := 0

	aoc.ChooseOneCallBack(rest, func(next string, next_rest []string) {
		dist := dm.Get(curPos, next)
		if dist < (timeRemaining - 1) {
			this := (timeRemaining - dist - 1) * V[next].rate
			r := dfs(V, next, next_rest, dm, timeRemaining-dist-1)
			if (this + r) > rv {
				rv = this + r
			}
		}
	})

	cache1[k] = rv
	return rv
}

var Infinity = 999999

type DistanceMatrix[T comparable] struct {
	dists [][]int
	keys  []T
}

func NewDistanceMatrix[T comparable](keys []T) DistanceMatrix[T] {
	dm := DistanceMatrix[T]{}
	dm.keys = keys
	dm.dists = make([][]int, len(keys))
	for i := range dm.dists {
		dm.dists[i] = make([]int, len(keys))
		for j := range dm.dists[i] {
			dm.dists[i][j] = Infinity
		}
		dm.dists[i][i] = 0
	}
	return dm
}

func (dm DistanceMatrix[T]) Get(i, j T) int {
	m := slices.Index(dm.keys, i)
	n := slices.Index(dm.keys, j)
	return dm.dists[m][n]
}

func (dm DistanceMatrix[T]) Set(i, j T, dist int) {
	m := slices.Index(dm.keys, i)
	n := slices.Index(dm.keys, j)
	dm.dists[m][n] = dist
}

func Min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func FloydWarshall[T comparable](dm DistanceMatrix[T]) {
	for k := range dm.dists {
		for i := range dm.dists {
			for j := range dm.dists {
				dm.dists[i][j] = Min(dm.dists[i][j], dm.dists[i][k]+dm.dists[k][j])
			}
		}
	}
}

func PartA(filename string) int {
	data := string(aoc.Must(os.ReadFile, filename))
	valves := getValves(data)

	keys := make([]string, 0, len(valves))
	for k := range valves {
		keys = append(keys, k)
	}

	dm := NewDistanceMatrix(keys)
	for _, k := range keys {
		for _, neigh := range valves[k].neighbors {
			dm.Set(k, neigh, 1)
			dm.Set(neigh, k, 1)
		}
	}

	FloydWarshall(dm)

	return dfs(valves, "AA", aoc.Filter(func(v string) bool { return valves[v].rate > 0 }, keys), dm, 30)
}

func getValves(data string) map[string]valve {
	valves := map[string]valve{}
	for _, line := range aoc.SplitLines(data) {
		res := lr.FindStringSubmatch(line)
		if res == nil {
			panic("no match")
		}
		valves[res[1]] = valve{
			name:      res[1],
			rate:      aoc.Atoi(res[2]),
			neighbors: strings.Split(res[3], ", "),
		}
	}
	return valves
}

func PartB(filename string) int {
	data := string(aoc.Must(os.ReadFile, filename))
	valves := getValves(data)

	keys := make([]string, 0, len(valves))
	for k := range valves {
		keys = append(keys, k)
	}

	dm := NewDistanceMatrix(keys)
	for _, k := range keys {
		for _, neigh := range valves[k].neighbors {
			dm.Set(k, neigh, 1)
			dm.Set(neigh, k, 1)
		}
	}

	FloydWarshall(dm)

	return dfs2(valves, "AA",
		aoc.Filter(func(v string) bool {
			return valves[v].rate > 0
		}, keys), dm, 26)
}
