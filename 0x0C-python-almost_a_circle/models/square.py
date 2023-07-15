#!/usr/bin/python3
"""Square Module"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """initialize the square"""
        Rectangle.__init__(self, size, size, x, y, id)
        self.__size = size
        self.__x = x
        self.__y = y
        self.id = id

    def __str__(self):
        
