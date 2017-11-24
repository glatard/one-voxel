#!/usr/bin/env python

import argparse
import norm_transfos as nt
import transfo_utils as tu

def main():

    parser = argparse.ArgumentParser(description="Computes Mahanalobis distance between two rigid transformations.")
    parser.add_argument("transfo1")
    parser.add_argument("transfo2")
    parser.add_argument("sigma_theta", type=float)
    parser.add_argument("sigma_x", type=float)
    parser.add_argument("sigma_y", type=float)
    parser.add_argument("sigma_z", type=float)
    args = parser.parse_args()

    d=nt.dist_square(tu.read_transfo(args.transfo1),
                   tu.read_transfo(args.transfo2),
                   args.sigma_theta,
                   args.sigma_x,
                   args.sigma_y,
                   args.sigma_z)
    print(d)
    
if __name__=='__main__':
    main()
