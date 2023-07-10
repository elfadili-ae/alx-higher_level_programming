#!/usr/bin/python3
"""currently empty class"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """area of the shape"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate if value is integer

        Args:
            name: type
            value: value to check
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
