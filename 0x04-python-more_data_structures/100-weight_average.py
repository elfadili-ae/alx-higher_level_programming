#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    res, weight = 0, 0
    for ele in my_list:
        res += ele[0] * ele[1]
        weight += ele[1]
    return res / weight
