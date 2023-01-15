package utils

import "github.com/google/go-cmp/cmp"

type Set[T any, U comparable] struct {
	dict   map[U]*T
	getKey func(T) U
}

// NewSet returns a new set of type T.
// The argument `t` is only used to specify the type T.
// `getKey` takes a T and returns a U, which is used as
// the key in the underlying map. It is up to the caller
// to ensure that the key is unique and consistent
// for each element.
func NewSet[T any, MapKey comparable](t T, getKey func(T) MapKey) Set[T, MapKey] {
	rv := Set[T, MapKey]{
		dict:   make(map[MapKey]*T),
		getKey: getKey,
	}
	return rv
}

func NewSetFromComparableSlice[T comparable](l []T) Set[T, T] {
	// If m is a map[whatever]T, then m[any unset key] returns the
	// nil value of T.
	rv := NewSet(make(map[int]T)[4], Id[T])
	for _, item := range l {
		rv.Add(item)
	}
	return rv
}

// Pop returns a random element from the set and `true`.
// If the set is empty, it returns the zero value of T and `false`.
func (s Set[T, U]) Pop() (T, bool) {
	var rv T
	for k := range s.dict {
		rv = *s.dict[k]
		delete(s.dict, k)
		return rv, true
	}
	return rv, false
}

// Add adds an element to the set and returns the set.
func (s Set[T, U]) Add(elem T) Set[T, U] {
	s.dict[s.getKey(elem)] = &elem
	return s
}

// Remove removes an element from the set and returns the set
func (s Set[T, U]) Remove(elem T) Set[T, U] {
	delete(s.dict, s.getKey(elem))
	return s
}

// AddMany simply adds a slice of elements to the set.
func (s Set[T, U]) AddMany(elems []T) Set[T, U] {
	for _, elem := range elems {
		s.Add(elem)
	}
	return s
}

// Contains returns true if the set contains the element.
func (s Set[T, U]) Contains(needle T) bool {
	_, ok := s.dict[s.getKey(needle)]
	return ok
}

// Intersection returns a new set containing every element
// that exists in both sets.
func (s Set[T, U]) Intersection(other Set[T, U]) Set[T, U] {
	var x T
	rv := NewSet(x, s.getKey)
	for k := range s.dict {
		if v := s.dict[k]; other.Contains(*v) {
			rv.Add(*v)
		}
	}
	return rv
}

// Union returns a new set containing every element
// that exists in either set.
func (s Set[T, U]) Union(other Set[T, U]) Set[T, U] {
	var x T
	rv := NewSet(x, s.getKey)
	for k := range s.dict {
		rv.Add(*(s.dict[k]))
	}
	for k := range other.dict {
		rv.Add(*(other.dict[k]))
	}
	return rv
}

// Union returns a new set containing every element
// that exists in either set.
func (s Set[T, U]) Subtract(other Set[T, U]) Set[T, U] {
	var x T
	rv := NewSet(x, s.getKey)
	s.Apply(func(x *T) {
		if !other.Contains(*x) {
			rv.Add(*x)
		}
	})
	return rv
}

// Equal returns true if `other` is of the same type and same
// length, and if `s` is a subset of `other`
// same length, and a subset this Set.
func (s Set[T, U]) Equal(other Set[T, U]) bool {
	return s.Len() == other.Len() && s.IsSubSetOf(other)
}

func (s Set[T, U]) List() []*T {
	rv := make([]*T, len(s.dict))
	i := 0
	for k := range s.dict {
		rv[i] = s.dict[k]
		i++
	}
	return rv
}

// IsSubSetOf returns true if every element in `s`
// is also in `other`.
func (s Set[T, U]) IsSubSetOf(other Set[T, U]) bool {
	for k := range s.dict {
		if !other.Contains(*s.dict[k]) {
			return false
		}
	}
	return true
}

// IsSuperSetOf returns true if every element in `other`
// is also in `s`. This is exactly equivalent of calling
// `other.IsSubSetOf(s)`, but it's here for symmetry.
func (s Set[T, U]) IsSuperSetOf(other Set[T, U]) bool {
	return other.IsSubSetOf(s)
}

// Len returns the number of elements in the set.
func (s Set[T, U]) Len() int {
	return len(s.dict)
}

// Apply calls a function on every element in the set.
// The function is called with a pointer to the element.
// Deleting elements from the set while iterating over it
// is safe. If an element is deleted, it will not visited.
// If it has already been visited... well, this ain't no
// time machine, so you'll need to handle that somehow.
func (s Set[T, U]) Apply(f func(*T)) {
	for k := range s.dict {
		f(s.dict[k])
	}
}

// GetTransformer returns a go-cmp.Option that makes it compare
// the contents of the underlying map instead of using Set.Equal.
//
// Use it like so:
//
//	if diff := cmp.Diff(got, want, got.GetTransformer()); diff != "" {
//		    t.Errorf("fooBarBaz() mismatch (-want +got):\n%s", diff)
//	}
//
// By default go-cmp will simply call got.Equal(want), and if that returns
// `false`, it will show a "-" before every line of the entire contents of
// `want`, and a "+" before every line of the entire contents of `got`.
// Using this transformer, it will inspect the underlying map and be able
// to pinpoint the actual differences between the two sets.
func (s Set[T, U]) GetTransformer() cmp.Option {
	return cmp.Transformer("embeddedMapOfSet", func(ss Set[T, U]) map[U]*T {
		return ss.dict
	})
}

// Id is a helper function that returns its argument.
// It's handy for passing to NewSet when Set[T] already
// is comparable.
func Id[T any](x T) T {
	return x
}
