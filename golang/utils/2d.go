package utils

type V2 [2]int

var FourDirections = []V2{{1, 0}, {0, 1}, {-1, 0}, {0, -1}}

func (v V2) AddInt(i int) V2 {
	return V2{v[0] + i, v[1] + i}
}

func (v V2) AddV(other V2) V2 {
	return V2{v[0] + other[0], v[1] + other[1]}
}

func (v V2) MultInt(i int) V2 {
	return V2{v[0] * i, v[1] * i}
}

// MD is Manhattan Distance
func (v V2) MD(other V2) int {
	return Abs(v[0]-other[0]) + Abs(v[1]-other[1])
}
