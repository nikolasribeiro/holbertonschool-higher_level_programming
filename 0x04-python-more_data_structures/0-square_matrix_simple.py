#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    neo = []

    for trinity in matrix:
        trinity = list(map(lambda agent: agent * agent, trinity))
        neo.append(trinity)

    return neo
