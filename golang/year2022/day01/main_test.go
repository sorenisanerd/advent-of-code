package day01

import (
	"testing"

	aoc "github.com/sorenisanerd/adventofcode/utils"
)

func Test_partA(t *testing.T) {
	tests := []struct {
		name     string
		filename string
		want     int
	}{
		{"Sample", "sample.txt", 24000},
		{"Real", "input.txt", 69528},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := PartA(aoc.GetDataFileName(tt.filename)); got != tt.want {
				t.Errorf("partA() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_partB(t *testing.T) {
	tests := []struct {
		name     string
		filename string
		want     int
	}{
		{"Sample", "sample.txt", 45000},
		{"Real", "input.txt", 206152},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := PartB(aoc.GetDataFileName(tt.filename)); got != tt.want {
				t.Errorf("partA() = %v, want %v", got, tt.want)
			}
		})
	}
}
