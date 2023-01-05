package day06

import (
	"testing"

	aoc "github.com/sorenisanerd/adventofcode/utils"
)

func TestDay06(t *testing.T) {
	tests := []struct {
		name     string
		f        func(string) int
		filename string
		want     int
	}{
		{"A:Sample", PartA, "sample.txt", 95437},
		{"A:Input", PartA, "input.txt", 1611443},
		{"B:Sample", PartB, "sample.txt", 24833642},
		{"B:Input", PartB, "input.txt", 2086088},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := tt.f(aoc.GetDataFileName(tt.filename)); got != tt.want {
				t.Errorf("Got = %v, want %v", got, tt.want)
			}
		})
	}
}
