#!/usr/bin/python3
"""
Module to check if is instance of a python object
"""


def is_same_class(obj, a_class):
    """ Functiopn that checks if an object is instance of another object """
    if type(obj) is a_class:
        return True

    return False
