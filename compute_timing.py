#!/usr/bin/python3

import sys
import datetime

FRAME_RATE=23

def print_usage():
    print(f"Usage: {sys.argv[0]} timing_file [-h help]")

def time_dif(start,end):
    return convert_time(end) - convert_time(start)

def convert_time(time_str):
    time_split = time_str.split(':')
    subseconds = (1./FRAME_RATE)*int(time_split[-1])
    seconds = 0
    minutes = 0
    if len(time_split) > 1:
        seconds = int(time_split[-2])
    if len(time_split) > 2:
        minutes = int(time_split[-3])
    total_time = 60*minutes + seconds + subseconds
    return total_time

if __name__ == "__main__":
    if len(sys.argv) < 2 or "-h" in sys.argv:
        print_usage()
        exit()
    f=open(sys.argv[1])
    for line in f.readlines():
        line_fixed = line.replace(' ','').replace('\n','').replace('\r','')
        if line_fixed[0] == '#':
            continue
        if len(line_fixed) == 0:
            continue
        subscene = line.split(',')[0]
        timing = line.split(',')[1]

        start = convert_time(timing.split('->')[0])
        end = convert_time(timing.split('->')[1])
        total_time = end - start

        print("{0} --> {1:.2f}".format(subscene,total_time))

    f.close()
