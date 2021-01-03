#!/usr/bin/env python3

# formal lib
import argparse
from argparse import RawTextHelpFormatter
import glob
import os
import numpy as np
# my lib


def dirstr(path_str):
    if not os.path.isdir(path_str):
        mes = "{} is not directory.".format(
                                        path_str
                                           )
        raise OSError(mes)
    return path_str


def sum_fpaths(fpaths):
    sum_list = []
    for fpath in fpaths:
        num_ar = np.loadtxt(fpath)
        sum_va = np.sum(num_ar)
        sum_list.append(sum_va)
    value = np.sum(sum_list)
    return value


if __name__ == "__main__":
    msg = "this program makes "
    parser = argparse.ArgumentParser(
                            description=msg,
                            fromfile_prefix_chars="@",
                            formatter_class=RawTextHelpFormatter)
    parser.add_argument("dpaths", type=dirstr, nargs="*")
    args = parser.parse_args()
    DPATHS = args.dpaths
    for dpath in DPATHS:
        abs_path = os.path.abspath(dpath)
        glob_word = abs_path + "/*.txt"
        fpaths = glob.glob(glob_word)
        value = sum_fpaths(fpaths)
        print("SUM: {}".format(value))
