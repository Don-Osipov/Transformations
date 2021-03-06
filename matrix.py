"""
A matrix will be an N sized list of 4 element lists.
Each individual list will represent an [x, y, z, 1] point.
For multiplication purposes, consider the lists like so:
x0  x1      xn
y0  y1      yn
z0  z1  ... zn
1  1        1
"""
import math


def make_translate(x, y, z):
    translateMatrix = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [x, y, z, 1]]
    return translateMatrix


def make_scale(x, y, z):
    scaleMatrix = [[x, 0, 0, 0], [0, y, 0, 0], [0, 0, z, 0,], [0, 0, 0, 1]]
    return scaleMatrix


def make_rotX(theta):
    rTheta = math.radians(theta)
    rotationMatrix = [
        [1, 0, 0, 0],
        [0, math.cos(rTheta), math.sin(rTheta), 0],
        [0, -math.sin(rTheta), math.cos(rTheta), 0],
        [0, 0, 0, 1],
    ]
    return rotationMatrix


def make_rotY(theta):
    rTheta = math.radians(theta)
    rotationMatrix = [
        [math.cos(rTheta), 0, -math.sin(rTheta), 0],
        [0, 1, 0, 0],
        [math.sin(rTheta), 0, math.cos(rTheta), 0],
        [0, 0, 0, 1],
    ]
    return rotationMatrix


def make_rotZ(theta):
    rTheta = math.radians(theta)
    print(theta)
    print(rTheta)
    rotationMatrix = [
        [math.cos(rTheta), math.sin(rTheta), 0, 0],
        [-math.sin(rTheta), math.cos(rTheta), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1],
    ]
    return rotationMatrix


# print the matrix such that it looks like
# the template in the top comment
def print_matrix(matrix):
    s = ""
    for r in range(len(matrix[0])):
        for c in range(len(matrix)):
            s += str(matrix[c][r]) + " "
        s += "\n"
    print(s)


# def print_matrix(matrix):
#     for row in matrix:
#         for el in row:
#             print(f"{el} ", end="")
#         print()


# turn the paramter matrix into an identity matrix
# you may assume matrix is square
def ident(matrix):
    for r in range(len(matrix[0])):
        for c in range(len(matrix)):
            if r == c:
                matrix[c][r] = 1
            else:
                matrix[c][r] = 0


# multiply m1 by m2, modifying m2 to be the product
# m1 * m2 -> m2
def matrix_mult(m1, m2):

    point = 0
    for row in m2:
        # get a copy of the next point
        tmp = row[:]

        for r in range(4):
            m2[point][r] = m1[0][r] * tmp[0] + m1[1][r] * tmp[1] + m1[2][r] * tmp[2] + m1[3][r] * tmp[3]
        point += 1


def new_matrix(rows=4, cols=4):
    m = []
    for c in range(cols):
        m.append([])
        for r in range(rows):
            m[c].append(0)
    return m
