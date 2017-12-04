#!/usr/bin/env python

import argparse
import transfo_utils as tu

def main():

    parser = argparse.ArgumentParser(description="Computes difference between two rigid transformations.")
    parser.add_argument("transfo1")
    parser.add_argument("transfo2")
    args = parser.parse_args()

    a = tu.read_transfo(args.transfo1)
    b = tu.read_transfo(args.transfo2)

    a_vec = tu.get_transfo_vector(a)
    b_vec = tu.get_transfo_vector(b)

    diff = [ i-j for (i,j) in zip(a_vec,b_vec) ]
    print("{0} {1} {2} {3} {4} {5}".format(diff[0], diff[1], diff[2],
                                           diff[3], diff[4], diff[5]))
    
if __name__=='__main__':
    main()
