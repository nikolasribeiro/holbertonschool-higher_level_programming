#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""
Module of Square
"""


class Square(Rectangle):
    """ defining class Square """

    def __init__(self, size):
        """ initializing self """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)