#!/usr/bin/env python3
"""Function to filter"""
import re


def filter_datum(fields, redaction, message, separator):
    """Function that returns the log message obfuscated"""
    return re.sub('|'.join(fields)
                  + r'=[^{}]+'.format(separator), redaction, message)
