#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for element in range(len(matrix)):
        for number in range(len(matrix[element])):
            print("{:d}".format(matrix[element][number]), end="")
            if number != (len(matrix[element]) - 1):
                print(" ", end="")

        print("")
