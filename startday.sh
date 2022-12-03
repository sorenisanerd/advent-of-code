#!/bin/sh
day=$1

echo "Starting day $day"
mkdir -p day$day/{golang,python,data}

cd day$day/golang
go mod init github.com/sorenisanerd/adventofcode2022/day$day
cd -

cp -r template/* day$day/
