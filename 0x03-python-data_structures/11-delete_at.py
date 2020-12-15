#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    for element in my_list:
        if element == idx + 1:
            my_list.remove(i)
    return my_list
