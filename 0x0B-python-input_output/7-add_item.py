#!/usr/bin/python3
""" importing json """
import json
import os
from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
"""
Module of add items
"""
if __name__ == "__main__":
    """ adding all the arguments passed by terminal """
    name = "add_item.json"

    if os.path.isfile(name):
        my_list = load_from_json_file(name)
    else:
        my_list = []

    for i in range(1, len(argv)):
        my_list.append(argv[i])
    save_to_json_file(my_list, name)
