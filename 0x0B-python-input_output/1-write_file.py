#!/usr/bin/python3
"""This module writes a string to a tesxt
"""


def write_file(filename="", text=""):
    """write a string to a text file

    Args:
        filename: file's name
        text: the text to write in the file

    Returns:
         number of characters written
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
