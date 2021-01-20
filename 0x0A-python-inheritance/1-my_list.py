#!/usr/bin/python3
"""
Module of my list
"""


class MyList(list):
    """ defining MyList class """

    def print_sorted(self):
        """ print_sorted method """
        new_list = self[:]
        new_list.sort()
        print(new_list)
