#!/usr/bin/env python3

# formal lib
import argparse
from argparse import RawTextHelpFormatter
# my lib
from help_argparse import ToDtime
from help_gnews import AdminGSerach


if __name__ == "__main__":
    msg = "this program helps to search contents of google news."
    parser = argparse.ArgumentParser(
                                description=msg,
                                fromfile_prefix_chars="@",
                                formatter_class=RawTextHelpFormatter)
    parser.add_argument("queries", type=str, nargs="+")
    ex_args_grp = parser.add_mutually_exclusive_group(required=True)
    ex_args_grp.add_argument("--to_csvs", type=str, nargs="*",
                             default=None)
    ex_args_grp.add_argument("--to_jsons", type=str, nargs="*",
                             default=None)
    ex_args_grp.add_argument("--to_urls", type=str, nargs="*",
                             default=None)
    parser.add_argument("--lang", type=str, default="en", nargs="?")
    parser.add_argument("--days", type=str, default=None)
    parser.add_argument("--start_day", type=ToDtime("%Y/%m/%d"),
                        nargs="?",
                        default=None)
    parser.add_argument("--end_day", type=ToDtime("%Y/%m/%d"),
                        nargs="?", default=None)
    parser.add_argument("--max_page", default=5)
    parser.add_argument("--max_contents", default=100)
    args = parser.parse_args()
    QUERIES = args.queries
    TO_CSVS = args.to_csvs
    TO_JSONS = args.to_jsons
    TO_URLS = args.to_urls
    LANG = args.lang
    DAYS = args.days
    START_DAY = args.start_day
    END_DAY = args.end_day
    admin_gsearch = AdminGSerach(
                             lang=LANG, days=DAYS,
                             start_dtime=START_DAY,
                             end_dtime=END_DAY)
    if TO_CSVS is not None:
        assert len(QUERIES) == len(TO_CSVS)
        for query, ocsv in zip(QUERIES, TO_CSVS):
            admin_gsearch.access(query)
            admin_gsearch.to_csv(ocsv)
            admin_gsearch.clear_gnews_updater()
    elif TO_JSONS is not None:
        assert len(QUERIES) == len(TO_JSONS)
        for query, ojson in zip(QUERIES, TO_JSONS):
            admin_gsearch.access(query)
            admin_gsearch.to_json(ojson)
            admin_gsearch.clear_gnews_updater()
    elif TO_URLS is not None:
        assert len(QUERIES) == len(TO_URLS)
        for query, url_file in zip(QUERIES, TO_URLS):
            admin_gsearch.access(query)
            admin_gsearch.write_URLlinks(url_file)
            admin_gsearch.clear_gnews_updater()
    else:
        raise AssertionError("")
