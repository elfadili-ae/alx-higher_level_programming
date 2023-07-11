#!/usr/bin/python3
"""This module returns the JSON representation
of an object
"""

import json


def to_json_string(my_obj):
    """return the JSON representation of the object

    Args:
        my_obj: object

    Returns:
        JSON representation
    """
    return json.dumps(my_obj)
