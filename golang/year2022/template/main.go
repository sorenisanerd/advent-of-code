package dayXX

import (
	"fmt"
	"os"

	aoc "github.com/sorenisanerd/adventofcode/utils"
)

func PartA(filename string) int {
	rv := 0
	data := string(aoc.Must(os.ReadFile, filename))
	fmt.Println(data)
	return rv
}

func PartB(filename string) int {
	rv := 0
	data := string(aoc.Must(os.ReadFile, filename))
	fmt.Println(data)
	return rv
}
