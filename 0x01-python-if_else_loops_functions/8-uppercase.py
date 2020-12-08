#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        if ord(letter) >= ord("a")and ord(letter) < ord("z"):
            letter = chr(ord(letter) - 32)
        print("{:s}".format(letter), end="")
    print()

uppercase("holberton")
uppercase("Holberton School 98 Battery street")