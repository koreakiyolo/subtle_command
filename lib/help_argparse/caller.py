#!/usr/bin/env python3


import os


class FilePathConverter(object):
    def __init__(self, common_src, common_dst,
                 src_confirm=False, dst_confirm=False,
                 src_abs=False, dst_abs=False):
        self.src_confirm = src_confirm
        self.dst_confirm = dst_confirm
        self.src_abs = src_abs
        self.dst_abs = dst_abs
        self._set_common_dst(common_dst)
        self._set_common_src(common_src)

    def _set_common_src(self, common_src):
        if self.src_confirm:
            if not os.path.exists(common_src):
                emes = "common_src isn't existing."
                raise OSError(emes)
        if self.src_abs:
            common_src = os.path.abspath(common_src)
        self.common_src = common_src

    def _set_common_dst(self, common_dst):
        if self.dst_confirm:
            if not os.path.exists(common_dst):
                emes = "common_dst"
                raise OSError(emes)
        if self.dst_abs:
            common_dst = os.path.abspath(common_dst)
        self.common_dst = common_dst

    def __call__(self, path):
        self._confirm_tgpath(path)
        converted_path = path.replace(
                                    self.common_src,
                                    self.common_dst)
        return converted_path

    def _confirm_tgpath(self, path):
        if path.find(self.common_src) != 0:
            emes = "invalid path is entered.\n"\
                   "path must match self.common_src from an initial"\
                   "character.\n"\
                   "commonpath_src:{}".format(self.common_src)
            raise AssertionError(emes)
