package day11

import (
	"os"
	"sort"
	"strings"

	aoc "github.com/sorenisanerd/adventofcode/utils"
)

type monkey struct {
	items       []int
	operation   func(int) int
	divisibleBy int
	trueMonkey  int
	falseMonkey int
	visitCount  int
}

func PartA(filename string) int {
	monkeys := parseMonkeys(filename)

	for i := 0; i < 20; i++ {
		round(monkeys, 3, 1e10)
	}

	return calculateMonkeyBusiness(monkeys)
}

func calculateMonkeyBusiness(monkeys []monkey) int {
	counts := aoc.Map(func(m monkey) int { return m.visitCount }, monkeys)
	sort.Ints(counts)
	return aoc.GetByIdx(counts, -1) * aoc.GetByIdx(counts, -2)
}

func parseMonkeys(filename string) []monkey {
	data := string(aoc.Must(os.ReadFile, filename))
	monkeys := []monkey{}
	for _, ls := range aoc.ChunkBySliceSize(strings.Split(data, "\n"), 7) {
		if len(ls) != 7 {
			continue
		}
		monkey := monkey{}
		monkey.items = aoc.ExtractInts(ls[1])
		monkey.divisibleBy = aoc.ExtractInts(ls[3])[0]
		monkey.trueMonkey = aoc.ExtractInts(ls[4])[0]
		monkey.falseMonkey = aoc.ExtractInts(ls[5])[0]
		opString := strings.Split(ls[2], " = ")[1]
		if opString == "old * old" {
			monkey.operation = func(i int) int {
				return i * i
			}
		} else if opString == "old + old" {
			monkey.operation = func(i int) int {
				return i + i
			}
		} else {
			words := strings.Split(opString, " ")
			if words[0] != "old" {
				panic("")
			} else if words[1] == "+" {
				x := aoc.Atoi(words[2])
				monkey.operation = func(i int) int {
					return i + x
				}
			} else if words[1] == "*" {
				x := aoc.Atoi(words[2])
				monkey.operation = func(i int) int {
					return i * x
				}
			} else {
				panic("")
			}
		}
		monkeys = append(monkeys, monkey)
	}
	return monkeys
}

func round(monkeys []monkey, reduction, modulo int) {
	for idx := range monkeys {
		monkey := monkeys[idx]
		monkey.visitCount += len(monkey.items)
		for i, item := range monkey.items {
			var newMonkey int
			monkey.items[i] = monkey.operation(item)
			monkey.items[i] = (monkey.items[i] / reduction) % modulo
			if monkey.items[i]%monkey.divisibleBy == 0 {
				newMonkey = monkey.trueMonkey
			} else {
				newMonkey = monkey.falseMonkey
			}
			monkeys[newMonkey].items = append(monkeys[newMonkey].items, monkey.items[i])
		}
		monkey.items = []int{}
		monkeys[idx] = monkey
	}
}

func PartB(filename string) int {
	monkeys := parseMonkeys(filename)

	modulo := aoc.Reduce(func(a int, b monkey) int { return a * b.divisibleBy }, monkeys, 1)
	for i := 0; i < 10000; i++ {
		round(monkeys, 1, modulo)
	}

	counts := aoc.Map(func(m monkey) int { return m.visitCount }, monkeys)
	sort.Ints(counts)
	return aoc.GetByIdx(counts, -1) * aoc.GetByIdx(counts, -2)
}
