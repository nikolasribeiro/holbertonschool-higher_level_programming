#!/bin/usr/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    my_list.sort(reverse=True)
    return my_list[0]
