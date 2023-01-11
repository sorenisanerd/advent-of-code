package utils

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

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
