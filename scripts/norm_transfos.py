#!/usr/bin/env python

import numpy
from scipy.optimize import minimize
import transfo_utils as tu

## Distance between transformations

def maha_norm_sq(transfo_mat, s_theta, s_x, s_y, s_z):
    rot_angle, rot_vec = tu.get_rot_angle_vec(tu.get_rot_mat(transfo_mat))
    tr_vec = tu.get_tr_vec(transfo_mat)
    contrib_angle = 0
    if rot_angle:
        contrib_angle = rot_angle**2/s_theta**2
    contrib_x = 0
    if tr_vec[0]:
        contrib_x = tr_vec[0]**2/s_x**2
    contrib_y = 0
    if tr_vec[1]:
        contrib_y = tr_vec[1]**2/s_y**2
    contrib_z = 0
    if tr_vec[2]:
        contrib_z = tr_vec[2]**2/s_z**2
    return contrib_angle + contrib_x + contrib_y + contrib_z

def dist_square(transfo_mat1, transfo_mat2, s_theta, s_x, s_y, s_z):
    d = maha_norm_sq(transfo_mat1.I * transfo_mat2, s_theta, s_x, s_y, s_z)
    return d

def ssd(transfo, transfos, s_theta, s_x, s_y, s_z):
    ssd = 0
    for t in transfos:
        ssd += dist_square(transfo, t, s_theta, s_x, s_y, s_z)
    return ssd

def get_sigmas(transfos):
    assert(transfos)
    angles = numpy.array([])
    sxs = numpy.array([])
    sys = numpy.array([])
    szs = numpy.array([])
    for transfo in transfos:
        rot_mat = tu.get_rot_mat(transfo)
        tr_vec = tu.get_tr_vec(transfo)
        angle, vec = tu.get_rot_angle_vec(rot_mat)
        angles = numpy.append(angles, angle)
        sxs = numpy.append(sxs, tr_vec[0])
        sys = numpy.append(sys, tr_vec[1])
        szs = numpy.append(szs, tr_vec[2])
    return numpy.std(angles), numpy.std(sxs), numpy.std(sys), numpy.std(szs)

def mean_transfo(transfos):
    s_theta, s_x, s_y, s_z = get_sigmas(transfos)
    assert(s_theta!=0 and s_x!=0 and s_y!=0 and s_z!=0)
    print("\n# Mean computation")
    print("s_theta={0}, s_x={1}, s_y={2}, s_z={3}".format(s_theta, s_x, s_y, s_z))
    def obj(x): # the objective function to minimize
        transfo = tu.get_transfo_mat(x)
        return ssd(transfo, transfos, s_theta, s_x, s_y, s_z)
    mean_transfo = transfos[0]
    rx, ry, rz = tu.get_euler_angles(mean_transfo)
    [tx, ty, tz] = tu.get_tr_vec(mean_transfo)
    res = minimize(obj, [tx, ty, tz, rz, ry, rz], method='BFGS', options={'disp': True})
    return tu.get_transfo_mat(res.x)


