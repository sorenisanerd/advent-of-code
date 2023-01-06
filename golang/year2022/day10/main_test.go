package day10

import (
	"testing"

	aoc "github.com/sorenisanerd/adventofcode/utils"
)

func TestDay10A(t *testing.T) {
	tests := []struct {
		name     string
		f        func(string) int
		filename string
		want     int
	}{
		{"A:Sample", PartA, "sample.txt", 13140},
		{"A:Input", PartA, "input.txt", 14520},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := tt.f(aoc.GetDataFileName(tt.filename)); got != tt.want {
				t.Errorf("Got = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestDay10B(t *testing.T) {
	tests := []struct {
		name     string
		f        func(string) string
		filename string
		want     string
	}{
		{"B:Sample", PartB, "sample.txt",
			"" +
				"##..##..##..##..##..##..##..##..##..##..\n" +
				"###...###...###...###...###...###...###.\n" +
				"####....####....####....####....####....\n" +
				"#####.....#####.....#####.....#####.....\n" +
				"######......######......######......####\n" +
				"#######.......#######.......#######....."},
		{"B:Input", PartB, "input.txt",
			"" +
				"###..####.###...##..####.####...##.###..\n" +
				"#..#....#.#..#.#..#....#.#.......#.#..#.\n" +
				"#..#...#..###..#......#..###.....#.###..\n" +
				"###...#...#..#.#.##..#...#.......#.#..#.\n" +
				"#....#....#..#.#..#.#....#....#..#.#..#.\n" +
				"#....####.###...###.####.####..##..###.."},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := tt.f(aoc.GetDataFileName(tt.filename)); got != tt.want {
				t.Errorf("Got = %v, want %v", got, tt.want)
			}
		})
	}
}
