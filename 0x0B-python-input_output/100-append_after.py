#!/usr/bin/python3
"""This module appends after something
"""


def append_after(filename="", search_string="", new_string=""):
    """insert text after sepecified string

    Args:
        filename: file's name
        search_string: string to search
        new_string: string to insert
    """
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()

    count = 0
    inlist = []
    for line in lines:
        if search_string in line:
            inlist.append(count + 1)
            count += 1
        count += 1

    if len(inlist) == 0:
        return
    for i in range(len(inlist)):
        lines.insert(inlist[i], new_string)
    with open(filename, "w", encoding="utf-8") as f:
        lines = "".join(lines)
        f.write(lines)
