#!/usr/bin/python3
"""This module defines a Rectangle"""


class Rectangle:
    """represents a rectangle"""

    def __init__(self, width=0, height=0):
        """initialize rectangle"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """get width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value: int):
        """set the width of the rectangle"""

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """get height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value: int):
        """set the height of the rectangle"""

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """area of the rectangle

        Returns:
            area = width x height
        """

        return self.__width * self.__height

    def perimeter(self):
        """perimeter of the rectangle

        Returns:
            perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0

        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """print rectangle"""
        rect = ""
        if self.height == 0 or self.width == 0:
            return rect

        for i in range(0, self.height):
            for j in range(0, self.width):
                rect += "#"
            if i < self.height - 1:
                rect += "\n"
        return rect
