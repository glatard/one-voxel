#!/usr/bin/env python

import argparse
import norm_transfos as nt
import transfo_utils as tu


parser = argparse.ArgumentParser("Computes the average of a set of transformations.")
parser.add_argument("transfo_xfm", nargs='+', 
                    help="A set of xfm transformations.")
parser.add_argument("output_file", action="store",
                    help="Output file with transformation matrix.")
results = parser.parse_args()

transfos = []
for x in results.transfo_xfm:
    transfos.append(tu.read_transfo(x))

# Naive mean
tx = 0
ty = 0
tz = 0
rx = 0
ry = 0
rz = 0
for t in transfos:
    ttx, tty, ttz, trx, try_, trz = tu.get_transfo_vector(t)
    tx += ttx
    ty += tty
    tz += ttz
    rx += trx
    ry += try_
    rz += trz
n = len(transfos)
tx /= n
ty /= n
tz /= n
rx /= n
ry /= n
rz /= n
naive_mean = tu.get_transfo_mat([tx, ty, tz, rx, ry, rz])

# Compute Frechet mean from Mahanalobis norm
try:
    mean, variance = nt.mean_transfo(transfos)
except:
    mean = naive_mean
    variance = -1


#print("\n# Results\n\nTransformations:")
#for x in transfos:
#    print(tu.get_transfo_vector(x))
#print("----------------------------------------------------------------\
#------------------------------------------------------------------------")
#print("Frechet mean: {0}".format(tu.get_transfo_vector(m)))
#print("Naive mean:   {0}".format(tu.get_transfo_vector(naive_mean)))

print("mean: {0} ; variance: {1}".format(tu.get_transfo_vector(mean),variance))

tu.print_mat(mean, results.output_file)

