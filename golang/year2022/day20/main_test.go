package day20

import (
	"testing"

	aoc "github.com/sorenisanerd/adventofcode/utils"
	"github.com/stretchr/testify/assert"
)

func TestDay20(t *testing.T) {
	tests := []struct {
		name     string
		f        func(string) int
		filename string
		want     int
	}{
		{"A:Sample", PartA, "sample.txt", 3},
		{"A:Input", PartA, "input.txt", 7584},
		{"B:Sample", PartB, "sample.txt", 1623178306},
		{"B:Input", PartB, "input.txt", 4907679608191},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := tt.f(aoc.GetDataFileName(tt.filename)); got != tt.want {
				t.Errorf("Got = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_calcMove(t *testing.T) {
	type args struct {
		pos  int
		val  int
		size int
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		// Initial arrangement:
		// 1, 2, -3, 3, -2, 0, 4

		// 1 moves between 2 and -3:
		// 2, 1, -3, 3, -2, 0, 4
		{"A", args{0, 1, 7}, 1},

		// 2 moves between -3 and 3:
		// 1, -3, 2, 3, -2, 0, 4
		{"B", args{0, 2, 7}, 2},

		// -3 moves between -2 and 0:
		// 1, 2, 3, -2, -3, 0, 4
		{"C", args{1, -3, 7}, 4},

		// 3 moves between 0 and 4:
		// 1, 2, -2, -3, 0, 3, 4
		{"D", args{2, 3, 7}, 5},

		// -2 moves between 4 and 1:
		// 1, 2, -3, 0, 3, 4, -2
		{"E", args{2, -2, 7}, 6},

		// 0 does not move:
		// 1, 2, -3, 0, 3, 4, -2
		{"F", args{3, 0, 7}, 3},

		// 4 moves between -3 and 0:
		// 1, 2, -3, 4, 0, 3, -2
		{"G", args{5, 4, 7}, 3},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			assert.Equal(t, tt.want, calcMove(tt.args.pos, tt.args.val, tt.args.size))
		})
	}
}
