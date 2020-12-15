#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = []

    if idx < 0 or idx > len(my_list):
        return new_list

    # Add all the elements into a new list
    for number in my_list:
        new_list.append(number)

    new_list[idx] = element
    return new_list