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

func GetGreaterThan[T constraints.Ordered](a T) func(T) bool {
	return func(b T) bool {
		return b > a
	}
}

func GetLessThan[T constraints.Ordered](a T) func(T) bool {
	return func(b T) bool {
		return b < a
	}
}

func GetGreaterThanOrEqual[T constraints.Ordered](a T) func(T) bool {
	return func(b T) bool {
		return b >= a
	}
}

func GetLessThanOrEqual[T constraints.Ordered](a T) func(T) bool {
	return func(b T) bool {
		return b <= a
	}
}
