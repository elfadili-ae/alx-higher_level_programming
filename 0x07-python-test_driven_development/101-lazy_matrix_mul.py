#!/usr/bin/python3
import numpy as np

"""This module multiplies two matrices using NumPy
"""


def lazy_matrix_mul(m_a, m_b):
    """multiply two matrices

    Args:
        m_a: first matrix
        m_b: second matrix

    Returns:
        result of multiplication
    """
    return np.matmul(m_a, m_b)
