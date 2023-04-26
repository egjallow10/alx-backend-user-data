#!/usr/bin/env python3
"""Function to filter"""


import re


def filter_datum(fields, redaction, message, separator):
    """Funtion that return a string"""
    pattern = r'({0})=([^{1}]+)'.format('|'.join(fields), separator)
    return re.sub(pattern, r'\1={0}{1}'.format(redaction, separator), message)
