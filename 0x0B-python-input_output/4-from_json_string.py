#!/usr/bin/python3
"""This module parses json to an object
"""

import json


def from_json_string(my_str):
    """parse json string to an object

    Args:
        my_str: json string

    Returns:
        parsed object
    """
    return json.loads(my_str)
