#!/usr/bin/enbv python3


import os
from datetime import datetime


def print_global_varibales():
    glva_dict = globals()
    print_dict = {key: va for key, va in glva_dict
                  if key.isupper()}
    print("== global varibale is in the following. ==")
    print(print_dict)
    print("==========================================")


def to_dtime(string, fmt="%Y/&m/%d"):
    dtime = datetime.strptime(string, fmt)
    return dtime


class ToDtime(object):
    def __init__(self, fmt="%Y/&m/%d"):
        self.fmt = fmt

    def __call__(self, string):
        dtime = datetime.strptime(
                              string,
                              self.fmt)
        return dtime


def fnmstr(path_str):
    if not os.path.exists(path_str):
        mes = "{} is not file.".format(
                                    path_str
                                      )
        raise OSError(mes)
    return path_str


def dirstr(path_str):
    if not os.path.isdir(path_str):
        mes = "{} is not directory.".format(
                                        path_str
                                           )
        raise OSError(mes)
    return path_str


def wio(fnm):
    wio = open(fnm, "w")
    return wio


class OutExtStr(object):
    def __init__(self, ext):
        self.ext = ext

    def __call__(self, argstr):
        os.path.splitext(argstr)
        if argstr == self.ext:
            return str(argstr)
        else:
            emes = "{} doesn't match {}".format(
                                            argstr,
                                            self.ext)
            raise TypeError(emes)


class ArgsDictCaller(object):
    def __init__(self, keys, va_objects):
        if len(keys) != len(va_objects):
            raise TypeError(
                    "keys and va_onbjects's length is not the same"
                           )
        self.args_dict = dict(zip(keys, va_objects))

    def __call__(self, st_wd):
        if st_wd not in self.args_dict:
            meg = "{} doesn't have key:{}".format(
                                              self.args_dict,
                                              st_wd)
            raise KeyError(meg)
        return self.args_dict[st_wd]

    @property
    def keys(self):
        return self.args_dict.keys()


def getenv(env_nm):
    env_dict = os.environ.copy()
    if env_nm not in env_dict:
        emes = "ENV: {} hasn't been definied.".format(
                                                    env_nm)
        raise OSError(emes)
    env_value = env_dict[env_nm]
    return env_value


def env_to_fnmstr(env_nm):
    env_str = getenv(env_nm)
    return fnmstr(env_str)


def env_to_dirstr(env_nm):
    env_str = getenv(env_nm)
    return dirstr(env_str)
