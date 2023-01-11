package utils

import (
	"fmt"
	"os"
	"path/filepath"
)

type Test struct {
	Name     string
	F        func(string) int
	Filename string
	Want     int
}

type InputOutputPair struct {
	Input  string // Full path to input file
	Output string // Full path to output file
	Part   string // Either "A" or "B"
}

func FindInputOutput(year, day int) []InputOutputPair {
	rv := []InputOutputPair{}
	dataDir := fmt.Sprintf("%s/data/%s/", GetTopDir(), GetDataDirSubPath(year, day))

	expFiles := Must(filepath.Glob, dataDir+"*.part[AB]")

	for _, outputFile := range expFiles {
		inputFile := outputFile[:len(outputFile)-len(".part?")]
		if _, err := os.Stat(inputFile); err != nil {
			continue
		}
		rv = append(rv, InputOutputPair{inputFile, outputFile, outputFile[len(outputFile)-1:]})
	}
	return rv
}

/*
func RunTests(t *testing.T, year, day int, tests []Test) {
	for _, tt := range tests {
		t.Run(tt.Name, func(t *testing.T) {
			for _, inOutFiles := range FindInputOutput(year, day) {
				input := LoadData(inOutFiles.Input)
				outut := LoadData(inOutFiles.Output)

				assert.Equal(t, mod.PartA(d), 69528)
			}
		})
	}
}
*/
