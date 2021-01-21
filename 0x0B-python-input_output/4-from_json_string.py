#!/usr/bin/python3
""" importing json """
import json
"""
Module of from_json_string
"""


def from_json_string(my_str):
    """ from_json_string function """
    json_string = json.loads(my_str)
    return json_string
