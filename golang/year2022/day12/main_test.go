package day12

import (
	"testing"

	aoc "github.com/sorenisanerd/adventofcode/utils"
)

func TestDay12(t *testing.T) {
	tests := []struct {
		name     string
		f        func(string) int
		filename string
		want     int
	}{
		{"A:Sample", PartA, "sample.txt", 31},
		{"A:Input", PartA, "input.txt", 420},
		{"B:Sample", PartB, "sample.txt", 29},
		{"B:Input", PartB, "input.txt", 414},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := tt.f(aoc.GetDataFileName(tt.filename)); got != tt.want {
				t.Errorf("Got = %v, want %v", got, tt.want)
			}
		})
	}
}
