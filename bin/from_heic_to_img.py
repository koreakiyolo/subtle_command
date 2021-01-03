#!/usr/bin/env python3


# formal lib
import argparse
from argparse import RawTextHelpFormatter
from PIL import Image
import os
import pyheif
# my lib


def dirstr(path_str):
    if not os.path.isdir(path_str):
        mes = "{} is not directory.".format(
                                        path_str
                                           )
        raise OSError(mes)
    return path_str


def fnmstr(path_str):
    if not os.path.exists(path_str):
        mes = "{} is not file.".format(
                                    path_str
                                      )
        raise OSError(mes)
    return path_str


def cnvrt_heic_to_img(image_path, save_path, fmt=None):
    heif_file = pyheif.read(image_path)
    data = Image.frombytes(
        heif_file.mode,
        heif_file.size,
        heif_file.data,
        "raw",
        heif_file.mode,
        heif_file.stride,
        )
    data.save(save_path, fmt=None)


if __name__ == "__main__":
    msg = "this program helps to "
    parser = argparse.ArgumentParser(
                                description=msg,
                                fromfile_prefix_chars="@",
                                formatter_class=RawTextHelpFormatter)
    parser.add_argument("heics", type=fnmstr, nargs="+")
    ex_args_grp = parser.add_mutually_exclusive_group(required=True)
    ex_args_grp.add_argument("--opaths", type=str, nargs="+", default=None)
    ex_args_grp.add_argument("--auto_jpeg", type="store_true",
                             default=False)
    ex_args_grp.add_argument("--auto_png", type="store_true",
                             default=False)
    parser.add_argument("--odir", type=dirstr, nargs="?", default=None)
    args = parser.parse_args()
    HEICS = args.heics
    OPATHS = args.opaths
    ODIR = args.odir
    AUTO_JPEG = args.auto_jpeg
    AUTO_PNG = args.auto_png
    if OPATHS is not None:
        assert len(OPATHS) == len(HEICS)
        for ipath, opath in zip(HEICS, OPATHS):
            cnvrt_heic_to_img(ipath, opath)
    elif AUTO_JPEG:
        # replacer_ext
        for ipath in HEICS:
            opath = replacer_ext(ipath)
            if ODIR is not None:
                opath = replacer_dir(opath)
            cnvrt_heic_to_img(ipath, opath)
    elif AUTO_PNG:
        for ipath in HEICS:
            opath = replacer_ext(ipath)
            if ODIR is not None:
                oapth = replacer_dir(opath)
            cnvrt_heic_to_img(ipath, opath)
    else:
        raise AssertionError("")
