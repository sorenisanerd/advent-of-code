package utils

import (
	"golang.org/x/exp/constraints"
)

func NumOp[T constraints.Float | constraints.Integer](op string) func(T, T) T {
	return func(a, b T) T {
		switch op {
		case "+":
			return a + b
		case "-":
			return a - b
		case "*":
			return a * b
		case "/":
			return a / b
		default:
			panic("Unknown operator: " + op)
		}
	}
}

func BoolOp[T constraints.Ordered](op string, a T) func(T) bool {
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
