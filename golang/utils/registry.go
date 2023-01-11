package utils

type partFunc func(string) any
type genericPartFunc[T any] func(string) T

type Day struct {
	Year  int
	Day   int
	PartA partFunc
	PartB partFunc
}

var Registry []Day

func buildPartFunc(pf any) partFunc {
	switch pft := pf.(type) {
	case func(string) int:
		return func(s string) any { return pft(s) }
	case func(string) string:
		return func(s string) any { return pft(s) }
	}
	return nil
}

func RegisterDay(year, d int, partA, partB any) {
	dd := Day{Year: year, Day: d, PartA: buildPartFunc(partA), PartB: buildPartFunc(partB)}
	Registry = append(Registry, dd)
}
