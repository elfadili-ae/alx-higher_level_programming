#!/usr/bin/python3
"""
This a square module.
"""


class Square:
    """
    represents a Square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a Square.

        Args:
            size (int): size of the square.
            position (tuple): square position.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """set/get the position."""
        return self.__position

    @position.setter
    def position(self, value):
        if (
            not (isinstance(value, tuple))
            or len(value) != 2
            or not all(isinstance(val, int) for val in value)
            or not all(val >= 0 for val in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """
        print in stdout the square.
        """
        if self.__size == 0:
            print("")
            return

        for i in range(0, self.__position[1]):
            print("")
        for i in range(self.__size):
            for j in range(0, self.__position[0]):
                print(" ", end="")
            for k in range(0, self.__size):
                print("#", end="")
            print("")
