package utils

type V3 [3]int

var All3DAdjecencies = []V3{}

func init() {
	for x := -1; x <= 1; x++ {
		for y := -1; y <= 1; y++ {
			for z := -1; z <= 1; z++ {
				if x == 0 && y == 0 && z == 0 {
					continue
				}
				All3DAdjecencies = append(All3DAdjecencies, V3{x, y, z})
			}
		}
	}
}

func (v V3) AddInt(i int) V3 {
	return V3{v[0] + i, v[1] + i, v[2] + i}
}

func (v V3) AddV(other V3) V3 {
	return V3{v[0] + other[0], v[1] + other[1], v[2] + other[2]}
}

func (v V3) MultInt(i int) V3 {
	return V3{v[0] * i, v[1] * i, v[2] * i}
}
