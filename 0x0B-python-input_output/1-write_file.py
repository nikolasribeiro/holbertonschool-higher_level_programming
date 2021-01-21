#!/usr/bin/python3
"""
Module of write_file
"""


def write_file(filename="", text=""):
    """ write_file function """
    with open(filename, 'w') as file:
        return file.write(text)
