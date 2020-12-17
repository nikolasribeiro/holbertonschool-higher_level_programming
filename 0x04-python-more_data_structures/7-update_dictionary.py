#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """ if a key in the dictionary dont exist, it created but if the key exist: replace it """
    a_dictionary[key] = value
    return a_dictionary