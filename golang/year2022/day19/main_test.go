package day19

import (
	"testing"

	"github.com/sorenisanerd/adventofcode/utils"
	"github.com/stretchr/testify/assert"
)

func TestDay19(t *testing.T) {
	tests := []struct {
		name     string
		f        func(string) int
		filename string
		want     int
	}{
		{"A:Sample", PartA, "sample.txt", 33},
		{"A:Input", PartA, "input.txt", 1199},
		{"B:Sample", PartB, "sample.txt", 62 * 56},
		{"B:Input", PartB, "input.txt", 3510},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := tt.f(utils.GetDataFileName(tt.filename)); got != tt.want {
				t.Errorf("Got = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_blueprint_timeNeeded(t *testing.T) {
	type fields struct {
		id        int
		robotCost []utils.V
	}
	type args struct {
		state State
	}
	tests := []struct {
		name   string
		fields fields
		args   args
		want   utils.V
	}{
		{"A", fields{0, []utils.V{
			{1, 0, 0, 0},
			{0, 1, 0, 0},
			{0, 0, 1, 0},
			{0, 0, 0, 1}}},
			args{State{
				utils.V{0, 0, 0, 0},
				utils.V{0, 0, 0, 0}}}, utils.V{10000, 10000, 10000, 10000}},
		{"B", fields{0, []utils.V{
			{1, 0, 0, 0},
			{0, 1, 0, 0},
			{0, 0, 1, 0},
			{0, 0, 0, 1}}},
			args{State{
				utils.V{1, 0, 0, 0},
				utils.V{0, 0, 0, 0}}}, utils.V{1, 10000, 10000, 10000}},
		{"C", fields{0, []utils.V{
			{1, 0, 0, 0},
			{0, 1, 0, 0},
			{0, 0, 1, 0},
			{0, 0, 0, 1}}},
			args{State{
				utils.V{1, 3, 5, 7},
				utils.V{0, 0, 0, 0}}}, utils.V{1, 1, 1, 1}},
		{"D", fields{0, []utils.V{
			{1, 0, 0, 0},
			{0, 1, 0, 0},
			{0, 0, 1, 0},
			{0, 0, 0, 1}}},
			args{State{
				utils.V{1, 3, 5, 7},
				utils.V{1, 1, 1, 1}}}, utils.V{0, 0, 0, 0}},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			bp := blueprint{
				id:        tt.fields.id,
				robotCost: tt.fields.robotCost,
			}
			assert.Equal(t, tt.want, bp.timeNeeded(tt.args.state))
		})
	}
}
