#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    check = -number % 10 * -1
else:
    check = number % 10
if check > 5:
    print('Last digit of {:d} is {:d} and is greater than 5'.format(number, check))
elif check == 0:
    print('Last digit of {:d} is {:d} and is 0'.format(number, check))
else:
    print('Last digit of {:d} is {:d} and is less than 6 and not 0'.
          format(number, check))