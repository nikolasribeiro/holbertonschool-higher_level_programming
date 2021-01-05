#!/usr/bin/python3

""" Defines a class based on 2-square """


class Square:
    """ square class """

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ return area """
        return self.__size ** 2
