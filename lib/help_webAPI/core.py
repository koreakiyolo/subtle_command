#!/usr/bin/env python3


import urllib
from urllib.parse import ParseResult


def get_query_dict_from_URL(URL_string):
    parse_result = urllib.parse.urlparse(
                                    URL_string)
    query_string = parse_result.query
    query_dict = urllib.parse.parse_qs(
                                    query_string)
    return query_dict


def replace_query_dict(parse_result, query_dict):
    assert isinstance(parse_result, ParseResult):
    assert isinstance(query_dict, dict)
    parse_result._replace(
                      query=urllib.parse.urlencode(
                      query_dict, doseq=True))
    return parse_result


def make_url(parse_result):
    assert isinstance(parse_result, ParseResult)
    url = urllib.parse.urlunparseparse_result)
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
    def __init__(self, ):
        pass

    @staticmethod
    def from_url(string)
        pass

    def write_query_json(self):
        pass

    def load_query_json(self):
        pass

    def reset_query_dict(self):
        pass
