package main

import "testing"

func Test_partA(t *testing.T) {
	want := 24000
	if got := partA("../python/day1/sample.txt"); got != want {
		t.Errorf("partA() = %v, want %v", got, want)
	}
}

func Test_partB(t *testing.T) {
	want := 45000
	if got := partB("../python/day1/sample.txt"); got != want {
		t.Errorf("partB() = %v, want %v", got, want)
	}
}
