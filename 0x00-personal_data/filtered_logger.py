#!/usr/bin/env pyhthon3
"""filters a logged file"""


import re


def filter_datum(fields, redaction, message, separator) -> str:
    """filters a logged file"""
    pattern = r'(' + '|'.join(re.escape(field) for field in fields) + r')=[^' + re.escape(separator) + r']*'
    return re.sub(pattern, lambda m: m.group().split('=')[0] + '=' + redaction, message)
