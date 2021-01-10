#!/usr/bin/env python3


import pyperclip
import argparse
from argparse import RawTextHelpFormatter
import time


class ClipBoardCollector(object):
    def __init__(self, wpath, interval_time):
        self._write = open(wpath, "w")
        self._interval_time = interval_time
        self._internal_set = set([])

    def run(self):
        pyperclip.copy("")
        while True:
            try:
                word = pyperclip.paste()
                if word != "":
                    self._internal_set.add(word)
                    time.sleep(self._interval_time)
            except KeyboardInterrupt:
                break
        for va in self._internal_set:
            if not isinstance(va, str):
                continue
            line = va + "\n"
            self._write.write(line)
        self._write.close()
        print("normally finished.")


if __name__ == "__main__":
    msg = "snipet script save all copy contents for a certain period"
    parser = argparse.ArgumentParser(
                            description=msg,
                            fromfile_prefix_chars="@",
                            formatter_class=RawTextHelpFormatter)
    parser.add_argument("wpath", type=str, nargs="?")
    parser.add_argument("--interval_time", type=int,
                        nargs="?", default=0.01)
    args = parser.parse_args()
    WPATH = args.wpath
    INTERVAL_TIME = args.interval_time
    clip_collector = ClipBoardCollector(WPATH, INTERVAL_TIME)
    clip_collector.run()
