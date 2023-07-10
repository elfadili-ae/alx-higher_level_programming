#!/usr/bin/python3
"""This module checks for exact same object"""


def is_kind_of_class(obj, a_class):
    """check if the obj is an instance of an object
       or if it's an instance of a class

    Args:
        obj: object
        a_class: class

    Returns:
        True (is an instance) False (otherwise)
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
