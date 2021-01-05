#!/usr/bin/env python3


import tempfile
import json


def to_tmpfio_from_lines_li(byte_lines, seek0=True):
    tmp_fio = tempfile.TemporaryFile(mode="w+b")
    tmp_fio.writelines(byte_lines)
    if seek0:
        tmp_fio.seek(0)
    return tmp_fio


def gene_bytelines_from_strlines(strlines):
    for sline in strlines:
        yield sline.encode("utf-8")


def gene_line_with_ncode(strlines):
    for line in strlines:
        yield line + "\n"


def gene_line_striped(line_iter):
    for line in line_iter:
        new_line = line.strip()
        yield new_line


def write_list(tg_list, fpath, mode="w"):
    with open(fpath, mode) as write:
        for one_str in tg_list:
            one_line = one_str + "\n"
            write.write(one_line)


def convert_dict_to_json(dict_ins, json_fpath):
    with open(json_fpath, "w") as write:
        json.dump(dict_ins, write)


def load_dict_from_json(json_fpath):
    with open(json_fpath, "r") as read:
        json_dict = json.load(read)
    return json_dict
