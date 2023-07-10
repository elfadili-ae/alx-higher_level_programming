#!/usr/bin/python3
"""MyList class"""


class MyList(list):
    """MyList subclass"""

    def __init_(self):
        """initialize MyList object"""
        super().__init_()

    def print_sorted(self):
        """print sorted lisst"""
        print(sorted(self))
