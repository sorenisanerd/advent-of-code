package utils

type StringSet map[string]bool

func NewStringSet() StringSet {
	return make(StringSet)
}

func (s StringSet) Pop() (string, bool) {
	for k := range s {
		delete(s, k)
		return k, true
	}
	return "", false
}

func (s StringSet) Add(elem string) StringSet {
	s[elem] = true
	return s
}

func (s StringSet) Remove(elem string) StringSet {
	delete(s, elem)
	return s
}

func (s StringSet) AddMany(elems []string) StringSet {
	for _, elem := range elems {
		s.Add(elem)
	}
	return s
}

func (s StringSet) Contains(needle string) bool {
	_, ok := s[needle]
	return ok
}

func (s StringSet) Intersection(other StringSet) StringSet {
	rv := NewStringSet()
	for k := range s {
		if other.Contains(k) {
			rv.Add(k)
		}
	}
	return rv
}

func (s StringSet) Union(other StringSet) StringSet {
	rv := NewStringSet()
	for k := range s {
		rv.Add(k)
	}
	for k := range other {
		rv.Add(k)
	}
	return rv
}

func (s StringSet) IsSubsetOf(other StringSet) bool {
	for k := range s {
		if !other.Contains(k) {
			return false
		}
	}
	return true
}
