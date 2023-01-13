package utils

import (
	"fmt"
	"os"
	"path/filepath"
	"runtime"
	"strings"
)

func GetDataFileName(fname string) string {
	return GetCallerDataDir() + fname
}

func LoadData(fname string) string {
	return string(Must(os.ReadFile, fname))
}

func GetDataDirSubPath(year, day int) string {
	return fmt.Sprintf("%04d/%02d", year, day)
}

func GetTopDir() string {
	_, filename, _, _ := runtime.Caller(0)
	return Must(filepath.Abs, filepath.Dir(filename)+"/../../")
}

func GetCallerDataDir() string {
	var elems []string
	var filename string
	for i := 0; i <= 10; i++ {
		_, filename, _, _ = runtime.Caller(i)
		if filename == "" {
			panic("Could not find caller data dir")
		}

		elems = strings.Split(filename, "/")
		if strings.HasPrefix(elems[len(elems)-3], "year") {
			break
		}
	}

	y := Atoi(elems[len(elems)-3][4:])
	d := Atoi(elems[len(elems)-2][3:])
	p, err := filepath.Abs(filepath.Dir(filename) + "/../../../data/" + GetDataDirSubPath(y, d))
	if err != nil {
		panic(err)
	}
	return p + "/"
}
