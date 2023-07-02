#!/usr/bin/python3
"""This function prints a square with #
"""


def print_square(size):
    """print a square

    Args:
        size: (int) size of the square
    """
    if not isinstance(size, (int, float)):
        raise TypeError("size must be an integer")

    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
