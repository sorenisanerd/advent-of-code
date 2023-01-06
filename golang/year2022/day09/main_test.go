package day09

import (
	"testing"

	aoc "github.com/sorenisanerd/adventofcode/utils"
)

func TestDayXX(t *testing.T) {
	tests := []struct {
		name     string
		f        func(string) int
		filename string
		want     int
	}{
		{"A:Sample", PartA, "sample.txt", 13},
		{"A:Input", PartA, "input.txt", 6642},
		{"B:Sample", PartB, "sample.txt", 1},
		{"B:Sample", PartB, "sample2.txt", 36},
		{"B:Input", PartB, "input.txt", 2765},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := tt.f(aoc.GetDataFileName(tt.filename)); got != tt.want {
				t.Errorf("Got = %v, want %v", got, tt.want)
			}
		})
	}
}
