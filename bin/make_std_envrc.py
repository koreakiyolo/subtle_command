#!/usr/bin/env python3


# formal lib
import os
import argparse
from argparse import RawDescriptionHelpFormatter
# my lib
EXPORT_PATH = "export PATH=${PATH}:"
EXPORT_PYTHONPATH = "export PYTHONPATH=${PYTHONPATH}:"


def dirstr(path_str):
    if not os.path.isdir(path_str):
        mes = "{} is not directory.".format(
                                        path_str
                                           )
        raise OSError(mes)
    return path_str


if __name__ == "__main__":
    msg = "this program make .envrc"
    parser = argparse.ArgumentParser(
                                description=msg,
                                formatter_class=RawDescriptionHelpFormatter)
    parser.add_argument("--dpath", type=dirstr, default="./", nargs="?")
    args = parser.parse_args()
    DPATH = args.dpath
    cond1 = os.path.exists("./bin")
    cond2 = os.path.exists("./lib")
    if not (cond1 and cond2):
        raise AssertionError("bin or lib isn't existing.")
    ENVRC_PATH = os.path.join(DPATH, ".envrc")
    ENVRC_PATH = os.path.abspath(ENVRC_PATH)
    LIB_PATH = os.path.abspath(
                        os.path.join(DPATH, "lib")
                              )
    BIN_PATH = os.path.abspath(
                        os.path.join(DPATH, "bin")
                              )
    PATH_LINE = EXPORT_PATH + BIN_PATH + "\n"
    PYTHONPATH_LINE = EXPORT_PYTHONPATH + LIB_PATH + "\n"
    with open(ENVRC_PATH, "w") as write:
        write.write(PATH_LINE)
        write.write(PYTHONPATH_LINE)
