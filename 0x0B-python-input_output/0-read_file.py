#!/usr/bin/python3
"""This Module reads a file
"""

import sys


def read_file(filename=""):
    """read the file and print it to stdout

    Args:
        filename: read the file and print it to stdout
    """
    with open(filename, encoding="utf-8") as f:
        read_data = f.read()

    sys.stdout.write(read_data)
    f.closed
