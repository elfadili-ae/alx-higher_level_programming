#!/usr/bin/python3
"""This module adds attribute to an object
"""


def add_attribute(obj, attr, value):
    """add an attriute to the object

    Args:
        obj: object
        attr: attribute name
        value: attribute value
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, attr, value)
