#!/bin/bash

svg_file=$1
temp_file="/tmp/$svg_file.temp"
usage="Converts svg files for use in manim using cairosvg.
USAGE:
$0 [SVG_FILE]"

if [ $# -eq 0 ]
  then
  echo "$usage"
  exit
fi

cairosvg "$svg_file" -f svg -o "$temp_file"
if  [ $? -eq 0 ] ; then
    rm -f "$svg_file"
    mv "$temp_file" "$svg_file"
else
    echo "error: cannot convert $svg_file"
fi
