#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if a_dictionary:
        keys = []
        for key in a_dictionary:
            if a_dictionary[key] == value:
                keys.append(key)
        for key in keys:
            a_dictionary.pop(key)
    return a_dictionary
