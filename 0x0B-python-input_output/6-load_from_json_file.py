#!/usr/bin/python3
"""This module creates an object from Json file
"""

import json
from io import StringIO


def load_from_json_file(filename):
    """create an object from json file

    Args:
        filename: file's name
    Return:
        created object
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(StringIO(f.read()))
