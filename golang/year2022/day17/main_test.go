package day17

import (
	"testing"

	aoc "github.com/sorenisanerd/adventofcode/utils"
)

func TestDay17(t *testing.T) {
	tests := []struct {
		name     string
		f        func(string) int
		filename string
		want     int
	}{
		{"A:Sample", PartA, "sample.txt", 3068},
		{"A:Input", PartA, "input.txt", 3186},
		{"B:Sample", PartB, "sample.txt", 1514285714288},
		{"B:Input", PartB, "input.txt", 1566376811584},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := tt.f(aoc.GetDataFileName(tt.filename)); got != tt.want {
				t.Errorf("Got = %v, want %v", got, tt.want)
			}
		})
	}
}
