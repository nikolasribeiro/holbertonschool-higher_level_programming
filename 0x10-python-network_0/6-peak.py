#!/usr/bin/python3
"""6-peak"""


def find_peak(list_of_integers):
    """function find_peak"""

    if len(list_of_integers) > 1:
        if list_of_integers[0] >= list_of_integers[1]:
            return list_of_integers[0]
        if list_of_integers[-1] >= list_of_integers[-2]:
            return list_of_integers[-1]
        return _find_peak(list_of_integers, 0, len(list_of_integers))
    if not list_of_integers:
        return None
    return list_of_integers[0]


def _find_peak(lint, start, stop):
    """function _find_peak"""
    if stop - start < 2:
        return None
    mid = (start + stop) // 2
    if lint[mid] >= lint[mid - 1] and lint[mid] >= lint[mid + 1]:
        return lint[mid]
    return _find_peak(lint, start, mid) or _find_peak(lint, mid, stop)