#!/usr/bin/python3
"""
Module of append_write
"""


def append_write(filename="", text=""):
    """append_write function """
    with open(filename, 'a') as file:
        return file.write(text)
