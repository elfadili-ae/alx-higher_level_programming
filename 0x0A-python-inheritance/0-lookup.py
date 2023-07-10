#!/usr/bin/python3
"""This Module lists all available
attributes and methods of an object
"""


def lookup(obj):
    """list attributes and methods of an object

    Args:
        obj: object

    Returns:
        list of attributes and methods
    """
    return dir(obj)
