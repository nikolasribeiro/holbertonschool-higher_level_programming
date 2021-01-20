#!/usr/bin/python3
"""
Module for MyInt.
"""


class MyInt(int):
    """Class MyInt"""

    def __eq__(self, number):
        """ equal function"""
        return False

    def __ne__(self, number):
        """negation function"""
        return True
