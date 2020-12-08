#!/usr/bin/python3
for letter in range(ord('z'), ord('a') - 1, - 1):
    if letter % 2 == 1:
        letter -= 32
    print("{:s}".format(chr(letter)), end="")
