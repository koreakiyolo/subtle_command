#!/usr/bin/env python3


# formal lib
import subprocess
import argparse
from argparse import RawTextHelpFormatter
import os
import pdfkit
import pyperclip
# my lib


def fnmstr(path_str):
    if not os.path.exists(path_str):
        mes = "{} is not file.".format(
                                    path_str
                                      )
        raise OSError(mes)
    return path_str


class FpathtoDropbox(object):
    def __init__(self, dropbox_path=None):
        if dropbox_path is None:
            self.dropbox_path = os.environ[
                                    "ICLOUDPATH_PDF"]
        else:
            if os.path.exists(dropbox_path):
                self.dropbox_path = dropbox_path
            else:
                raise OSError(
                       "invalid dropbox_path is entered.")

    def __call__(self, path):
        if os.path.basename(path) == path:
            outpath = os.path.join(
                            self.dropbox_path,
                            path)
        else:
            outpath = path
        return outpath


def download_pdf_from_url(self):
    pass



if __name__ == "__main__":
    msg = "this program download mp4"
    parser = argparse.ArgumentParser(
                            description=msg,
                            fromfile_prefix_chars="@",
                            formatter_class=RawTextHelpFormatter)
    ex_args_grp = parser.add_mutually_exclusive_group(
                                            required=True)
    ex_args_grp.add_argument("--dl_urls", type=str, nargs="+",
                             default=None)
    ex_args_grp.add_argument("--clip_board", action="store_true",
                             default=False)
    parser.add_argument("--off_share_cloud", action="store_true",
                        default=False)
    parser.add_argument("--outpdf", type=str, nargs="?", required=True)
    args = parser.parse_args()
    DL_URLS = args.dl_urls
    CLIP_BOARD = args.clip_board
    OFF_SHARE_CLOUD = args.off_share_cloud
    OUTPDF = args.outpdf
    fpathtodbox = FpathtoDropbox()
    if OFF_SHARE_CLOUD:
        opdf = OUTPDF
    else:
        opdf = fpathtodbox(OUTPDF)
    if DL_URLS is not None:
        pdfkit.from_url(DL_URLS, opdf)
    elif CLIP_BOARD:
        copied_urls = pyperclip.paste()
        pdfkit.from_url(copied_urls, opdf)
    else:
        raise AssertionError()
