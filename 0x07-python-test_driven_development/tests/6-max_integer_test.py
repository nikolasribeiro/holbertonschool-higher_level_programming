#!/usr/bin/python3
""" 
Unittest of 6-max_integer
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ Unit test class for max_integer function"""

    def test_int_max(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_is_none(self):
        self.assertIsNone(max_integer())
