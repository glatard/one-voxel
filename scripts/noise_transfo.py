#!/usr/bin/env python

import argparse
import transfo_utils as tu
import random

parser = argparse.ArgumentParser("Adds Gaussian noise to transformation parameters.")
parser.add_argument("input_transfo_xfm",  
                    help="Input xfm transformations.")
parser.add_argument("output_transfo_xfm", action="store",
                    help="Output xfm transformation.")
parser.add_argument("sigma_tr", type=float, help="Noise variance on translation parameters")
parser.add_argument("sigma_rot", type=float, help="Noise variance on rotation parameters")
results = parser.parse_args()

transfo = tu.read_transfo(results.input_transfo_xfm)
tr_vector = tu.get_transfo_vector(transfo)
new_tr_vector = []
for i, x in enumerate(tr_vector):
    if i < 3:
        sigma = results.sigma_tr
    else:
        sigma = results.sigma_rot
    r = random.gauss(0, sigma)
    new_tr_vector.append(x+r)
transfo = tu.get_transfo_mat(new_tr_vector)
tu.print_mat(transfo, results.output_transfo_xfm)
