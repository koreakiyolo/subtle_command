#!/usr/bin/env python3


# formal lib
import subprocess
import argparse
from argparse import RawTextHelpFormatter
import os
# my lib
BASE_CMD = "youtube_dl --extract-audio '{}' --output {}"


def fnmstr(path_str):
    if not os.path.exists(path_str):
        mes = "{} is not file.".format(
                                    path_str
                                      )
        raise OSError(mes)
    return path_str


def download_contents_to_mp3(url, omp3):
    cmd = BASE_CMD.format(url, omp3)
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
    parser.add_argument("dl_url", type=str, nargs="+")
    parser.add_argument("--off_dbox", action="store_true", default=False)
    parser.add_argument("--outmp3s", type=str, nargs="+", required=True)
    args = parser.parse_args()
    DL_URLS = args.dl_urls
    OFF_DBOX = args.off_dbox
    OUTMP3S = args.outmp3s
    if len(DL_URLS) != len(OUTMP3S):
        raise AssertionError("")
    fpathtodbox = FpathtoDropbox()
    for url, omp3 in zip(DL_URLS, OUTMP3S):
        converted_omp3 = fpathtodbox(omp3)
        download_contents_to_mp3(url, converted_omp3)
