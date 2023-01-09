package utils

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestSetBasic(t *testing.T) {
	s := NewSet("", Id[string])
	assert.NotNil(t, s, "NewSet() constructor returned nil")

	s.Add("foo")
	assert.True(t, s.Contains("foo"), "Set did not contain added element")
	assert.False(t, s.Contains("bar"), "Set contained non-added element")

	s.Remove("foo")
	assert.False(t, s.Contains("foo"), "Set contained removed element")

	// Removing the same element more than once is a no-op
	s.Remove("foo")
	assert.False(t, s.Contains("foo"), "Set contained removed element")

	assert.Equal(t, s.Len(), 0, "Set contained elements")

	s.AddMany([]string{"foo", "bar", "baz"})
	assert.Equal(t, s.Len(), 3, "Set did not contain all added elements")
	assert.True(t, s.Contains("foo"), "Set did not contain added element")
	assert.True(t, s.Contains("bar"), "Set did not contain added element")
	assert.True(t, s.Contains("baz"), "Set did not contain added element")

}

func TestIntersection(t *testing.T) {
	s1 := NewSet("", Id[string]).AddMany([]string{"foo", "bar", "wibble"})
	s2 := NewSet("", Id[string]).AddMany([]string{"bar", "baz", "wibble"})
	intersection := s1.Intersection(s2)
	assert.Equal(t, intersection.Len(), 2, "Intersection did not contain any elements")
	assert.True(t, intersection.Contains("bar"), "Intersection did not contain common element")
	assert.True(t, intersection.Contains("wibble"), "Intersection did not contain common element")

}

func TestUnion(t *testing.T) {
	s1 := NewSet("", Id[string]).AddMany([]string{"foo", "bar", "wibble"})
	s2 := NewSet("", Id[string]).AddMany([]string{"bar", "baz", "wibble"})
	union := s1.Union(s2)
	assert.Equal(t, union.Len(), 4, "Union did not contain all elements")
	assert.True(t, union.Contains("foo"), "Union did not contain element")
	assert.True(t, union.Contains("bar"), "Union did not contain element")
	assert.True(t, union.Contains("baz"), "Union did not contain element")
	assert.True(t, union.Contains("wibble"), "Union did not contain common element")

}

func TestPop(t *testing.T) {
	s := NewSet("", Id[string]).AddMany([]string{"foo"})

	v, ok := s.Pop()
	assert.Equal(t, "foo", v, "Pop did not return element")
	assert.Equal(t, ok, true, "Pop did not return element")

	v, ok = s.Pop()
	assert.Equal(t, "", v, "Pop returned element even though it was supposed to be empty")
	assert.Equal(t, ok, false, "Pop did not return ok=false when it was empty")
}

func TestIsSubSet(t *testing.T) {
	s1 := NewSet("", Id[string]).AddMany([]string{"bar", "baz"})
	s2 := NewSet("", Id[string]).AddMany([]string{"foo", "bar", "baz"})
	assert.True(t, s1.IsSubSetOf(s2), "s1 was not a subset of s2")
	assert.False(t, s2.IsSubSetOf(s1), "s2 was a subset of s1")
}
