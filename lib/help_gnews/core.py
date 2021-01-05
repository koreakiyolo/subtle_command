#!/usr/bin/env python3


from GoogleNews import GoogleNews
from datetime import datetime
from pandas import DataFrame
import json
import io


class DictWordChecker(object):
    def __init__(self, key, words):
        self._key = key
        self._words = words

    def __call__(self, tg_dict):
        assert isinstance(tg_dict, dict)
        assert self._key in tg_dict
        tg_word = tg_dict[self._key]
        for wd in self._words:
            if wd in tg_word:
                return False
        return True


class AdminGSerach(object):
    def __init__(self, lang="en",
                 days=3, start_dtime=None,
                 end_dtime=None):
        self._lang = lang
        self._set_days(days)
        self._start = self._get_dtime_string(start_dtime)
        self._end = self._get_dtime_string(end_dtime)
        self._gnews_updaters = []
        self._rapped_results = []

    def _set_days(self, days_or_none):
        if days_or_none is None:
            self._days = None
        elif isinstance(days_or_none, int):
            self._days = "{}d".format(days_or_none)
        else:
            raise AssertionError("")

    def _get_dtime_string(self, dtime):
        if dtime is None:
            return None
        assert isinstance(dtime, datetime)
        dtime_string = dtime.strptime("%m/%d/%Y")
        return dtime_string

    def _set_gnews_updater(self):
        gnews = GoogleNews(
                       lang=self._lang,
                       period=self._days,
                       start=self._start,
                       end=self._end,
                       encode="utf-8")
        self._gnews_updater = gnews

    def access(self, search_q,
               max_pages=5, max_contents=100):
        self._set_gnews_updater()
        self._gnews_updater.search(search_q)
        old_cont_num = 0
        for i in range(max_pages):
            self._gnews_updater.get_page(i)
            cont_num = len(self._gnews_updater.get_links())
            if cont_num > max_contents:
                break
            elif old_cont_num == cont_num:
                break
            old_cont_num = cont_num
        self._set_total_datadict()

    def clear_gnews_updater(self):
        self._gnews_updater = None

    def _merge_URL_links(self):
        links = self._gnews_updater.get_links()
        return links

    def _set_total_datadict(self):
        gnews = self._gnews_updater
        self._set_datadict_from_gnews(gnews)

    def _set_datadict_from_gnews(self, gnews):
        assert isinstance(gnews, GoogleNews)
        results = gnews.results(sort=True)
        lang = gnews._GoogleNews__lang
        for result in results:
            data_dict = {}
            data_dict["lang"] = lang
            data_dict["title"] = result["title"]
            data_dict["link"] = result["link"]
            data_dict["media"] = result["media"]
            data_dict["datetime"] = result["datetime"]
            data_dict["date"] = result["date"]
            self._rapped_results.append(data_dict)

    def write_URLlinks(self, fpath):
        url_links = self._merge_URL_links()
        with open(fpath, "w") as write:
            for url in url_links:
                write.write(url + "\n")

    def to_csv(self, ocsv):
        df = DataFrame(self._rapped_results)
        if isinstance(ocsv, io.TextIOWrapper):
            write = ocsv
            df.to_csv(write)
        elif isinstance(ocsv, str):
            df.to_csv(ocsv)
        else:
            raise AssertionError("")

    def to_json(self, ojson):
        ddict_list = self._rapped_results
        if isinstance(ojson, io.TextIOWrapper):
            write = ojson
            json.dump(ddict_list, write)
        elif isinstance(ojson, str):
            with open(ojson, "w") as write:
                json.dump(ddict_list, write)
        else:
            raise AssertionError("")
