#!/usr/bin/python3
"""Find the peak in a list."""


def find_peak(list_of_integers):
    """Peak finder."""
    n = len(list_of_integers)
    if n == 0:
        return None

    mid = int(n / 2)
    if mid - 1 < 0 and mid + 1 >= n:
        return list_of_integers[mid]

    if mid - 1 < 0:
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            return list_of_integers[mid + 1]
        else:
            return list_of_integers[mid]

    if mid + 1 >= n:
        if list_of_integers[mid] > list_of_integers[mid - 1]:
            return list_of_integers[mid]
        else:
            return list_of_integers[mid - 1]

    if list_of_integers[mid] > list_of_integers[mid - 1]:
        return find_peak(list_of_integers[mid:])
    else:
        return find_peak(list_of_integers[:mid])
