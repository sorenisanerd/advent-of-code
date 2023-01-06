package utils

type Set[T comparable] map[T]bool

func NewSet[T comparable](T) Set[T] {
	return make(Set[T])
}

func (s Set[T]) Pop() (T, bool) {
	var rv T
	for k := range s {
		delete(s, k)
		return k, true
	}
	return rv, false
}

func (s Set[T]) Add(elem T) Set[T] {
	s[elem] = true
	return s
}

func (s Set[T]) Remove(elem T) Set[T] {
	delete(s, elem)
	return s
}

func (s Set[T]) AddMany(elems []T) Set[T] {
	for _, elem := range elems {
		s.Add(elem)
	}
	return s
}

func (s Set[T]) Contains(needle T) bool {
	_, ok := s[needle]
	return ok
}

func (s Set[T]) Intersection(other Set[T]) Set[T] {
	var x T
	rv := NewSet(x)
	for k := range s {
		if other.Contains(k) {
			rv.Add(k)
		}
	}
	return rv
}

func (s Set[T]) Union(other Set[T]) Set[T] {
	var x T
	rv := NewSet(x)
	for k := range s {
		rv.Add(k)
	}
	for k := range other {
		rv.Add(k)
	}
	return rv
}

func (s Set[T]) IsSubSetOf(other Set[T]) bool {
	for k := range s {
		if !other.Contains(k) {
			return false
		}
	}
	return true
}
