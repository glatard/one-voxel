#!/usr/bin/env python

import argparse
import transfo_utils as tu

parser = argparse.ArgumentParser("Prints transformation parameters from xfm file: tx, ty, tz, rx, ry, rz")
parser.add_argument("transfo_file", action="store",
                    help="xfm transformation file.")
results = parser.parse_args()

transfo_mat = tu.read_transfo(results.transfo_file)
tr_vec = tu.get_tr_vec(transfo_mat)
rot_mat = tu.get_rot_mat(transfo_mat)
rot_angles = tu.get_euler_angles(rot_mat)
print("{0}, {1}, {2}, {3}, {4}, {5}".format(tr_vec[0], tr_vec[1], tr_vec[2],
                                            rot_angles[0], rot_angles[1], rot_angles[2]))
