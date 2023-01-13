package main

import (
	"flag"
	"fmt"
	"path/filepath"
	"strings"
	"time"

	"github.com/sorenisanerd/adventofcode/utils"
	_ "github.com/sorenisanerd/adventofcode/year2022"
)

var baseDir *string

func init() {
	topDir := utils.GetTopDir()
	baseDir = flag.String("data-dir", topDir+"/data", "data directory")
}

func prependMultilineStringWithNewline(s any) string {
	rv := fmt.Sprintf("%v", s)
	if strings.Contains(rv, "\n") {
		return "\n" + rv
	}
	return rv
}

func runDayPart(inputData string, year, day int, partName string, f func(string) any) {
	fmt.Printf("Year %4d, day %2d, Part %s:", year, day, partName)
	rv := fmt.Sprint(f(inputData))
	if strings.Contains(rv, "\n") {
		fmt.Printf("\n%s\n", rv)
	} else {
		fmt.Printf("%s\n", rv)
	}
}

func benchDayPart(inputData string, year, day int, partName string, f func(string) any) {
	count := 0
	start := time.Now()
	deadline := start.Add(2 * time.Second)

	// Run it once for warmup
	f(inputData)
	for time.Now().Before(deadline) {
		f(inputData)
		count += 1
	}

	fmt.Printf("Year %4d, day %2d, Part %s: %05fms (averaged over %d runs)\n", year, day, partName, time.Since(start).Seconds()*1000/float64(count), count)
}

func main() {
	bench := flag.Bool("bench", false, "benchmark mode")
	flag.Parse()
	for _, d := range utils.Registry {
		inputFile := filepath.Join(*baseDir, utils.GetDataDirSubPath(d.Year, d.Day), "input.txt")
		//		inputData := utils.LoadData(inputFile)
		if *bench {
			benchDayPart(inputFile, d.Year, d.Day, "A", d.PartA)
			benchDayPart(inputFile, d.Year, d.Day, "B", d.PartB)
		} else {
			runDayPart(inputFile, d.Year, d.Day, "A", d.PartA)
			runDayPart(inputFile, d.Year, d.Day, "B", d.PartB)
		}
	}
}
