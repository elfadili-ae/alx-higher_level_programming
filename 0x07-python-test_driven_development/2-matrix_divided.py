#!/usr/bin/python3
"""This function divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """divide all elements of a matrix

    Args:
        matrix: matrix to divide its elements
        div: integer

    Returns:
        matrix after dividing elements
    """
    err1 = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list):
        raise TypeError(err1)

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(err1)
        for ele in row:
            if not isinstance(ele, (int, float)):
                raise TypeError(err1)

    if len(matrix) == 0:
        return matrix

    matrix_size = len(matrix[0])
    for row in matrix:
        if len(row) != matrix_size:
            raise TypeError("Each row of the matrix must have the same size")

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    else:
        res = []
        for row in matrix:
            newRow = []
            for i in range(0, len(row)):
                newRow.append(round(row[i] / div, 2))
            res.append(newRow)

    return res
