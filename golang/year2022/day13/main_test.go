package day13

import (
	"testing"

	aoc "github.com/sorenisanerd/adventofcode/utils"
)

func TestDay13(t *testing.T) {
	tests := []struct {
		name     string
		f        func(string) int
		filename string
		want     int
	}{
		{"A:Sample", PartA, "sample.txt", 13},
		{"A:Input", PartA, "input.txt", 5340},
		{"B:Sample", PartB, "sample.txt", 140},
		{"B:Input", PartB, "input.txt", 21276},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := tt.f(aoc.GetDataFileName(tt.filename)); got != tt.want {
				t.Errorf("Got = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestCmp(t *testing.T) {
	tests := []struct {
		name string
		a    string
		b    string
		want int
	}{
		{"wtf", "[[[[4],5,[2,0,0,9,3]],1],[8,[[2],[10]],2]]", "[[4,[[6,8,6,1,0]],[[7,5,8,2,3],2],[10,4]],[2,8],[],[10,10,[]],[]]", 1},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := cmp(parseLine(tt.a), parseLine(tt.b)); got != tt.want {
				t.Errorf("Got = %v, want %v", got, tt.want)
			}
		})
	}
}
