#!/usr/bin/env python

import argparse
import transfo_utils as tu

def get_mean_and_variance(transfos):
    # Naive mean
    tx = 0
    ty = 0
    tz = 0
    rx = 0
    ry = 0
    rz = 0
    tx2 = 0
    ty2 = 0
    tz2 = 0
    rx2 = 0
    ry2 = 0
    rz2 = 0
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
        tx2 += ttx**2
        ty2 += tty**2
        tz2 += ttz**2
        rx2 += trx**2
        ry2 += try_**2
        rz2 += trz**2
    n = len(transfos)
    tx /= n
    ty /= n
    tz /= n
    rx /= n
    ry /= n
    rz /= n
    tx2 /= n
    ty2 /= n
    tz2 /= n
    rx2 /= n
    ry2 /= n
    rz2 /= n
    
    var_tx = tx2 - tx**2
    var_ty = ty2 - ty**2
    var_tz = tz2 - tz**2
    var_rx = rx2 - rx**2
    var_ry = ry2 - ry**2
    var_rz = rz2 - rz**2

    # Compute Frechet mean from Mahanalobis norm
    #mean, variance = nt.mean_transfo(transfos)

    return tx, ty, tz, rx, ry, rz, var_tx, var_ty, var_tz, var_rx, var_ry, var_rz

### Main
def main():
    
    parser = argparse.ArgumentParser("Computes the average of a set of transformations.")
    parser.add_argument("transfo_xfm", nargs='+', 
                        help="A set of xfm transformations.")
    parser.add_argument("output_file", action="store",
                        help="Output file with transformation matrix containing the mean transformation.")
    results = parser.parse_args()
    
    transfos = []
    for x in results.transfo_xfm:
        transfos.append(tu.read_transfo(x))

        tx, ty, tz, rx, ry, rz, var_tx, var_ty, var_tz, var_rx, var_ry, var_rz = get_mean_and_variance(transfos)
        mean = tu.get_transfo_mat([tx, ty, tz, rx, ry, rz])

        print("Variance: {0} {1} {2} {3} {4} {5}".format(
            var_tx,
            var_ty,
            var_tz,
            var_rx,
            var_ry,
            var_rz))

        tu.print_mat(mean, results.output_file)

if __name__=='__main__':
    main()

# print("\n# Results\n\nTransformations:")
# for x in transfos:
#     print(tu.get_transfo_vector(x))
# print("----------------------------------------------------------------\
# ------------------------------------------------------------------------")
# print("Naive mean:   {0}".format(tu.get_transfo_vector(naive_mean)))

#print("mean: {0} ; variance: {1}".format(tu.get_transfo_vector(mean),variance))



