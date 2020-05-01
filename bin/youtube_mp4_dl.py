#!/usr/bin/env python3


# formal lib
import subprocess
import argparse
from argparse import RawTextHelpFormatter
import os
# my lib
BASE_CMD = "youtube-dl '{}' --output {}"


def fnmstr(path_str):
    if not os.path.exists(path_str):
        mes = "{} is not file.".format(
                                    path_str
                                      )
        raise OSError(mes)
    return path_str


def download_contents_to_mp4(url, omp4):
    cmd = BASE_CMD.format(url, omp4)
    popen_ins = subprocess.Popen(cmd, shell=True,
                                 env=os.environ.copy())
    popen_ins.communicate()


class FpathtoDropbox(object):
    def __init__(self, dropbox_path=None):
        if dropbox_path is None:
            self.dropbox_path = os.environ["DROPBOXPATH"]
        else:
            if os.path.exists(dropbox_path):
                self.dropbox_path = dropbox_path
            else:
                raise OSError("invalid dropbox_path is entered.")

    def __call__(self, path):
        if os.path.basename(path) == path:
            outpath = os.path.join(
                            self.dropbox_path,
                            path)
        else:
            outpath = path

        return outpath


if __name__ == "__main__":
    msg = "this program download mp4"
    parser = argparse.ArgumentParser(
                                description=msg,
                                fromfile_prefix_chars="@",
                                formatter_class=RawTextHelpFormatter)
    parser.add_argument("dl_urls", type=str, nargs="+")
    parser.add_argument("--off_dbox", action="store_true", default=False)
    parser.add_argument("--outmp4s", type=str, nargs="+", required=True)
    args = parser.parse_args()
    DL_URLS = args.dl_urls
    OFF_DBOX = args.off_dbox
    OUTMP4S = args.outmp4s
    if len(DL_URLS) != len(OUTMP4S):
        raise AssertionError("")
    fpathtodbox = FpathtoDropbox()
    for url, omp4 in zip(DL_URLS, OUTMP4S):
        if not OFF_DBOX:
            converted_omp4 = fpathtodbox(omp4)
        else:
            converted_omp4 = omp4
        download_contents_to_mp4(url, converted_omp4)
