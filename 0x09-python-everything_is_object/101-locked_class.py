#!/usr/bin/python3
"""locked class
"""


class LockedClass:
    """prevent user from creating new instance attributes"""

    def __setattr__(self, attr, val):
        """set attribute"""
        if attr != "first_name":
            raise AttributeError(
                "'LockedClass' object has no attribute {}".format(attr)
            )
        else:
            self.__dict__[attr] = val
