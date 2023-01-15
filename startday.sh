#!/bin/sh
if [ $# -ne 2 ]; then
    echo "Usage: $0 year day"
    exit 1
fi

year=$1
day="$2"
paddedDay="$(printf %02d $2)"

echo "Starting day $year/12/$day"
pydir=python/aoc/year$year/day$paddedDay

if [ -d $pydir ]; then
    echo "Directory $pydir already exists"
else
    mkdir -p $pydir
    cp -r python/_template/*.py $pydir
    sed -e "s#ayXX#ay${paddedDay}#" -i '' $pydir/*
    git add $pydir
fi

godir=golang/year$year/day$paddedDay
if [ -d $godir ]; then
    echo "Directory $godir already exists"
else
    mkdir -p $godir
    cp -r golang/_template/*.go $godir
    sed -e "s#ayXX#ay${paddedDay}#" -i '' $godir/*
    git add $godir
fi
