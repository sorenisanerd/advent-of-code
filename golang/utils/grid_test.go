package utils

import (
	"fmt"
	"reflect"
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestGrid(t *testing.T) {
	g := NewGrid(func(r rune) int { return int(r) })
	g.AddLine("1234###abc")
	assert.Equal(t, g.Get(V2{0, 0}), 49)
	assert.Panics(t, func() { g.Get(V2{10, 10}) })
	assert.Equal(t, g.ToString(), "1234###abc")
}

func TestAllPoints(t *testing.T) {
	g := NewGrid(func(r rune) int { return int(r) })
	g.AddLine("1234")
	g.AddLine("9876")
	for p := range g.AllPoints() {
		fmt.Println(p)
		assert.True(t, g.InsideBounds(p))
	}
}

func TestStraightLine(t *testing.T) {
	type args struct {
		a V2
		b V2
	}
	tests := []struct {
		name          string
		args          args
		want          []V2
		wantException bool
	}{
		{"1", args{V2{0, 0}, V2{0, 0}}, []V2{{0, 0}}, false},
		{"2", args{V2{0, 0}, V2{1, 0}}, []V2{{0, 0}, {1, 0}}, false},
		{"3", args{V2{0, 0}, V2{0, 1}}, []V2{{0, 0}, {0, 1}}, false},
		{"4", args{V2{0, 0}, V2{1, 1}}, []V2{{0, 0}, {1, 1}}, false},
		{"4", args{V2{0, 0}, V2{2, 1}}, []V2{}, true},
		{"5", args{V2{0, 1}, V2{0, 0}}, []V2{{0, 1}, {0, 0}}, false},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			defer func() {
				if r := recover(); r != nil {
					if !tt.wantException {
						t.Errorf("StraightLine() panicked unexpectedly")
					}
				} else {
					if tt.wantException {
						t.Errorf("StraightLine() did not panic")
					}
				}
			}()
			if got := StraightLine(tt.args.a, tt.args.b); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("StraightLine() = %v, want %v", got, tt.want)
			}
		})
	}
}
