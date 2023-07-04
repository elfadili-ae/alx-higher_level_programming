#!/usr/bin/python3
"""locked class
"""


class LockedClass:
    """prevent user from creating new instance attributes"""
    __slots__ = ['first_name']
