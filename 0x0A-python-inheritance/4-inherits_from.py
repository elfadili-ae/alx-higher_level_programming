#!/usr/bin/python3
"""This module checks if an object is an instance
of a class that inherited from a specified class
"""


def inherits_from(obj, a_class):
    """check if obj inherits from a_class

    Args:
        obj: object
        a_class: class

    Returns:
        True (inherits) False (otherwise)
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
