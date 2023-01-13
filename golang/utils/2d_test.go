package utils

import (
	"fmt"
	"testing"

	"github.com/stretchr/testify/assert"
	"golang.org/x/exp/slices"
)

func TestFourDirections(t *testing.T) {
	for _, x := range []V2{V2{-1, 0}, V2{0, 1}, V2{1, 0}, V2{0, -1}} {
		t.Run(fmt.Sprint(x), func(t *testing.T) {
			if !slices.Contains(FourDirections, x) {
				t.Errorf("FourDirections does not contain %v", x)
			}
		})
	}
}

func TestEightDirections(t *testing.T) {
	dirSet := NewSet(V2{0, 0}, Id[V2])
	for _, d := range EightDirections {
		dirSet.Add(d)
	}
	assert.Equal(t, 8, dirSet.Len(), "EightDirections should have 8 directions")
	assert.False(t, dirSet.Contains(V2{0, 0}), "V{0,0} should not be in EightDirections")
}

func TestDirectionsMap(t *testing.T) {
	tests := []struct {
		name string
		want V2
	}{
		{"N", V2{0, 1}},
		{"NE", V2{1, 1}},
		{"E", V2{1, 0}},
		{"SE", V2{1, -1}},
		{"S", V2{0, -1}},
		{"SW", V2{-1, -1}},
		{"W", V2{-1, 0}},
		{"NW", V2{-1, 1}},
	}
	for _, tt := range tests {
		assert.Equal(t, tt.want, DirectionsMap[tt.name], fmt.Sprintf("Expected DirectionsMap[%v] = %v, got = %v", tt.name, tt.want, DirectionsMap[tt.name]))
	}
}

func TestV2Equality(t *testing.T) {
	tests := []struct {
		v1, v2 V2
		want   bool
	}{
		{V2{1, 1}, V2{1, 1}, true},
		{V2{1, 1}, V2{1, 2}, false},
	}
	for _, tt := range tests {
		assert.Equal(t, tt.want, tt.v1 == tt.v2, "V2 equality failed")
	}
}

func TestV2AddInt(t *testing.T) {
	tests := []struct {
		v    V2
		i    int
		want V2
	}{
		{V2{-5, 5}, 10, V2{5, 15}},
		{V2{5, -5}, -10, V2{-5, -15}},
	}
	for _, tt := range tests {
		assert.Equal(t, tt.want, tt.v.AddInt(tt.i), "V2.AddInt failed")
	}
}

func TestV2AddV(t *testing.T) {
	tests := []struct {
		v1, v2 V2
		want   V2
	}{
		{V2{-12, 98}, V2{10, -8}, V2{-2, 90}},
	}
	for _, tt := range tests {
		assert.Equal(t, tt.want, tt.v1.AddV(tt.v2), "V2.AddV failed")
	}
}

func TestV2MultInt(t *testing.T) {
	tests := []struct {
		v    V2
		i    int
		want V2
	}{
		{V2{-3, 7}, -2, V2{6, -14}},
	}
	for _, tt := range tests {
		assert.Equal(t, tt.want, tt.v.MultInt(tt.i), "V2.MultInt failed")
	}
}

func TestV2_MD(t *testing.T) {
	tests := []struct {
		name  string
		v     V2
		other V2
		want  int
	}{
		{"Self", V2{0, 0}, V2{0, 0}, 0},
		{"Horizontal", V2{15, 7}, V2{-5, 7}, 20},
		{"Vertical", V2{15, 7}, V2{15, -7}, 14},
		{"Both", V2{8, -7}, V2{14, 1}, 14},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := tt.v.MD(tt.other); got != tt.want {
				t.Errorf("V2.MD() = %v, want %v", got, tt.want)
			}
		})
	}
}
