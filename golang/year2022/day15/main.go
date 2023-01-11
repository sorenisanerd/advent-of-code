package day15

import (
	"os"
	"strings"

	aoc "github.com/sorenisanerd/adventofcode/utils"
)

type V2 = aoc.V2

type sensor struct {
	self   V2
	beacon V2
	dist   int
}

func PartA(filename string) int {
	data := string(aoc.Must(os.ReadFile, filename))
	sensors := parseSensors(data)

	target_row := 10
	if len(data) > 1024 {
		target_row = 2_000_000
	}

	blocked := aoc.NewSet(1, aoc.Id[int])
	beaconsInTargetRow := aoc.NewSet(V2{0, 0}, aoc.Id[V2])
	for _, s := range sensors {
		if s.beacon[1] == target_row {
			beaconsInTargetRow.Add(s.beacon)
		}
		dist := s.self.MD(s.beacon)
		r := dist - aoc.Abs(s.self[1]-target_row)
		if r >= 0 {
			for x := s.self[0] - r; x <= s.self[0]+r; x++ {
				blocked.Add(x)
			}
		}
	}
	return blocked.Len() - beaconsInTargetRow.Len()
}

func parseSensors(data string) []sensor {
	sensors := []sensor{}
	for _, line := range strings.Split(data, "\n") {
		ints := aoc.ExtractInts(line)
		s := V2{ints[0], ints[1]}
		b := V2{ints[2], ints[3]}
		d := s.MD(b)
		sensors = append(sensors, sensor{s, b, d})
	}
	return sensors
}

func PartB(filename string) int {
	data := string(aoc.Must(os.ReadFile, filename))
	maxCoord := 4_000_000
	if len(data) < 1024 {
		maxCoord = 20
	}
	sensors := parseSensors(data)

	for _, s := range sensors {
		// This puts us at the far left corner
		// of the rombus
		startP := s.self.AddV(V2{-(s.dist + 1), 0})
		p := startP

		seq := []struct {
			dir       V2
			condition func(V2) bool
		}{
			// Northeast
			{V2{1, -1}, func(p V2) bool { return p[0] < s.self[0] }},
			// Southeast
			{V2{1, 1}, func(p V2) bool { return p[1] < s.self[1] }},
			// Southwest
			{V2{-1, 1}, func(p V2) bool { return p[0] > s.self[0] }},
			// Northwest
			{V2{-1, -1}, func(p V2) bool { return p[1] > s.self[1] }},
		}
		for _, step := range seq {
			dir := step.dir
			for step.condition(p) {

				if !(p[0] < 0 || p[1] < 0 || p[0] > maxCoord || p[1] > maxCoord) {
					blocked := false
					for _, ss := range sensors {
						if ss.self.MD(p) <= ss.dist {
							blocked = true
							break
						}
					}
					if !blocked {
						return 4_000_000*p[0] + p[1]
					}
				}
				p = p.AddV(dir)
			}
		}
	}
	return 0
}
