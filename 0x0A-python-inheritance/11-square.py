#!/usr/bin/python3
"""currently empty class"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size):
        """initialize the square

        Args:
            size: size of the square
        """
        self.integer_validator("size", size)
        self.__size = size
        Rectangle.__init__(self, size, size)

    def area(self):
        """area of the suare

        Returns:
            area
        """
        return self.__size * self.__size

    def __str__(self):
        """represent a square

        Returns:
            representation of a square
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
