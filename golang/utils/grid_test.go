package utils

import (
	"reflect"
	"strings"
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestGrid(t *testing.T) {
	g := NewDynamicGrid("r")
	g.AddRow(strings.Split("1234###abc", ""))
	assert.Equal(t, "1", g.Get(V2{0, 0}))
	assert.Panics(t, func() { g.Get(V2{10, 10}) })
	assert.Equal(t, "1234###abc", g.ToString(nil))
}

func TestDynamicGridDimensions(t *testing.T) {
	g := NewDynamicGrid("r")
	g.AddRow(strings.Split("123", ""))
	g.AddRow(strings.Split("abcdefg", ""))
	g.AddRow(strings.Split("$", ""))
	g.AddRow(strings.Split("", ""))
	assert.Equal(t, V2{3, 4}, g.Dimensions())
	assert.Equal(t, 0, g.MinX())
	assert.Equal(t, 0, g.MinY())
	assert.Equal(t, 6, g.MaxX())
	assert.Equal(t, 3, g.MaxY())
	assert.True(t, g.InsideBounds(V2{0, 0}))
	assert.False(t, g.InsideBounds(V2{-1, 0}))
	assert.False(t, g.InsideBounds(V2{0, -1}))
	assert.True(t, g.InsideBounds(V2{5, 1}))
	assert.False(t, g.InsideBounds(V2{5, 2}))

	g2 := NewDynamicGrid("r")
	assert.Equal(t, V2{0, 0}, g2.Dimensions())
	assert.Equal(t, -1, g2.MinX())
	assert.Equal(t, -1, g2.MinY())
	assert.Equal(t, -1, g2.MaxX())
	assert.Equal(t, -1, g2.MaxY())
}

func TestDynamicGridToString(t *testing.T) {
	g := NewDynamicGrid("r")
	g.AddRow(strings.Split("1234", ""))
	g.AddRow(strings.Split("1bc", ""))
	g.AddRow(strings.Split("!!!", ""))
	g.AddRow(strings.Split("", ""))
	g.AddRow(strings.Split("n", ""))
	assert.Equal(t, "1234\n1bc\n!!!\n\nn", g.ToString(nil))
}

func TestAllPoints(t *testing.T) {
	g := NewDynamicGrid("r")
	g.AddRow(strings.Split("1234", ""))
	g.AddRow(strings.Split("9876", ""))
	counter := 0
	for p := range g.AllPoints() {
		counter += 1
		assert.True(t, g.InsideBounds(p))
	}
	assert.Equal(t, 8, counter)
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
