#!/usr/bin/env python

import argparse
import csv

def get_csv_lines(file_name, delimiter):
    lines = []
    with open(file_name, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=delimiter)
        for line in reader:
            lines.append(line)
    return lines

parser = argparse.ArgumentParser("Prints the difference of transfo param files formated as: vol_id, tx, ty, tz, rx, ry, rz")
parser.add_argument("file1", action="store",
                    help="first transformation file.")
parser.add_argument("file2", action="store",
                    help="second transformation file.")
parser.add_argument("--mcflirt", action="store_true",
                    help="File is in format produced by mcflirt.")

results = parser.parse_args()



if not results.mcflirt:
    lines1 = get_csv_lines(results.file1,',')
    lines2 = get_csv_lines(results.file2,',')
else:
    lines1 = get_csv_lines(results.file1,' ')
    lines2 = get_csv_lines(results.file2,' ')

   
assert(len(lines1)==len(lines2)),"{0} != {1}".format(len(lines1), len(lines2))

for i in range(0, len(lines1)):
    line1 = lines1[i]
    line2 = lines2[i]
    # filter empty elements
    line1 = [x for x in line1 if len(x)!=0]
    line2 = [x for x in line2 if len(x)!=0]
    if not results.mcflirt:
        assert(len(line1)==7)
        assert(len(line2)==7)
        assert(line1[0]==line2[0])
        print("{0} {1} {2} {3} {4} {5} {6}".format(
            line1[0],
            float(line1[1])-float(line2[1]),
            float(line1[2])-float(line2[2]),
            float(line1[3])-float(line2[3]),
            float(line1[4])-float(line2[4]),
            float(line1[5])-float(line2[5]),
            float(line1[6])-float(line2[6])))
    else:
        assert(len(line1)==6)
        assert(len(line2)==6)
        print("{0} {1} {2} {3} {4} {5}".format(
            float(line1[0])-float(line2[0]),
            float(line1[1])-float(line2[1]),
            float(line1[2])-float(line2[2]),
            float(line1[3])-float(line2[3]),
            float(line1[4])-float(line2[4]),
            float(line1[5])-float(line2[5])))
