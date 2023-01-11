package day15

import (
	"testing"

	aoc "github.com/sorenisanerd/adventofcode/utils"
)

func TestDay15(t *testing.T) {
	tests := []struct {
		name     string
		f        func(string) int
		filename string
		want     int
	}{
		{"A:Sample", PartA, "sample.txt", 26},
		{"A:Input", PartA, "input.txt", 4737443},
		{"B:Sample", PartB, "sample.txt", 56000011},
		{"B:Input", PartB, "input.txt", 11482462818989},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := tt.f(aoc.GetDataFileName(tt.filename)); got != tt.want {
				t.Errorf("Got = %v, want %v", got, tt.want)
			}
		})
	}
}
