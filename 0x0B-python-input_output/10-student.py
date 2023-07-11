#!/usr/bin/python3
"""This module contains Student class
"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """initialize the student object

        Args:
            first_name: first name
            last_name: last name
            age: age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """dictionary representation of a student

        Args:
            attrs: attributes

        Returns:
            student representation
        """
        if type(attrs) == list and all(type(ele) == str for ele in attrs):
            dicto = {}
            for element in attrs:
                if hasattr(self, element):
                    dicto.update({element: getattr(self, element)})
            return dicto
        return self.__dict__
