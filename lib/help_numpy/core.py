#!/usr/bin/evn python3


import numpy as np
from numpy import linalg as la


def calc_angle(a_vec, b_vec, degree=False):
    product = np.dot(a_vec, b_vec)
    scale_size = la.norm(a_vec) * la.norm(b_vec)
    cos_va = product / size
    radian_angle = np.arccos(cos_va)
    if degree:
        degree_angle = np.rad2deg(degree)
        return degree_angle
    return radian_angle
