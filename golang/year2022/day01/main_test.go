package day01

import (
	"testing"

	aoc "github.com/sorenisanerd/adventofcode/utils"
)

func Test_Day01(t *testing.T) {
	tests := []struct {
		name     string
		f        func(string) int
		filename string
		want     int
	}{
		{"A:Sample", PartA, "sample.txt", 24000},
		{"A:Input", PartA, "input.txt", 69528},
		{"B:Sample", PartB, "sample.txt", 45000},
		{"B:Input", PartB, "input.txt", 206152},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := tt.f(aoc.GetDataFileName(tt.filename)); got != tt.want {
				t.Errorf("Got = %v, want %v", got, tt.want)
			}
		})
	}
}
