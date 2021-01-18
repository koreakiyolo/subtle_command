#!/usr/bin/env python3

import os
import json
import argparse
from argparse import RawTextHelpFormatter

SHELL_BLINE = "{}='{}'"
EXPORT_BLINE = "export {}='{}'"


def get_partial_dict(tot_dict, partial_keys):
    p_key_set = set(partial_keys)
    tot_keys = tot_dict.keys()
    if not p_key_set.issubset(tot_keys):
        ems = "partial_keys:{} must include total_dict.".format(p_key_set)
        raise KeyError(ems)
    partial_dict = {}
    for p_key in partial_keys:
        value = tot_dict[p_key]
        partial_dict[p_key] = value
    return partial_dict


def fnmstr(path_str):
    if not os.path.exists(path_str):
        mes = "{} is not file.".format(
                                    path_str
                                      )
        raise OSError(mes)
    return path_str


class EnvExporter(object):
    def __init__(self, envs_dict=None):
        if envs_dict is None:
            self._internal_envs = os.environ.copy()
        elif isinstance(envs_dict, dict):
            self._internal_envs = envs_dict
        else:
            raise AssertionError("")

    def set_envs_for_python(self):
        keys = ["PATH", "PYTHONPATH"]
        new_envs = get_partial_dict(
                                self._internal_envs,
                                keys)
        self._new_envs = new_envs

    def set_envs_for_designated_keys(self, designated_keys):
        assert isinstance(designated_keys, list)
        new_envs = get_partial_dict(
                            self._internal_envs,
                            designated_keys)
        self._new_envs = new_envs

    @property
    def new_envs(self):
        if hasattr(self, "_new_envs"):
            return self._new_envs
        else:
            return self._internal_envs

    def to_json(self, ojson):
        with open(ojson, "w") as write:
            json.dump(self.new_envs, write)

    def to_export(self, export_file):
        with open(export_file, "w") as write:
            for key, va in self.new_envs.items():
                line = EXPORT_BLINE.format(key, va) + "\n"
                write.write(line)

    def to_shell(self, shell_src):
        with open(shell_src, "w") as write:
            for key, va in self.new_envs.items():
                line = EXPORT_BLINE.format(key, va) + "\n"
                write.write(line)

    @staticmethod
    def from_json(json_file):
        assert os.path.exists(json_file)
        with open(json_file) as read:
            jdict = json.load(read)
            env_exporter = EnvExporter(envs_dict=jdict)
        return env_exporter


if __name__ == "__main__":
    msg = "this program export env variables into a file."\
          "--for_python options output ${PYTHONPATH} and ${PATH}."\
          "output type is selected the following two options. "\
          "--to_json and --to_shell."
    parser = argparse.ArgumentParser(
                            description=msg,
                            fromfile_prefix_chars="@",
                            formatter_class=RawTextHelpFormatter)
    parser.add_argument("--from_json", type=fnmstr, nargs="?", default=None)
    for_opt_args = parser.add_mutually_exclusive_group()
    for_opt_args.add_argument("--for_python", action="store_true",
                              default=False)
    for_opt_args.add_argument("--for_designated_envs", type=str,
                              nargs="*", default=None)
    ex_out_grp = parser.add_mutually_exclusive_group(required=True)
    ex_out_grp.add_argument("--to_json", type=str, nargs="?", default=None)
    ex_out_grp.add_argument("--to_shell", type=str, nargs="?", default=None)
    ex_out_grp.add_argument("--to_export", type=str, nargs="?",
                            default=None)
    args = parser.parse_args()
    FROM_JSON = args.from_json
    FOR_PYTHON = args.for_python
    FOR_DESIGNATED_ENVS = args.for_designated_envs
    TO_JSON = args.to_json
    TO_SHELL = args.to_shell
    TO_EXPORT = args.to_export
    # input options
    if FROM_JSON is not None:
        env_exporter = EnvExporter.from_json(FROM_JSON)
    else:
        env_exporter = EnvExporter()
    # options
    if FOR_PYTHON:
        env_exporter.set_envs_for_python()
    elif FOR_DESIGNATED_ENVS is not None:
        env_exporter.set_envs_for_designated_keys(
                                    FOR_DESIGNATED_ENVS)
    # ouput options.
    if TO_JSON is not None:
        env_exporter.to_json(TO_JSON)
    elif TO_SHELL is not None:
        env_exporter.to_shell(TO_SHELL)
    elif TO_EXPORT is not None:
        env_exporter.to_export(TO_EXPORT)
    else:
        raise AssertionError("")
