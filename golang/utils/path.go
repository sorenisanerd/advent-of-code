package utils

import (
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

func GetCallerDataDir() string {
	var elems []string
	var filename string
	for i := 0; i <= 10; i++ {
		_, filename, _, _ = runtime.Caller(i)
		elems = strings.Split(filename, "/")
		if strings.HasPrefix(elems[len(elems)-3], "year") {
			break
		}
	}

	y := elems[len(elems)-3][4:]
	d := elems[len(elems)-2][3:]
	p, err := filepath.Abs(filepath.Dir(filename) + "/../../../data/" + y + "/" + d)
	if err != nil {
		panic(err)
	}
	return p + "/"
}
