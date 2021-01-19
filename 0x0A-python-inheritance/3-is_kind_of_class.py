#!/usr/bin/python3
""" 
Module of is kind of class
"""


def is_kind_of_class(obj, a_class):
    """ Function that returns if obj is instance of a_class """
    if isinstance(obj, a_class):
        return True
    return False
