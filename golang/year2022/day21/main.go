package day21

import (
	"os"
	"strconv"
	"strings"

	aoc "github.com/sorenisanerd/adventofcode/utils"
)

func PartA(filename string) int {
	known, unknown := loadData(filename)
	return int(solve(unknown, known))
}

func solve(unknown map[string]string, known map[string]float64) float64 {
	for len(unknown) > 0 {
		for k := range unknown {
			arg1, op, arg2 := func(s string) (string, string, string) {
				ss := strings.Split(s, " ")
				return ss[0], ss[1], ss[2]
			}(unknown[k])

			if _, ok := known[arg1]; ok {
				if _, ok2 := known[arg2]; ok2 {
					known[k] = aoc.NumOp[float64](op)(known[arg1], known[arg2])
					delete(unknown, k)
				}
			}
		}
	}
	return known["root"]
}

func loadData(filename string) (map[string]float64, map[string]string) {
	data := string(aoc.Must(os.ReadFile, filename))
	known := make(map[string]float64)
	unknown := make(map[string]string)
	for _, line := range aoc.SplitLines(data) {
		kexpr := strings.Split(line, ": ")
		k, expr := kexpr[0], kexpr[1]
		if v, err := strconv.Atoi(expr); err == nil {
			known[k] = float64(v)
		} else {
			unknown[k] = expr
		}
	}
	return known, unknown
}

func PartB(filename string) int {
	tryGuess := func(humn float64) float64 {
		known, unknown := loadData(filename)

		delete(unknown, "humn")
		known["humn"] = humn
		args := strings.Split(unknown["root"], " ")
		args[1] = "-"
		unknown["root"] = strings.Join(args, " ")

		return solve(unknown, known)
	}

	return int(Newton(tryGuess, 0))
}

// Let's find us some roots, Newton style!
func Newton(f func(float64) float64, x0 float64) float64 {
	y := f(x0)

	if y == 0 {
		return x0
	}

	dx := 1.0
	x := x0 + dx
	for {
		newY := f(x)
		if newY == 0 {
			return x
		}

		dy := newY - y
		dx = -newY / (dy / dx)
		x = x + dx
		y = newY
	}
}
