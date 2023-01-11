package day16

import (
	"testing"

	aoc "github.com/sorenisanerd/adventofcode/utils"
)

func TestDay16(t *testing.T) {
	tests := []struct {
		name     string
		f        func(string) int
		filename string
		want     int
	}{
		{"A:Sample", PartA, "sample.txt", 1651},
		{"A:Input", PartA, "input.txt", 1701},
		{"B:Sample", PartB, "sample.txt", 1707},
		{"B:Input", PartB, "input.txt", 2455},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := tt.f(aoc.GetDataFileName(tt.filename)); got != tt.want {
				t.Errorf("Got = %v, want %v", got, tt.want)
			}
		})
	}
}
