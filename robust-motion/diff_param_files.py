#!/usr/bin/env python

import argparse
import csv

def get_csv_lines(file_name):
    lines = []
    with open(file_name, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for line in reader:
            lines.append(line)
    return lines

parser = argparse.ArgumentParser("Prints the difference of transfo param files formated as: vol_id, tx, ty, tz, rx, ry, rz")
parser.add_argument("file1", action="store",
                    help="first transformation file.")
parser.add_argument("file2", action="store",
                    help="second transformation file.")
results = parser.parse_args()



lines1 = get_csv_lines(results.file1)
lines2 = get_csv_lines(results.file2)

assert(len(lines1)==len(lines2))

for i in range(0, len(lines1)):
    line1 = lines1[i]
    line2 = lines2[i]
    assert(len(line1)==7)
    assert(len(line2)==7)
    assert(line1[0]==line2[0])
    print("{0}, {1}, {2}, {3}, {4}, {5}".format(
        line1[0],
        float(line1[1])-float(line2[1]),
        float(line1[2])-float(line2[2]),
        float(line1[3])-float(line2[3]),
        float(line1[4])-float(line2[4]),
        float(line1[5])-float(line2[5]),
        float(line1[6])-float(line2[6])
    ))
