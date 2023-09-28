#!/usr/bin/python3
"""Find the peak in a list."""

def find_peak(list_of_integers):
    """Peak finder."""

    if len(list_of_integers) == 0:
        return None
    return (max(list_of_integers))
