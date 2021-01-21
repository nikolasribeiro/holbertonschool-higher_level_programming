#!/usr/bin/python3
""" importing json """
import json
"""
Module of to_json_string
"""


def to_json_string(my_obj):
    """to_json_string function """
    json_string = json.dumps(my_obj)
    return json_string
