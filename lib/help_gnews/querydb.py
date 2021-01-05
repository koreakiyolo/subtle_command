#!/usr/bin/env python3


from tinydb import TinyDB


class SerarchRow(object):
    def __init__(self):
        self._internal_dict = {}

    def from_interactive(self):
        pass

    def update_word(self, tinydb):
        assert isinstance(tinydb, TinyDB)
        pass
