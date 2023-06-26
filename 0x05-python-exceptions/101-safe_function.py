#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    val = None
    try:
        val = fct(*args)
    except Exception as err:
        sys.stderr.write("Exception: {}\n".format(err))
        return val
    return val
