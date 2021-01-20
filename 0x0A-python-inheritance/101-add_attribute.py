#!/usr/bin/python3
"""
Module for add_attribute.
"""


def add_attribute(obj, name, value):
    """add attribute function"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, name, value)
