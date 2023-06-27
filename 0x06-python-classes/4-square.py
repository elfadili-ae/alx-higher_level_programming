#!/usr/bin/python3
"""
This a square module.
"""


class Square:
    """
    represents a Square.
    """

    def __init__(self, size=0):
        """
        Initialize a Square.

        Args:
            length (int): size of the square.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        the area of the square.

        Returns:
            the square area.
        """
        return self.__size * self.__size

    @property
    def size(self):
        """
        get the size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        set the size of the square.

        Args:
            value (int): size value.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
