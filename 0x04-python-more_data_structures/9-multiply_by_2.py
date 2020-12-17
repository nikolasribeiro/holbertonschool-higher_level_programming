#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = {}
    for key in a_dictionary.keys():
        value_x_2 = a_dictionary[key] * 2
        new_dict[key] = value_x_2
    
    return new_dict