#!/usr/bin/python3
'''magic calculation
'''
def magic_calculation(a, b):
    """magic calculation

    Args:
        a (int): a
        b (int): b

    Raises:
        Execption: too far

    Returns:
        int: calculated value
    """
    result = 0

    for i in range(1, 3):
        try:
            if i > a:
                raise Execption("Too far")
            else:
                result += (a**b) / i
        except:
            result = a + b
            break
        return result
