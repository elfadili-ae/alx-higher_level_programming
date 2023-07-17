#!/usr/bin/python3
"""Square Module"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """initialize the square"""
        Rectangle.__init__(self, size, size, x, y, id)

    @property
    def size(self):
        """get the size"""
        return self.width

    @size.setter
    def size(self, value):
        """set the size of the Square"""
        self.width = value
        self.height = value

    def __str__(self):
        """representation of Square"""
        ret = "[Square] ({})".format(self.id)
        ret += " {}/{}".format(self.x, self.y)
        ret += " - {}".format(self.width)
        return ret

    def update(self, *args, **kwargs):
        """update the square"""
        if len(args) == 4:
            self.y = args[3]
        if len(args) >= 3:
            self.x = args[2]
        if len(args) >= 2:
            self.width = args[1]
            self.height = args[1]
        if len(args) >= 1:
            self.id = args[0]

        if "id" in kwargs:
            self.id = kwargs["id"]
        if "size" in kwargs:
            self.width = kwargs["size"]
            self.height = kwargs["size"]
        if "x" in kwargs:
            self.x = kwargs["x"]
        if "y" in kwargs:
            self.y = kwargs["y"]

    def to_dictionary(self):
        """Square dictionary representation"""
        return {'id': self.id,
                'x': self.x,
                'size': self.size,
                'y': self.y}
