#!/usr/bin/python3
""" importing json """
import json
"""
Module of save_to_json_file
"""


def save_to_json_file(my_obj, filename):
    """ save_to_json_file function """
    with open(filename, 'w') as file:
        json_string = json.dump(my_obj, file)
