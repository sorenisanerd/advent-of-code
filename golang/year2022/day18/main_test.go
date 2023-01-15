package day18

import (
	"testing"

	"github.com/google/go-cmp/cmp"
	"github.com/sorenisanerd/adventofcode/utils"
)

func testDay18(t *testing.T) {
	tests := []struct {
		name     string
		f        func(string) int
		filename string
		want     int
	}{
		{"A:Sample", PartA, "sample.txt", 0},
		{"A:Input", PartA, "input.txt", 0},
		{"B:Sample", PartB, "sample.txt", 0},
		{"B:Input", PartB, "input.txt", 0},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := tt.f(utils.GetDataFileName(tt.filename)); got != tt.want {
				t.Errorf("Got = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_getAllSides(t *testing.T) {
	tests := []struct {
		name string
		p    utils.V3
		want []side
	}{
		{"Easy peasy", utils.V3{0, 0, 0},
			[]side{
				{utils.V3{0, 0, 0}, "x"},
				{utils.V3{-1, 0, 0}, "x"},

				{utils.V3{0, 0, 0}, "y"},
				{utils.V3{0, -1, 0}, "y"},

				{utils.V3{0, 0, 0}, "z"},
				{utils.V3{0, 0, -1}, "z"}}},
		{"Also easy", utils.V3{-2, -3, -4}, []side{
			{utils.V3{-2, -3, -4}, "x"},
			{utils.V3{-3, -3, -4}, "x"},

			{utils.V3{-2, -3, -4}, "y"},
			{utils.V3{-2, -4, -4}, "y"},

			{utils.V3{-2, -3, -4}, "z"},
			{utils.V3{-2, -3, -5}, "z"},
		}},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := utils.NewSetFromComparableSlice(getAllSides(tt.p))
			want := utils.NewSetFromComparableSlice(tt.want)

			if diff := cmp.Diff(want, got, got.GetTransformer()); diff != "" {
				t.Errorf("getAllSides() mismatch (-want +got):\n%s", diff)
			}
		})
	}
}
