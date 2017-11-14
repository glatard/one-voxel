#!/usr/bin/env python

import argparse
import nibabel

def main():

    parser = argparse.ArgumentParser(description="Changes the intensity of the\
 central voxel in each volume by 1%.")
    parser.add_argument("image_file")
    parser.add_argument("output_file")
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

    if tdim != 0:
        for t in range(0, tdim):
            data[xdim/2][ydim/2][zdim/2][t] *= 1.01
    else:
        data[xdim/2][ydim/2][zdim/2] *= 1.01
            
    im.to_filename(args.output_file)

if __name__=='__main__':
    main()

