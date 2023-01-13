package utils

import (
	"testing"
)

func testForPanic(t *testing.T, s string, wantPanic, didPanic bool) {
	if didPanic != wantPanic {
		var s string
		if didPanic {
			t.Errorf("%s panicked, which we did NOT expect it to", s)
		} else {
			t.Errorf("%s did not panic, but we expected it to", s)
		}
	}
}

func TestAtoi(t *testing.T) {
	tests := []struct {
		name      string
		want      int
		wantPanic bool
	}{
		{"0", 0, false},
		{"-1", -1, false},
		{"ab", 0, true},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			defer func() {
				testForPanic(t, tt.name, tt.wantPanic, recover() != nil)
			}()
			if got := Atoi(tt.name); got != tt.want {
				t.Errorf("Atoi() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestAbs(t *testing.T) {
	tests := []struct {
		name string
		arg  int
		want int
	}{
		{"0", 0, 0},
		{"234", 234, 234},
		{"-1234", -1234, 1234},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := Abs(tt.arg); got != tt.want {
				t.Errorf("Abs() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestSign(t *testing.T) {
	tests := []struct {
		name string
		arg  int
		want int
	}{
		{"0", 0, 0},
		{"-1", -1, -1},
		{"-123", -123, -1},
		{"1234", 1234, 1},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := Sign(tt.arg); got != tt.want {
				t.Errorf("Sign() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestMod(t *testing.T) {
	tests := []struct {
		name      string
		want      int
		wantPanic bool
	}{
		{"1 % 1", 0, false},
		{"-1 % 1", 0, false},
		{" 10 % 3", 1, false},
		{"-10 % 3", 2, false},
		{"10 % -3", -2, false},
		{"-4 % 3", 2, false},
		{"-3 % 3", 0, false},
		{"-2 % 3", 1, false},
		{"-1 % 3", 2, false},
		{" 0 % 3", 0, false},
		{" 1 % 3", 1, false},
		{" 2 % 3", 2, false},
		{" 3 % 3", 0, false},
		{" 4 % 3", 1, false},
		{"0 % 0", -1, true},
		{"0 % 0", -1, true},
		{"-1 % 0", -1, true},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			defer func() {
				testForPanic(t, tt.name, tt.wantPanic, recover() != nil)
			}()
			ints := ExtractInts(tt.name)
			if got := Mod(ints[0], ints[1]); got != tt.want {
				t.Errorf("Mod() = %v, want %v", got, tt.want)
			}
		})
	}
}
