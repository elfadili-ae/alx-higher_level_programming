#!/usr/bin/python3
""" inherits from int
"""


class MyInt(int):
    """MyInt class"""

    def __eq__(self, otro):
        """Determineth wheth'r this object is ylike
        unto anoth'r.
        """
        return int.__ne__(self, otro)

    def __ne__(self, otro):
        """Determineth wheth'r this object is not ylike
        unto anoth'r
        """
        return int.__eq__(self, otro)
