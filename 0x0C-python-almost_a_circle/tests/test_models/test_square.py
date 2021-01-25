#!/usr/bin/python3


""" Module test_square"""
import unittest
import io
import sys

from models.rectangle import Rectangle
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    """ class TestSquare """

    def test_parent(self):
        """ function test_parent """
        self.sq = Square(1)
        self.assertTrue(isinstance(self.sq, Rectangle))
        self.assertTrue(issubclass(Square, Rectangle))
        self.assertEqual(self.sq.id, 1)

    def test_init(self):
        """ function test_init """
        self.sq = Square(1, 2, 3, 10)
        self.assertEqual(self.sq.width, 1)
        self.assertEqual(self.sq.height, 1)
        self.assertEqual(self.sq.size, 1)
        self.assertEqual(self.sq.x, 2)
        self.assertEqual(self.sq.y, 3)
        self.assertEqual(self.sq.id, 10)

        self.sq = Square(1)
        self.assertEqual(self.sq.x, 0)
        self.assertEqual(self.sq.y, 0)
        self.assertEqual(self.sq.id, 1)

    def test_bad_types(self):
        """ function test_bad_types """
        with self.assertRaises(TypeError):
            self.sq = Square("g")
        with self.assertRaises(TypeError):
            self.sq = Square(0.3)
        with self.assertRaises(TypeError):
            self.sq = Square([3])
        with self.assertRaises(TypeError):
            self.sq = Square({2: 2})
        with self.assertRaises(TypeError):
            self.sq = Square((2,))

    def test_bad_values(self):
        """ function test_bad_values """
        with self.assertRaises(ValueError):
            self.sq = Square(-1)
        with self.assertRaises(ValueError):
            self.sq = Square(1, -2)
        with self.assertRaises(ValueError):
            self.sq = Square(1, 2, -3)

    def test_etc(self):
        """ function test_etc """
        with self.assertRaises(TypeError):
            self.sq = Square()
        with self.assertRaises(TypeError):
            self.sq = Square(1, 3, 5, 6, 3, 4, 4)

    def test_area(self):
        """ function test_area """
        self.sq = Square(4)
        self.assertEqual(self.sq.area(), 16)
        self.sq1 = Square(8, 0, 0, 12)
        self.assertEqual(self.sq1.area(), 64)

    def test_display(self):
        """ function test_display """
        self.sq = Square(3)
        cap_out = io.StringIO()
        sys.stdout = cap_out
        self.sq.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(cap_out.getvalue(), "###\n###\n###\n")
        self.sq = Square(2, 1, 2)
        cap_out = io.StringIO()
        sys.stdout = cap_out
        self.sq.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(cap_out.getvalue(), "\n\n ##\n ##\n")

    def test_str(self):
        """ function test_str """
        self.sq = Square(4)
        self.assertEqual(self.sq.__str__(), "[Square] (1) 0/0 - 4")
        self.sq = Square(4, 12, 1, 24)
        self.assertEqual(self.sq.__str__(), "[Square] (24) 12/1 - 4")

    def test_update(self):
        """ function test_update """
        self.sq = Square(10, 10, 10)
        self.assertEqual(self.sq.__str__(), "[Square] (1) 10/10 - 10")
        self.sq.update(98)
        self.assertEqual(self.sq.__str__(), "[Square] (98) 10/10 - 10")
        self.sq.update(98, 2)
        self.assertEqual(self.sq.__str__(), "[Square] (98) 10/10 - 2")
        self.sq.update(98, 2, 3)
        self.assertEqual(self.sq.__str__(), "[Square] (98) 3/10 - 2")
        self.sq.update(98, 2, 3, 4)
        self.assertEqual(self.sq.__str__(), "[Square] (98) 3/4 - 2")
        self.sq = Square(10, 10, 10)
        self.assertEqual(self.sq.__str__(), "[Square] (2) 10/10 - 10")
        self.sq.update(id=98)
        self.assertEqual(self.sq.__str__(), "[Square] (98) 10/10 - 10")
        self.sq.update(id=98, size=2)
        self.assertEqual(self.sq.__str__(), "[Square] (98) 10/10 - 2")
        self.sq.update(id=98, size=2, x=4)
        self.assertEqual(self.sq.__str__(), "[Square] (98) 4/10 - 2")
        self.sq.update(id=98, size=2, x=4, y=5)
        self.assertEqual(self.sq.__str__(), "[Square] (98) 4/5 - 2")
        with self.assertRaises(KeyError):
            self.sq.update(chicken=3)
        with self.assertRaises(TypeError):
            self.sq.update("f")
        with self.assertRaises(TypeError):
            self.sq.update(size="f")
        self.sq = Square(1, 2)
        self.sq.update(3, 3, id=9)
        self.assertEqual(self.sq.__str__(), "[Square] (3) 2/0 - 3")

    def test_dictionary(self):
        """ function test_dictionary """
        self.sq = Square(10, 10, 10, 10)
        sq_dict = self.sq.to_dictionary()
        self.assertEqual(sq_dict, {"id": 10, "x": 10, "size": 10, "y": 10})
        self.assertTrue(isinstance(sq_dict, dict))
        self.sq2 = Square(1, 1)
        self.sq2.update(**sq_dict)
        self.assertFalse(self.sq == self.sq2)

    def test_create_cls(self):
        """ function test_create_cls """
        self.s1 = Square(10, 10, 10, 99)
        self.s1_dict = self.s1.to_dictionary()
        self.s2 = Square.create(**self.s1_dict)
        self.assertEqual(self.s2.__str__(), "[Square] (99) 10/10 - 10")
        self.assertTrue(self.s2 is not self.s1)
        self.assertTrue(self.s2 != self.s1)

    def test_loading_from_file(self):
        """ function test_loading_from_file """
        self.s1 = Square(1)
        self.s2 = Square(1)
        input_li = [self.s1, self.s2]
        Square.save_to_file(input_li)
        output_li = Square.load_from_file()
        for obj1, obj2 in zip(input_li, output_li):
            self.assertEqual(obj1.__dict__, obj2.__dict__)


if __name__ == "__name__":
    unittest.main()
