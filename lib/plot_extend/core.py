#!/usr/bin/env python3


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from itertools import cycle


COLOR_LI = ["b", "g", "r", "k", "c", "m", "y", "b"]
MARKER_LI = ["o", "H", "<", ">", "D", "s", "^", "V"]
LINE_STYLES_TYPES = ["--", "-", ":", "-."]


def color_gene():
    for col in cycle(COLOR_LI):
        yield col


def marker_gene():
    for mark in cycle(MARKER_LI):
        yield mark


def plot_symbol_gene(line_style):
    if line_style not in LINE_STYLES_TYPES:
        raise TypeError("line_style is invalid arg")
    for marker, color in  zip(marker_gene(),
                              color_gene()):
        symbol = color + line_style + marker
        yield symbol


COLOR_ITER = color_gene()
MARKER_ITER = marker_gene()


def reset_iter():
    global COLOR_ITER
    COLOR_ITER = color_gene()
    global MARKER_ITER
    MARKER_ITER = marker_gene()


def file_plot(fpath, label=None, color=None, marker=None,
              xminmax=(None, None), yminmax=(None, None)):
    if color is None:
        color = next(COLOR_ITER)
    if marker is None:
        marker = next(MARKER_ITER)
    tmp_ars = np.loadtxt(fpath)
    x_ar = tmp_ars[:, 0]
    y_ar = tmp_ars[:, 1]
    plt.plot(x_ar, y_ar, marker=marker, color=color, label=label)
    plt.xlim(*xminmax)
    plt.ylim(*yminmax)


def file_plot_act_kwargs(fpath, *args, **kargs):
    tmp_ar = np.loadtxt(fpath)
    x_ar = tmp_ar[:, 0]
    y_ar = tmp_ar[:, 1]
    plt.plot(x_ar, y_ar, *args ,**kwargs)


def file_plot_act_colnum(fpath, *args, x_colnum=0, y_colnum=1,
                         **kargs):
    tmp = np.loadtxt(fpath)
    x_ar = tmp[:, x_colnum]
    y_ar = tmp[:, y_colnum]
    plt.scatter(x_ar, y_ar,
                *args, **kwargs)


def file_scatter_act_kwargs(fpath, *args, **kargs):
    tmp_ar = np.loadtxt(fpath)
    x_ar = tmp_ar[:, 0]
    y_ar = tmp_ar[:, 1]
    plt.scatter(x_ar, y_ar, *args ,**kwargs)


def make_legened(*labels, fontsize=24,
                 color_iter=COLOR_ITER, marker_iter=MARKER_ITER):
    for label in labels:
        color = next(color_iter)
        marker = next(marker_iter)
        plt.plot(0, 0, marker=marker,
                 color=color, label=label)
    plt.legend(fontsize=24)


def make_rectangle(xminmax, yminmax, edge_color="r", fill=False):
    xmin, xmax = xminmax
    xwidth = xmax - xmin
    ymin, ymax = yminmax
    yheight = ymax - ymin
    rec_ins = patches.Rectangle(xy=(xmin, ymin),
                                width=xwidth, height=yheight,
                                ec=edge_color, fill=fill)
    return rec_ins


class ColorMarker(object):
    def __init__(self, color_li=COLOR_LI):
        pass

    def _set_color_cycle(self):
        self.color_cycle = cycle(self.color_li)

    def _set_color_dict(self):
        tmp = enumerate(self.color_li)
        self.color_dict = dict(tmp)
        self.color_id_li = self.color_dict.keys()

    def cnvt_str_to_csymbol(self, str_sym):
        if str_sym not in self.color_li:
            err_mes = "str_sym is invalid:{}".format(str_sym)
            raise TypeError(err_mes)
        return str_sym

    def cnvt_id_to_csymbol(self, num_id):
        csymbol = self.color_dict[num_id]
        return csymbol

    def gene_csymbol_and_condar_act_col_idar(self, col_idar):
        if col_idar.dtype != np.int64:
            raise TypeError("")

    def __next__(self):
        return next(self.color_cycle)

    def __iter__(self):
        return self.color_cycle
