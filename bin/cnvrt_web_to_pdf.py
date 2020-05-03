#!/usr/bin/env python3

# formal lib
import os
import argparse
from argparse import RawTextHelpFormatter
import pdfkit
import json
# my lib
from gmail import AdminGmail
from gmail import ContFpathMimetype

env_dict = os.environ.copy()
HOME_PATH = env_dict["HOME"]
DEFAULT_SETTING_PATH = os.path.join(
                                  HOME_PATH,
                                  "/Users/haruyuki/.__setting/kindle.json")
GMAIL_ACCOUNT_KEY = "gmail_account"
GMAIL_PASSWD_KEY = "gmail_passwd"
KINDLE_ADDRESS_KEY = "to_kindle_address"
G_PDF_OPTIONS = {}
G_PDF_OPTIONS["page-size"] = "A4"
G_PDF_OPTIONS["margin-top"] = "0.1in"
G_PDF_OPTIONS["margin-right"] = "0.1in"
G_PDF_OPTIONS["margin-left"] = "0.1in"
G_PDF_OPTIONS["margin-bottom"] = "0.1in"
G_PDF_OPTIONS["no-outline"] = None
G_PDF_OPTIONS["disable-smart-shrinking"] = ""


def fnmstr(path_str):
    if not os.path.exists(path_str):
        mes = "{} is not file.".format(
                                    path_str
                                      )
        raise OSError(mes)
    return path_str


def send_pdf_to_kindle(opdf, delete=True,
                       kindle_setfile=DEFAULT_SETTING_PATH):
    input_dict = json.load(open(kindle_setfile))
    g_account = input_dict[GMAIL_ACCOUNT_KEY]
    g_pass = input_dict[GMAIL_PASSWD_KEY]
    to_kindle_addr = input_dict[KINDLE_ADDRESS_KEY]
    admin_gmail_ins = AdminGmail(g_account, g_pass)
    cont_with_fpath_and_myme = ContFpathMimetype(OPDFS)
    admin_gmail_ins.set_origcont_with_path_myme(
                                    cont_with_fpath_and_myme)
    admin_gmail_ins.set_attachment_mimes_li()
    admin_gmail_ins.set_msg_with_attachment(g_account, to_kindle_addr)
    admin_gmail_ins.send()
    if delete:
        os.remove(opdf)


if __name__ == "__main__":
    msg = "this program convert a web page with html and css to one pdf file."
    parser = argparse.ArgumentParser(
                                description=msg,
                                fromfile_prefix_chars="@",
                                formatter_class=RawTextHelpFormatter)
    ex_args_grp = parser.add_mutually_exclusive_group(required=True)
    ex_args_grp.add_argument("--urls", type=str, nargs="*", default=None)
    ex_args_grp.add_argument("--html_and_css", type=fnmstr, nargs=2,
                             default=None)
    parser.add_argument("--opdfs", type=str, nargs="+", required=True)
    parser.add_argument("--to_kindle", action="store_true", default=False)
    parser.add_argument(
                    "--jsonsetting", type=fnmstr, nargs="?",
                    default=DEFAULT_SETTING_PATH)
    args = parser.parse_args()
    URLS = args.urls
    HTML_AND_CSS = args.html_and_css
    OPDFS = args.opdfs
    TO_KINDLE = args.to_kindle
    JSONSETTING = args.jsonsetting
    # output pdfs from web pages.
    if URLS is not None:
        if len(URLS) != len(OPDFS):
            emes = "URLS and OPDFS's lengths must be the same."
            raise AssertionError(emes)
        for url, opdf in zip(URLS, OPDFS):
            pdfkit.from_url(url, opdf, options=G_PDF_OPTIONS)
            if TO_KINDLE:
                send_pdf_to_kindle(opdf, delete=True,
                                   kindle_setfile=JSONSETTING)

    elif HTML_AND_CSS is not None:
        if len(OPDFS) != 1:
            raise AssertionError(
                    "OPDF must include only one string.")
        HTML_FILE, CSS_FILE = HTML_AND_CSS
        opdf = OPDFS[0]
        pdfkit.from_file(HTML_FILE, opdf, css=CSS_FILE,
                         options=G_PDF_OPTIONS)
        send_pdf_to_kindle(opdf, delete=True,
                           kindle_setfile=JSONSETTING)
    else:
        raise AssertionError("")
