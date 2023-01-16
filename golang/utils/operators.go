package utils

import (
	"golang.org/x/exp/constraints"
)

func Op[T constraints.Ordered](op string, a T) func(T) bool {
	switch op {
	case ">":
		return func(b T) bool {
			return b > a
		}
	case "<":
		return func(b T) bool {
			return b < a
		}
	case ">=":
		return func(b T) bool {
			return b >= a
		}
	case "<=":
		return func(b T) bool {
			return b <= a
		}
	}
	panic("Unknown operator: " + op)
}
