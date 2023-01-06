package day08

import (
	"testing"

	aoc "github.com/sorenisanerd/adventofcode/utils"
)

func TestDay08(t *testing.T) {
	tests := []struct {
		name     string
		f        func(string) int
		filename string
		want     int
	}{
		{"A:Sample", PartA, "sample.txt", 21},
		{"A:Input", PartA, "input.txt", 1812},
		{"B:Sample", PartB, "sample.txt", 8},
		{"B:Input", PartB, "input.txt", 315495},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := tt.f(aoc.GetDataFileName(tt.filename)); got != tt.want {
				t.Errorf("Got = %v, want %v", got, tt.want)
			}
		})
	}
}
