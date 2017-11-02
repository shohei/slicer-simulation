#!/bin/sh
if [ $# -ne 1 ]; then
  echo "./pre.sh <some gcode file>"
  exit 1
fi
sed -n '/^G1/p' $1 > g1.txt
