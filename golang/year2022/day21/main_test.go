package day21

import (
	"testing"

	aoc "github.com/sorenisanerd/adventofcode/utils"
)

func TestDay21(t *testing.T) {
	tests := []struct {
		name     string
		f        func(string) int
		filename string
		want     int
	}{
		{"A:Sample", PartA, "sample.txt", 152},
		{"A:Input", PartA, "input.txt", 152479825094094},
		{"B:Sample", PartB, "sample.txt", 301},
		{"B:Input", PartB, "input.txt", 3360561285172},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := tt.f(aoc.GetDataFileName(tt.filename)); got != tt.want {
				t.Errorf("Got = %v, want %v", got, tt.want)
			}
		})
	}
}
