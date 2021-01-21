#!/usr/bin/python3
""" importing json """
import json
"""
Module of load_from_json_file
"""


def load_from_json_file(filename):
    """ load_from_json_file function """
    with open(filename, 'r') as file:
        json_string = json.load(file)
        return json_string
