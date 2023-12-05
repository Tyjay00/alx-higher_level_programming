#!/usr/bin/python3
"""Finds peak in unsorted integers"""

def find_peak(lst):
    """Finds a peak in lst"""

    if lst is None or lst == []:
        return None
    lo = 0
    hi = len(lst)
    mid = ((hi - lo) // 2) + lo
    mid = int(mid)
    if hi == 1:
        return lst[0]
    if hi == 2:
        return max(lst)
    if lst[mid] >= lst[mid - 1] and lst[mid] >= lst[mid + 1]:
        return lst[mid]
    if mid > 0 and lst[mid] < lst[mid + 1]:
        return find_peak(lst[mid:])
    if mid > 0 and lst[mid] < lst[mid - 1]:
        return find_peak(lst[:mid])
