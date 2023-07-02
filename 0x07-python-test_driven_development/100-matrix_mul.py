#!/usr/bin/python3
"""This module multiplies 2 matrices
"""


def matrix_mul(m_a, m_b):
    """multiply two matrices

    Args:
        m_a: (list of lists) first matrix
        m_b: (list of lists) second matrix

    Returns:
        result of multiplication
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    for row in m_a:
        if type(row) is not list:
            raise TypeError("m_a must be a list of lists")
    for row in m_b:
        if type(row) is not list:
            raise TypeError("m_b must be a list of lists")

    if len(m_a) != 0:
        for row in m_a:
            if len(row) == 0:
                raise ValueError("m_a can't be empty")
    else:
        raise ValueError("m_a can't be empty")
    if len(m_b) != 0:
        for row in m_b:
            if len(row) == 0:
                raise ValueError("m_b can't be empty")
    else:
        raise ValueError("m_b can't be empty")

    for row in m_a:
        for ele in row:
            if not isinstance(ele, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        for ele in row:
            if not isinstance(ele, (int, float)):
                raise TypeError("m_b should contain only integers or floats")

    size = len(m_a[0])
    for row in m_a:
        if len(row) != size:
            raise TypeError("each row of m_a must be of the same size")
    size = len(m_b[0])
    for row in m_b:
        if len(row) != size:
            raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    res = [[0 for _ in range(len(m_b[0]))] for _ in range(len(m_a))]
    for i in range(0, len(m_a)):
        for j in range(0, len(m_b[0])):
            for k in range(0, len(m_a[0])):
                res[i][j] += m_a[i][k] * m_b[k][j]

    return res
