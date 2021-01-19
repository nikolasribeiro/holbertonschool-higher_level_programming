#!/usr/bin/python3
"""
Module based on 5-base geometry
"""


class BaseGeometry:
    """ Main class of base geometry """

    def area(self):
        """ Gets the area of a geometry  """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validation for value """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
