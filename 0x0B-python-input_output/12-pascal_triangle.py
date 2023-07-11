#!/usr/bin/python3
"""This module contains Pascal_triangle method
"""


def pascal_triangle(n):
    """pascal triangle"""
    if n <= 0:
        return []

    res = [[1]]
    for i in range(1, n):
        row = [1] * (i + 1)
        if i > 1:
            for j in range(1, len(row) - 1):
                row[j] = res[i - 1][j - 1] + res[i - 1][j]
        res.append(row)
    return res
