#!/usr/bin/env python

import argparse
import norm_transfos as nt
import transfo_utils as tu


parser = argparse.ArgumentParser("Computes the average of a set of transformations.")
parser.add_argument("transfo_xfm", nargs='+', 
                    help="A set of xfm transformations.")
parser.add_argument("output_file", action="store",
                    help="Output file with transformation matrix containing the mean transformation.")
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
transfo_vectors = []
for t in transfos:
    t = tu.get_transfo_vector(t)
    transfo_vectors.append(t)
    ttx, tty, ttz, trx, try_, trz = t
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

# Compute naive variance
var_tx = 0
var_ty = 0
var_tz = 0
var_rx = 0
var_ry = 0
var_rz = 0
for t in transfo_vectors:
    ttx, tty, ttz, trx, try_, trz = t
    var_tx += (ttx-tx)**2
    var_ty += (tty-ty)**2
    var_tz += (ttz-tz)**2
    var_rx += (trx-rx)**2
    var_ry += (try_-ry)**2
    var_rz += (trz-rz)**2
var_tx /= n
var_ty /= n
var_tz /= n
var_rx /= n
var_ry /= n
var_rz /= n

print("Variance: {0} {1} {2} {3} {4} {5}".format(
    var_tx,
    var_ty,
    var_tz,
    var_rx,
    var_ry,
    var_rz))

naive_mean = tu.get_transfo_mat([tx, ty, tz, rx, ry, rz])

# Compute Frechet mean from Mahanalobis norm
#try: 
#mean, variance = nt.mean_transfo(transfos)
#except:
mean = naive_mean
#  variance = -1


# print("\n# Results\n\nTransformations:")
# for x in transfos:
#     print(tu.get_transfo_vector(x))
# print("----------------------------------------------------------------\
# ------------------------------------------------------------------------")
# print("Frechet mean: {0}".format(tu.get_transfo_vector(m)))
# print("Naive mean:   {0}".format(tu.get_transfo_vector(naive_mean)))

#print("mean: {0} ; variance: {1}".format(tu.get_transfo_vector(mean),variance))

tu.print_mat(mean, results.output_file)

