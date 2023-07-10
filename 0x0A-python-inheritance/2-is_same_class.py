#!/usr/bin/python3
"""This module checks for exact same boject"""


def is_same_class(obj, a_class):
    """check if the obj is an instance of the specified class

    Args:
        obj: object
        a_class: class

    Returns:
        True (is an instance) False (otherwise)
    """
    if obj.__class__ is a_class:
        return True
    else:
        return False
