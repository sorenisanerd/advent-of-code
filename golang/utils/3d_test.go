package utils

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestV3Equality(t *testing.T) {
	tests := []struct {
		v1, v2 V3
		want   bool
	}{
		{V3{1, 1, 1}, V3{1, 1, 1}, true},
		{V3{1, 1, 1}, V3{1, 2, 1}, false},
	}
	for _, tt := range tests {
		assert.Equal(t, tt.want, tt.v1 == tt.v2, "V3 equality failed")
	}
}

func TestV3AddInt(t *testing.T) {
	tests := []struct {
		v    V3
		i    int
		want V3
	}{
		{V3{-5, 5, 7}, 10, V3{5, 15, 17}},
		{V3{5, -5, 12}, -10, V3{-5, -15, 2}},
	}
	for _, tt := range tests {
		assert.Equal(t, tt.want, tt.v.AddInt(tt.i), "V3.AddInt failed")
	}
}

func TestV3AddV(t *testing.T) {
	tests := []struct {
		v1, v2 V3
		want   V3
	}{
		{V3{-12, 98, 0}, V3{10, -8, 4}, V3{-2, 90, 4}},
	}
	for _, tt := range tests {
		assert.Equal(t, tt.want, tt.v1.AddV(tt.v2), "V3.AddV failed")
	}
}

func TestV3MultInt(t *testing.T) {
	tests := []struct {
		v    V3
		i    int
		want V3
	}{
		{V3{-3, 7, 5}, -2, V3{6, -14, -10}},
	}
	for _, tt := range tests {
		assert.Equal(t, tt.want, tt.v.MultInt(tt.i), "V3.MultInt failed")
	}
}
