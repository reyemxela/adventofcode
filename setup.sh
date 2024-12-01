#!/bin/bash

MAINDIR=$(dirname $(readlink -f "$0"))

SESSION=$(<"$MAINDIR/.token")
if [ $? -ne 0 ]; then echo ".token file read error"; exit 1; fi
if [ "$SESSION" = "" ]; then echo ".token file empty"; exit 1; fi

YEAR=`date +"%Y"`
DAY=`date +"%d"`

if [[ $# == 2 ]]; then
  YEAR=$1
  DAY=$2
else
  echo -n "Year [${YEAR}]: "; read y
  echo -n "Day [${DAY}]: "; read d
  [[ $y != "" ]] && YEAR=$y
  [[ $d != "" ]] && DAY=$d
fi

DAY_PAD=$DAY
[[ ${#DAY_PAD} == 1 ]] && DAY_PAD="0$DAY_PAD"

NEWDIR="${MAINDIR}/${YEAR}/${DAY_PAD}"
mkdir -p $NEWDIR
cd $NEWDIR

[[ ! -e input.txt ]] && curl -s -b "session=${SESSION}" "https://adventofcode.com/${YEAR}/day/${DAY}/input" > input.txt

touch sample.txt

FILENAME="main.py"

if [ -f $FILENAME ]; then
    echo "!!! $FILENAME already exists !!!"
else
    cp ${MAINDIR}/_template.py $FILENAME
fi
