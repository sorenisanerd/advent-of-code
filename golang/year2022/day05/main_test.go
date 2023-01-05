package day05

import (
	"testing"

	aoc "github.com/sorenisanerd/adventofcode/utils"
)

func TestDay05(t *testing.T) {
	tests := []struct {
		name     string
		f        func(string) string
		filename string
		want     string
	}{
		{"A:Sample", PartA, "sample.txt", "CMZ"},
		{"A:Input", PartA, "input.txt", "FWSHSPJWM"},
		{"B:Sample", PartB, "sample.txt", "MCD"},
		{"B:Input", PartB, "input.txt", "PWPWHGFZS"},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := tt.f(aoc.GetDataFileName(tt.filename)); got != tt.want {
				t.Errorf("Got = %v, want %v", got, tt.want)
			}
		})
	}
}
