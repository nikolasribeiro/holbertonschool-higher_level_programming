#!/usr/bin/python3
"""
Module of pascal_triangle
"""


def pascal_triangle(n):
    """ pascal_triangle function """
    new_list = []
    if n <= 0:
        return new_list
    new_list = [[1]]

    for i in range(1, n):
        row = [1]
        for element in range(1, i):
            row.append(new_list[i - 1][element - 1] + new_list[i - 1][element])
        row.append(1)
        new_list.append(row)
    return(new_list)
