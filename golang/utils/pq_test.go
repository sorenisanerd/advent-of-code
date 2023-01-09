package utils

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestPriorityQueue(t *testing.T) {
	pq := NewPriorityQueue(Atoi)
	pq.Ascending(false)

	pq.Push("20")
	pq.Push("30")
	pq.Push("25")
	assert.Equal(t, 3, pq.Len())
	assert.Equal(t, "30", *(pq.Pop()))
	assert.Equal(t, "25", *(pq.Pop()))
	assert.Equal(t, "20", *(pq.Pop()))

	assert.Equal(t, 0, pq.Len())

	pq.Push("20")
	pq.Push("30")
	pq.Push("25")
	pq.Ascending(true)
	assert.Equal(t, 3, pq.Len())
	assert.Equal(t, "20", *(pq.Pop()))
	assert.Equal(t, "25", *(pq.Pop()))
	assert.Equal(t, "30", *(pq.Pop()))

}
