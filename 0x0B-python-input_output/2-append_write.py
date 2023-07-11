#!/usr/bin/python3
"""This module appends data to a file
"""


def append_write(filename="", text=""):
    """append text to the file

    Args:
        filename: file's name
        text: text to append
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
