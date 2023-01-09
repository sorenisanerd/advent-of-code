package utils

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

// Len returns the number of elements in the set.
func (s Set[T, U]) Len() int {
	return len(s.dict)
}

// ID is a helper function that returns its argument.
// It's handy for passing to NewSet when Set[T] already
// is comparable.
func Id[T any](x T) T {
	return x
}
