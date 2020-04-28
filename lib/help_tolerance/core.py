#!/usr/bin/env python3


import numpy as np


def isclose(a, b, ref_tol=1e-09):
    abs_va = abs(a - b)
    if abs_va < ref_tol:
        return True
    else:
        raise AssertionError("a is not enough close to b")
