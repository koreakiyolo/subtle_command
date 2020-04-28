#!/usr/bin/env python3


import os


class ConfirmExt(object):
    def __init__(self, fpath_ext=".png"):
        self.fpath_ext = fpath_ext

    def __call__(self, fnm):
        basenm, ext = os.path.splitext(
                                    fnm)
        if ext != self.fpath_ext:
            emes = "{} has invalid extention:".format(fnm)
            raise TypeError(emes)
        return fnm


class FilterExt(object):
    def __init__(self, fpath_ext=".png"):
        self.fpath_ext = fpath_ext

    def __call__(self, fnms):
        new_fnms = list(
                      self._gene_filtered_fnm(fnms)
                       )
        return new_fnms

    def gene_filtered_fnm(self, files):
        for fnm in files:
            basenm, ext = os.path.splitext(fnm)
            if ext == self.fpath_ext:
                yield fnm


class CompareFilePath(object):
    def __init__(self, ref_paths):
        self.ref_paths_set = self._convert_normal_set_from_paths(
                                                            ref_paths)

    def _convert_normal_set_from_paths(self, paths):
        paths = list(gene_absnormal_path(paths))
        paths_set = set(paths)
        return paths_set

    def ref_minus_target_paths(self, target_paths):
        target_paths_set = self._convert_normal_set_from_paths(
                                                        target_paths)
        ref_minus_target_paths = self.ref_paths_set - target_paths_set
        ref_minus_target_paths = list(ref_minus_target_paths)
        return ref_minus_target_paths


def extract_basenm_in_dirnm(dir_nm):
    fnms = os.listdir(dir_nm)
    base_nm = [os.path.splitext(fnm)[0] for fnm in fnms]
    return base_nm


def gene_normal_path(paths):
    for a_path in paths:
        normed_path = os.path.normpath(a_path)
        yield normed_path


def gene_abs_path(paths):
    for a_path in paths:
        abs_path = os.path.abspath(a_path)
        yield abs_path


def gene_absnormal_path(paths):
    tmp_iter = gene_abs_path(paths)
    iter_absnormal_path = gene_normal_path(tmp_iter)
    return iter_absnormal_path


def replace_ext(fnm, repl_ext):
    basenm, ext = os.path.splitext(fnm)
    new_fpath = basenm + repl_ext
    return new_fpath


def replace_dirnm_of_fpath(self, dname, fpath):
    if not os.path.isdir(dname):
        raise OSError(
                "{} is not directory.".format(dname)
                     )
    new_dname = os.path.abspath(dname)
    abs_fpath = os.path.abspath(fpath)
    _, fnm = os.path.split(abs_fpath)
    new_path = os.path.join(new_dname, fnm)
    return new_path
