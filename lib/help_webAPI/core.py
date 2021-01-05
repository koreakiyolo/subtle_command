#!/usr/bin/env python3


import urllib
from urllib.parse import ParseResult
import json


def get_query_dict_from_URL(URL_string):
    parse_result = urllib.parse.urlparse(
                                    URL_string)
    query_string = parse_result.query
    query_dict = urllib.parse.parse_qs(
                                    query_string)
    return query_dict


def replace_query_dict(parse_result, query_dict):
    assert isinstance(parse_result, ParseResult)
    assert isinstance(query_dict, dict)
    parse_result._replace(
                      query=urllib.parse.urlencode(
                                    query_dict, doseq=True)
                         )
    return parse_result


def make_url(parse_result):
    assert isinstance(parse_result, ParseResult)
    url = urllib.parse.urlunparse(parse_result)
    return url


def get_quoted_URL(url_p):
    quoted_url = urllib.parse.quote(
                                url_p)
    return quoted_url


def get_unquoted_URL(quoted_url):
    quoted_url = urllib.parse.unquote(
                                quoted_url)
    return quoted_url


class QueryReplacer(object):
    def __init__(self, parse_result):
        assert isinstance(parse_result, ParseResult)
        self._parse_result = parse_result

    @staticmethod
    def from_url(url):
        parse_result = urllib.parse.urlparse(url)
        return QueryReplacer(parse_result)

    @property
    def query_dict(self):
        query_string = self._parse_result.query
        query_dict = urllib.parse.parse_qs(query_string)
        return query_dict

    @property
    def URL(self):
        url = make_url(self._parse_result)
        return url

    def write_query_json(self, ojson):
        with open(ojson, "w") as write:
            json.dump(self.query_dict, write)

    def load_query_json(self, rjson):
        with open(rjson, "r") as read:
            json_dict = json.load(read)
        self.reset_query_dict(json_dict)

    def reset_query_dict(self, query_dict):
        assert isinstance(query_dict, dict)
        replace_query_dict(self._parse_result,
                           query_dict)
