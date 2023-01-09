package day11

import (
	"testing"

	aoc "github.com/sorenisanerd/adventofcode/utils"
)

func TestDay11(t *testing.T) {
	tests := []struct {
		name     string
		f        func(string) int
		filename string
		want     int
	}{
		{"A:Sample", PartA, "sample.txt", 10605},
		{"A:Input", PartA, "input.txt", 316888},
		{"B:Sample", PartB, "sample.txt", 2713310158},
		{"B:Input", PartB, "input.txt", 35270398814},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := tt.f(aoc.GetDataFileName(tt.filename)); got != tt.want {
				t.Errorf("Got = %v, want %v", got, tt.want)
			}
		})
	}
}
