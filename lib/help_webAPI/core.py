#!/usr/bin/env python3

import urllib


def get_query_dict_from_URL(URL_string):
    parse_result = urllib.parse.urlparse(
                                    URL_string)
    query_string = parse_result.query
    query_dict = urllib.parse.parse_qs(
                                    query_string)
    return query_dict


def get_quoted_URL(url_p):
    quoted_url = urllib.parse.quote(
                                url_p)
    return quoted_url


def get_unquoted_URL(quoted_url):
    quoted_url = urllib.parse.unquote(
                                quoted_url)
    return quoted_url
