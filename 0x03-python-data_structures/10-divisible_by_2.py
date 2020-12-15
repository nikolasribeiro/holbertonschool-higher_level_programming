#!/bin/usr/python3
def divisible_by_2(my_list=[]):
    boolean_lists = []
    for number in my_list:
        if number % 2 == 0:
            boolean_lists.append(True)
        else:
            boolean_lists.append(False)
    return boolean_lists
