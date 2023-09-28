#!/usr/bin/python3
"""Find the peak in a list."""


def find_peak(nums):
    """Peak finder."""
    n = len(nums)
    if n == 0:
        return None

    mid = int(n / 2)
    if mid - 1 < 0 and mid + 1 >= n:
        return nums[mid]

    if mid - 1 < 0:
        if nums[mid] < nums[mid + 1]:
            return nums[mid + 1]
        else:
            return nums[mid]

    if mid + 1 >= n:
        if nums[mid] > nums[mid - 1]:
            return nums[mid]
        else:
            return nums[mid - 1]

    if nums[mid - 1] < nums[mid] and nums[mid] > nums[mid + 1]:
        return nums[mid]

    if nums[mid + 1] < nums[mid - 1]:
        return find_peak(nums[:mid])
    else:
        return find_peak(nums[mid:])
