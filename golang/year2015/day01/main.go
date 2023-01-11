package day01

import (
	"fmt"
	"os"
	"strings"

	aoc "github.com/sorenisanerd/adventofcode/utils"
)

func PartA(filename string) int {
	data := string(aoc.Must(os.ReadFile, filename))
	return strings.Count(data, "(") - strings.Count(data, ")")
}

func PartB(filename string) int {
	rv := 0
	data := string(aoc.Must(os.ReadFile, filename))
	fmt.Println(data)
	return rv
}
