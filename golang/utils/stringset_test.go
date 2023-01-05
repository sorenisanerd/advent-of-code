package utils

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestNewStringSet(t *testing.T) {
	s := NewStringSet()
	assert.NotNil(t, s, "NewStringSet() constructor returned nil")

	s.Add("foo")
	assert.True(t, s.Contains("foo"), "StringSet did not contain added element")
	assert.False(t, s.Contains("bar"), "StringSet contained non-added element")

	s.Remove("foo")
	assert.False(t, s.Contains("foo"), "StringSet contained removed element")

	// Removing the same element more than once is a no-op
	s.Remove("foo")
	assert.False(t, s.Contains("foo"), "StringSet contained removed element")

	assert.Equal(t, len(s), 0, "StringSet contained elements")

	s.AddMany([]string{"foo", "bar", "baz"})
	assert.Equal(t, len(s), 3, "StringSet did not contain all added elements")
	assert.True(t, s.Contains("foo"), "StringSet did not contain added element")
	assert.True(t, s.Contains("bar"), "StringSet did not contain added element")
	assert.True(t, s.Contains("baz"), "StringSet did not contain added element")

	s1 := NewStringSet().AddMany([]string{"foo", "bar", "wibble"})
	s2 := NewStringSet().AddMany([]string{"bar", "baz", "wibble"})
	intersection := s1.Intersection(s2)
	assert.Equal(t, len(intersection), 2, "Intersection did not contain any elements")
	assert.True(t, intersection.Contains("bar"), "Intersection did not contain common element")
	assert.True(t, intersection.Contains("wibble"), "Intersection did not contain common element")

	union := s1.Union(s2)
	assert.Equal(t, len(union), 4, "Union did not contain all elements")
	assert.True(t, union.Contains("foo"), "Union did not contain element")
	assert.True(t, union.Contains("bar"), "Union did not contain element")
	assert.True(t, union.Contains("baz"), "Union did not contain element")
	assert.True(t, union.Contains("wibble"), "Union did not contain common element")

	s = NewStringSet().AddMany([]string{"foo"})

	v, ok := s.Pop()
	assert.Equal(t, "foo", v, "Pop did not return element")
	assert.Equal(t, ok, true, "Pop did not return element")

	v, ok = s.Pop()
	assert.Equal(t, "", v, "Pop returned element even though it was supposed to be empty")
	assert.Equal(t, ok, false, "Pop did not return ok=false when it was empty")

}
