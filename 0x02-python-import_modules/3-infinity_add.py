#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    total = 0
    for value in range(len(argv) - 1):
        total += int(argv[value + 1])
    print("{}".format(total))
