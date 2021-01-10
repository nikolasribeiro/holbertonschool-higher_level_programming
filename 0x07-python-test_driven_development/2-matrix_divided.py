#!/usr/bin/python3

""" 
 Matrix Divider
"""


def matrix_divided(matrix, div):
    """ matrix divider function """
    # Creates new list
    new_neo = []

    # Check if the div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check that div is not zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Loop over the matrix for check the content inside
    for content in matrix:
        # if one row of the matrix is bigger than other, raise error
        if len(content) is not len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

        # Check the elements inside the row of the matrix
        for element in content:
            if not isinstance(element, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats")

    morpheus = list(map(lambda el: round(el / div, 2), content))
    new_neo.append(morpheus)
