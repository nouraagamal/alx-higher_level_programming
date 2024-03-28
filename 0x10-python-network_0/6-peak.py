#!/usr/bin/python3
"""Find a peak."""


def find_peak(list_of_integers):
    """Function that finds a peak in a list of unsorted integers."""
    m = 0
    l = len(list_of_integers) - 1
    if list_of_integers:
        while m < l:
            mid = (m + l) // 2
            if list_of_integers[mid] > list_of_integers[mid + 1]:
                l = mid
            else:
                m = mid + 1
        return list_of_integers[m]
