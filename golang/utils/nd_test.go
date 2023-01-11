package utils

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestVEquality(t *testing.T) {
	tests := []struct {
		v1, v2 V
		want   bool
	}{
		{V{1, 2, 3, 4, 5, 6}, V{1, 2, 3, 4, 5, 6}, true},
		{V{1, 2, 3, 4, 5, 6}, V{1, 2, 3, 4, 5, 7}, false},
		{V{1, 2, 3, 4, 5, 6}, V{1, 2, 3, 4, 5, 6, 7}, false},
	}
	for _, tt := range tests {
		assert.Equal(t, tt.want, tt.v1.Equals(tt.v2), "V.Equals(otherV) failed")
	}
}

func TestVAddInt(t *testing.T) {
	tests := []struct {
		v    V
		i    int
		want V
	}{
		{V{-5, 5, 7, 12, 33}, 10, V{5, 15, 17, 22, 43}},
		{V{5, -5, 12, 33}, -10, V{-5, -15, 2, 23}},
	}
	for _, tt := range tests {
		assert.Equal(t, tt.want, tt.v.AddInt(tt.i), "V.AddInt failed")
	}
}

func TestVAddV(t *testing.T) {
	tests := []struct {
		name      string
		v1, v2    V
		want      V
		wantPanic bool
	}{
		{"4 dimensions", V{-12, 98, 0, 1}, V{10, -8, 4, 2}, V{-2, 90, 4, 3}, false},
		{"4d + 5d", V{-12, 98, 0, 1}, V{10, -8, 4, 2, 4}, V{-2, 90, 4, 3}, true},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			defer func(wantPanic bool) {
				if r := recover(); r != nil {
					assert.True(t, wantPanic, "V.AddV should not panic")
				} else {
					assert.False(t, wantPanic, "V.AddV did not panic")
				}
			}(tt.wantPanic)
			assert.Equal(t, tt.want, tt.v1.AddV(tt.v2), "V.AddV failed")
		})
	}
}

func TestVMultInt(t *testing.T) {
	tests := []struct {
		v    V
		i    int
		want V
	}{
		{V{-3, 7, 5, 4}, -2, V{6, -14, -10, -8}},
	}
	for _, tt := range tests {
		assert.Equal(t, tt.want, tt.v.MultInt(tt.i), "V.MultInt failed")
	}
}
