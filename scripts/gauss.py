#!/usr/bin/env python

import argparse
import nibabel
import random

def main():

    parser = argparse.ArgumentParser(description="Adds Gaussian noise to input image.")
    parser.add_argument("image_file")
    parser.add_argument("output_file")
    parser.add_argument("sigma", type=float)
    args = parser.parse_args()
    
    # Load image using nibabel
    im = nibabel.load(args.image_file)
       
    shape = im.header.get_data_shape()
    assert(len(shape) == 4 or len(shape) == 3)
    
    xdim = shape[0]
    ydim = shape[1]
    zdim = shape[2]
    tdim = 0
    if (len(shape) == 4):
        tdim = shape[3] 

    data = im.get_data()

    print(xdim, ydim, zdim, tdim)

    if tdim != 0:
        for x in range(0, xdim):
            for y in range(0, ydim):
                for z in range(0, zdim):
                    for t in range(0, tdim):
                        r = random.gauss(0, args.sigma)
                        data[x][y][z][t] += r
    else:
        for x in range(0, xdim):
            for y in range(0, ydim):
                for z in range(0, zdim):
                        r = random.gauss(0, args.sigma)
                        data[x][y][z] += r
            
    im.to_filename(args.output_file)

if __name__=='__main__':
    main()
