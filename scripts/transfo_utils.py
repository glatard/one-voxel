import numpy
import math

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

def get_euler_angles(transfo_mat):
    # From http://nghiaho.com/?page_id=846
    rx = math.atan2(transfo_mat.item(2,1), transfo_mat.item(2,2))
    ry = math.atan2(-transfo_mat.item(2,0),
                    math.sqrt(transfo_mat.item(2,1)**2 + transfo_mat.item(2,2)**2)
    )
    rz = math.atan2(transfo_mat.item(1,0), transfo_mat.item(0,0))
    return rx, ry, rz

# Reads an MNI xfm transformation
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
