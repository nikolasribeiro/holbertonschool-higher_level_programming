#!/usr/bin/python3
from sys import argv


def is_exist(y):
    """ Method that determines a queen does not already exist in that y value
    Args:
        y: array that has the queens positions
        nqueen: ueen number
    Returns:
        bool
    """
    for x in range(N):
        if queens[x][1] == y:
            return True
    return False


def reject(x, y):
    """function thath check solution
    Args:
        x (int): queen number
        y (int): position index
    Returns:
        bool
    """
    if (is_exist(y)):
        return False
    i = 0
    while(i < x):
        if abs(queens[i][1] - y) == abs(i - x):
            return False
        i += 1
    return True


def solveNQ(x):
    """ Recursive function that solve the Backtracking algorithm
     Args:
         x: queen number
     """
    for y in range(N):
        for i in range(x, N):
            queens[i][1] = -1
        if reject(x, y):
            queens[x][1] = y
            if (x == N - 1):
                print(queens)
            else:
                solveNQ(x + 1)


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    if argv[1].isdigit() is False:
        print("N must be a number")
        exit(1)
    N = int(argv[1])
    if N < 4:
        print("N must be at least 4")
        exit(1)

    queens = [[i, -1] for i in range(N)]
    solveNQ(0)
