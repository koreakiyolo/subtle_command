#!/usr/bin/env python3

# formal lib
import argparse
from argparse import RawTextHelpFormatter
import subprocess
import os
# my lib
from more_itertools import consume


def fnmstr(path_str):
    if not os.path.exists(path_str):
        mes = "{} is not file.".format(
                                    path_str
                                      )
        raise OSError(mes)
    return path_str


def check_type_list(target_li, type_ob=str):
    for ob in target_li:
        assert isinstance(ob, type_ob)


def check_files(pdf_files):
    for pdf in pdf_files:
        assert os.path.exists(pdf)


def input_wcontent():
    input_list = []
    while True:
        num = input("cost?:(#:fin_code):")
        if num.isdigit():
            input_list.append(num)
        elif num == "#":
            break
        else:
            warning_mes = "you must input digit or #."
            print(warning_mes)
    wcontent = "\n".join(input_list)
    return wcontent


class ArangeExpenseIterator(object):
    def __init__(self, pdf_files):
        self.pdf_files = pdf_files

    def _set_pdf_files(self, pdf_files):
        check_type_list(pdf_files, str)
        check_files(pdf_files)
        self.pdf_files = pdf_files

    def write_expenses_into_path(self, wpath):
        wcontent = input_wcontent()
        with open(wpath, "w") as write:
            write.write(wcontent)

    def _from_pdf_into_txt(self, pdf):
        abs_path = os.path.abspath(pdf)
        without_ext = os.path.splitext(abs_path)[0]
        txtpath = without_ext + ".txt"
        return txtpath

    def _open_pdf(self, pdf):
        assert os.path.exists(pdf)
        cmd = "open {}".format(pdf)
        subprocess.run(cmd, shell=True, env=os.environ.copy())

    def _coroutine_write_info(self):
        start_base = "start writing into {}"
        end_mes = "finish writing."
        for pdf in self.pdf_files:
            self._open_pdf(pdf)
            txt_path = self._from_pdf_into_txt(pdf)
            start_mes = start_base.format(txt_path)
            print(start_mes)
            self.write_expenses_into_path(txt_path)
            print(end_mes)
            yield

    def run(self):
        tmp_itr = self._coroutine_write_info()
        consume(tmp_itr)


if __name__ == "__main__":
    msg = "this program makes"
    parser = argparse.ArgumentParser(
                                description=msg,
                                formatter_class=RawTextHelpFormatter,
                                fromfile_prefix_chars="@")
    parser.add_argument("pdf_files", type=fnmstr, nargs="*")
    args = parser.parse_args()
    PDF_FILES = args.pdf_files
    organizer_expenses = ArangeExpenseIterator(PDF_FILES)
    organizer_expenses.run()
