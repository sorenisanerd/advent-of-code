#!/bin/sh
day=$1

echo "Starting day $day"
mkdir -p day$day/{python,data}

cp -r template/* day$day/
git add day$day
