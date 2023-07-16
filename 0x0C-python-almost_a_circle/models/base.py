#!/usr/bin/python3
"""Base
"""

import json

class Base:
    """Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """initialize the base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """JSON representation of list_dictionaries"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save the obj representation to JSON file"""
        filename = cls.__name__ + ".json"
        with open(filename, "w", encoding="utf-8") as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dictionaries = [ele.to_dictionary() for ele in list_objs]
                f.write(Base.to_json_string(list_dictionaries))

    @staticmethod
    def from_json_string(json_string):
        """return the list of JSON string representation"""
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """return an instance with all attributes"""
        if dictionary is not None:
            if cls.__name__ == "Rectangle":
                insta = cls(1, 1)
            elif cls.__name__ == "Square":
                insta = cls(1)
            val =insta.update(**dictionary)
            return insta

    @classmethod
    def load_from_file(cls):
        """return list of instances"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r', encoding="utf-8") as f:
                li = Base.from_json_string(f.read())
                return [cls.create(**ele) for ele in li]
        except IOError:
            return []
