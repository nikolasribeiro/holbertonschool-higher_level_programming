#!/usr/bin/python3
"""
Print Square 
"""


def print_square(size):
    """ print square function """

    if not isinstance(size, int) or isinstance(size, float):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for row in range(size):
        for column in range(size):
            print("#", end="")
        print()
