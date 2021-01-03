#!/usr/bin/env python3


# formal lib
import os
import argparse
from argparse import RawTextHelpFormatter
# my lib


def fnmstr(path_str):
    if not os.path.exists(path_str):
        mes = "{} is not file.".format(
                                    path_str
                                      )
        raise OSError(mes)
    return path_str


if __name__ == "__main__":
    msg = "this program gets absolute paths"
    parser = argparse.ArgumentParser(
                                description=msg,
                                fromfile_prefix_chars="@",
                                formatter_class=RawTextHelpFormatter)
    parser.add_argument("paths", type=fnmstr, nargs="+")
    parser.add_argument("--opath", type=str, nargs="?", default=None)
    args = parser.parse_args()
    PATHS = args.paths
    OPATH = args.opath
    # main function is in the following
    OPATH_LI = []
    for fpath in PATHS:
        abspath = os.path.abspath(fpath)
        print(abspath)
        if OPATH is not None:
            OPATH_LI.append(abspath + "\n")
    if OPATH is not None:
        with open(OPATH, "w") as write:
            write.writelines(OPATH_LI)
