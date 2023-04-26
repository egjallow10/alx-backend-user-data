#!/usr/bin/env python3
"""Function to filter"""


import re
from typing import List


def filter_datum(
        fields: List[str],
        redaction: str, message: str, separator: str
        ) -> str:
    """returns strings obfuscated"""

    for i in fields:
        message = re.sub(i + "=.*?" + separator,
                         i + "=" + redaction + separator,
                         message)
    return message
