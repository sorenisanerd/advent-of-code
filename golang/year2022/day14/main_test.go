package day14

import (
	"testing"

	aoc "github.com/sorenisanerd/adventofcode/utils"
)

func TestDay14(t *testing.T) {
	tests := []struct {
		name     string
		f        func(string) int
		filename string
		want     int
	}{
		{"A:Sample", PartA, "sample.txt", 24},
		{"A:Input", PartA, "input.txt", 737},
		{"B:Sample", PartB, "sample.txt", 93},
		{"B:Input", PartB, "input.txt", 28145},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := tt.f(aoc.GetDataFileName(tt.filename)); got != tt.want {
				t.Errorf("Got = %v, want %v", got, tt.want)
			}
		})
	}
}

func BenchmarkPartB(b *testing.B) {
	for i := 0; i < b.N; i++ {
		PartB(aoc.GetDataFileName("input.txt"))
	}
}
