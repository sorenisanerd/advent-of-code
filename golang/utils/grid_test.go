package utils

import (
	"fmt"
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestGrid(t *testing.T) {
	g := NewGrid(func(r rune) int { return int(r) })
	g.AddLine("1234###abc")
	assert.Equal(t, g.Get(V{0, 0}), 49)
	assert.Panics(t, func() { g.Get(V{10, 10}) })
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
