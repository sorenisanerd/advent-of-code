package utils

// These are n-dimensional vectors. They are much slower than
// their 2D or 3D counterparts, so use those if you can.
type V []int

func (v V) AddInt(i int) V {
	rv := make([]int, len(v))
	for j := range v {
		rv[j] = v[j] + i
	}
	return rv
}

func (v V) Equals(other V) bool {
	if len(v) != len(other) {
		// Should we panic instead?
		return false
	}

	for i := range v {
		if v[i] != other[i] {
			return false
		}
	}
	return true
}

func (v V) MultInt(i int) V {
	rv := make([]int, len(v))
	for j := range v {
		rv[j] = v[j] * i
	}
	return rv
}

func (v V) AddV(v2 V) V {
	if len(v) != len(v2) {
		panic("vectors must be same length")
	}
	rv := make([]int, len(v))
	for i := range v {
		rv[i] = v[i] + v2[i]
	}
	return rv
}
