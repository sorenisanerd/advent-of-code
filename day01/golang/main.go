package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"path/filepath"
	"runtime"
	"sort"
	"strconv"
	"strings"
)

func partA(filename string) int {
	sums := getSums(filename)
	return getHighest(sums)
}

func partB(filename string) int {
	sums := getSums(filename)
	sort.Ints(sums)
	return sums[len(sums)-3] + sums[len(sums)-2] + sums[len(sums)-1]
}

func getHighest(sums []int) int {
	highest := 0
	for _, sum := range sums {
		if sum > highest {
			highest = sum
		}
	}
	return highest
}

func getSums(filename string) []int {
	fp, err := os.Open(filename)
	if err != nil {
		log.Fatal(err)
	}
	sums := []int{}
	sum := 0
	scanner := bufio.NewScanner(fp)
	for scanner.Scan() {
		l := scanner.Text()
		l = strings.Trim(l, "\n")
		if l == "" {
			sums = append(sums, sum)
			sum = 0
			continue
		}
		n, _ := strconv.Atoi(l)
		sum += n
	}
	sums = append(sums, sum)
	return sums
}

func main() {
	_, filename, _, _ := runtime.Caller(0)
	fmt.Println(partA(filepath.Dir(filename) + "/../data/input.txt"))
	fmt.Println(partB(filepath.Dir(filename) + "/../data/input.txt"))
}
