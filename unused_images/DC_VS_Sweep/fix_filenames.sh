#!/bin/bash

#   fixes incorrectly formated file labels
#
#   2.0                ->    2.00
#   1.0400000000001    ->    1.04

for file in $(ls | grep DC-Ampl-)
do 
    fixed_fname=$(echo $file | sed 's/DC-Ampl-//g' | sed 's/.png//g' | printf "DC-Ampl-%1.2f.png\n" $(</dev/stdin))
    cp $file output/$fixed_fname
done
