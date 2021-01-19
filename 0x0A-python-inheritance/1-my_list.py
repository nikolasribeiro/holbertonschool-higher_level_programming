#!/usr/bin/python3
"""
Module of my list
"""


class MyList(list):
    """ defining MyList class """

    def print_sorted(self):
        """ print_sorted method """
        print(sorted(self))
