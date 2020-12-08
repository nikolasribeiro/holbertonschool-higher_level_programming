#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        if ord(letter) in range(ord("a"), ord("z")+1):
            letter = chr(ord(letter) - 32)
        print("{:s}".format(letter), end="")
    print()
