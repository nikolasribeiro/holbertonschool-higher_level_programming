#!/usr/bin/python3
"""
Module of read_file
"""


def read_file(filename=""):
    """ read_file function """
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end='')
