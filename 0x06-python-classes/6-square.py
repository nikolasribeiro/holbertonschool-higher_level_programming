#!/usr/bin/python3
""" defines a square from 5-square """


class Square:
    """ square class """

    def __init__(self, size=0, position=(0, 0)):
        """ initializing set """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if type(position) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(position) is not 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        for i in position:
            if not isinstance(i, int):
                raise TypeError("position must be a tuple of 2 "
                                "positive integers")
            if i < 0:
                raise TypeError("position must be a tuple of 2 "
                                "positive integers")
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """ getting self """
        return self.__size

    @size.setter
    def size(self, value):
        """ setting self """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """ retrieve position"""
        return self.__position

    @position.setter
    def position(self, value):
        """ setting position """
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) is not 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        for i in value:
            if not isinstance(i, int):
                raise TypeError("position must be a tuple of 2 "
                                "positive integers")
            if i < 0:
                raise TypeError("position must be a tuple of 2 "
                                "positive integers")
        self.__position = value

    def area(self):
        """ defining area """
        return self.__size ** 2

    def my_print(self):
        """ defining print """
        if self.__size == 0:
            print()
        else:
            for i in range(0, self.__position[1]):
                print()
            for row in range(self.__size):
                for j in range(0, self.__position[0]):
                    print(" ", end="")
                for column in range(self.__size):
                    print("#", end="")
                print()
