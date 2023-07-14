#!/usr/bin/python3
"""Rectangle Module"""

from models.base import Base


class Rectangle(Base):
    """Rectangle's class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initialize the rectangle object

        Args:
            width: width
            height: height
            x: x pos
            y: y pos
            id: id
        """
        Base.__init__(self, id)
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.width = width

        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.height = height

        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.x = x

        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.y = y

    @property
    def width(self):
        """get the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the width of the rectangle"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """get the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the height of the rectangle"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """get the x of the rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """set the x of the rectangle"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """get the y of the rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """set the y of the rectangle"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """return the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """print the Rectangle"""
        for i in range(self.__y):
            print()

        for i in range(self.__height):
            for k in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """representation of Rectangle"""
        ret = "[Rectangle] ({})".format(self.id)
        ret += " {}/{}".format(self.__x, self.__y)
        ret += " - {}/{}".format(self.__width, self.__height)
        return ret
