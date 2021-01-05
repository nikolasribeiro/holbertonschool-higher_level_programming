#!/usr/bin/python3
""" defines a square from 4-square.py """


class Square:
    """ square class """

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """ get size """
        return self.__size

    @size.setter
    def size(self, value):
        """ Setting the size of the square """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ return area of square """
        return self.__size ** 2

    def my_print(self):
        """ own print """
        if self.size == 0:
            print()
        for i in range(self.size):
            for j in range(self.size):
                print("#", end="")
            print()
