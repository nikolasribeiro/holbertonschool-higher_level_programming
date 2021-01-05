#!/usr/bin/python3
""" defining class Square """


class Square:
    """ initializing self """

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """ getting size """
        return self.__size

    @size.setter
    def size(self, value):
        """ setting size """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """ getting position """
        return self.__position

    @position.setter
    def position(self, value):
        """ setting position """
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integer")
        if len(value) is not 2:
            raise TypeError("position must be a tuple of 2 positive integer")
        for element in value:
            if not isinstance(element, int):
                raise TypeError("position must be a tuple of "
                                "2 positive integer")
            if element < 0:
                raise TypeError("position must be a tuple of 2 "
                                "positive integer")
        self.__position = value

    def area(self):
        """ defining area """
        return self.__size ** 2

    def my_print(self):
        """ defining my_print """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size + self.__position[1]):
                if i < self.__position[1]:
                    print()
                    continue
                for j in range(self.__size + self.__position[0]):
                    if j < self.__position[0]:
                        print(" ", end="")
                        continue
                    print("#", end="")
                print()

    def __str__(self):
        """ defining str """
        str1 = ""
        if self.__size == 0:
            return str1
        else:
            for i in range(0, self.__size + self.__position[1]):
                if i < self.__position[1]:
                    str1 += "\n"
                    continue
                for j in range(0, self.__size + self.__position[0]):
                    if j < self.__position[0]:
                        str1 += " "
                        continue
                    str1 += "#"
                if i is not self.__size + self.__position[1] - 1:
                    str1 += "\n"
        return str1
