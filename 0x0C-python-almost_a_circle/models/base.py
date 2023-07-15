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
