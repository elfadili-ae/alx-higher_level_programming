#!/usr/bin/python3
"""This function calculates the addition of two integers
"""


def add_integer(a, b=98):
    """return the addition of a and b

    Args:
    a (int): first number
    b (int): second number

    Return:
    return the addition of a and b
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
