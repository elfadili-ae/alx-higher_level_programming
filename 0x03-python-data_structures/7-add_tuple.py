#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) >= 2:
        nums1 = (tuple_a[0], tuple_a[1])
    elif len(tuple_a) == 1:
        nums1 = (tuple_a[0], 0)
    else:
        nums1 = (0, 0)
    if len(tuple_b) >= 2:
        nums2 = (tuple_b[0], tuple_b[1])
    elif len(tuple_b) == 1:
        nums2 = (tuple_b[0], 0)
    else:
        nums2 = (0, 0)
    new_tuple = (nums1[0] + nums2[0], nums1[1] + nums2[1])
    return (new_tuple)
