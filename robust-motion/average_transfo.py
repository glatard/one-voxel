#!/usr/bin/env python

import numpy
import math

## Distance between transformations

def maha_norm_sq(transfo_mat, s_theta, s_x, s_y, s_z):
    rot_angle, rot_vec = get_rot_angle_vec(get_rot_mat(transfo_mat))
    tr_vec = get_tr_vec(transfo_mat)
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

## Conversions between transformation formats

def get_rot_angle_vec(rot_mat):
    # See http://www.euclideanspace.com/maths/geometry/rotations/conversions/matrixToAngle/
    rot_angle = math.acos((rot_mat.item(0,0)+rot_mat.item(1,1)+rot_mat.item(2,2)-1)/2)
    x = (rot_mat.item(2,1)-rot_mat.item(1,2))/math.sqrt((rot_mat.item(2,1)-rot_mat.item(1,2))**2+(rot_mat.item(0,2)-rot_mat.item(2,0))**2 + (rot_mat.item(1,0)-rot_mat.item(0,1))**2)
    y = (rot_mat.item(0,2)-rot_mat.item(2,0))/math.sqrt((rot_mat.item(2,1)-rot_mat.item(1,2))**2+(rot_mat.item(0,2)-rot_mat.item(2,0))**2 + (rot_mat.item(1,0)-rot_mat.item(0,1))**2)
    z = (rot_mat.item(1,0)-rot_mat.item(0,1))/math.sqrt((rot_mat.item(2,1)-rot_mat.item(1,2))**2+(rot_mat.item(0,2)-rot_mat.item(2,0))**2 + (rot_mat.item(1,0)-rot_mat.item(0,1))**2)
    rot_vec = numpy.array([x, y, z])
    return rot_angle, rot_vec
   
def get_rot_mat(transfo_mat):
    rot_mat = numpy.matrix([[transfo_mat.item(0,0), transfo_mat.item(0,1), transfo_mat.item(0,2)],
                           [transfo_mat.item(1,0), transfo_mat.item(1,1), transfo_mat.item(1,2)],
                           [transfo_mat.item(2,0), transfo_mat.item(2,1), transfo_mat.item(2,2)]])
    return rot_mat

def get_tr_vec(transfo_mat):
    tr_vec = numpy.array([transfo_mat.item(0,3), transfo_mat.item(1,3), transfo_mat.item(2,3)])
    return tr_vec

## Read MNI xfm transformation

def read_transfo(file_name):
    transfo = numpy.zeros(shape=(4, 4))
    transfo_line = -1
    with open(file_name) as f:
        for line in f:
            line = line.strip()
            if transfo_line >= 0:
                elements = line.split()
                assert(len(elements) == 4), "Wrong format in transformation line: {0}".format(line)
                for i in range(0, 4):
                    transfo[transfo_line][i] = float(elements[i].strip().replace(";",""))
                transfo_line += 1
            if transfo_line >= 4:
                break
            if line.startswith("Linear_Transform"):
                transfo_line = 0

    transfo_mat = numpy.matrix([[transfo[0][0], transfo[0][1], transfo[0][2], transfo[0][3]],
        [transfo[1][0], transfo[1][1], transfo[1][2], transfo[1][3]],
        [transfo[2][0], transfo[2][1], transfo[2][2], transfo[2][3]],
        [0, 0, 0, 1]
    ])

    return transfo_mat

def get_sigmas(transfos):
    assert(transfos)
    angles = numpy.array([])
    sxs = numpy.array([])
    sys = numpy.array([])
    szs = numpy.array([])
    for transfo in transfos:
        rot_mat = get_rot_mat(transfo)
        tr_vec = get_tr_vec(transfo)
        angle, vec = get_rot_angle_vec(rot_mat)
        angles = numpy.append(angles, angle)
        sxs = numpy.append(sxs, tr_vec[0])
        sys = numpy.append(sys, tr_vec[1])
        szs = numpy.append(szs, tr_vec[2])
    return numpy.std(angles), numpy.std(sxs), numpy.std(sys), numpy.std(szs)

def mean_transfo(transfos):
    mean_transfo = transfos[0]
    s_theta, s_x, s_y, s_z = get_sigmas(transfos)
    print("sigmas: ", s_theta, s_x, s_y, s_z)
    return ssd(mean_transfo, transfos, s_theta, s_x, s_y, s_z)

transfos = []
transfos.append(read_transfo('transfo-0.xfm'))
transfos.append(read_transfo('transfo-1.xfm'))
transfos.append(read_transfo('transfo-2.xfm'))
transfos.append(read_transfo('transfo-3.xfm'))

print(mean_transfo(transfos))
