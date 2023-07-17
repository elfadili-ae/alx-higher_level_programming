#!/usr/bin/python3
"""This Module test the Rectangle class
"""

import unittest
import sys
from io import StringIO
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle


class RectangleTest(unittest.TestCase):
    """BaseTest"""

    def test_RectInhertsBase(self):
        """check Rectangle inherits Base"""
        self.assertTrue(issubclass(Rectangle, Base))

    def test_TwoRectID(self):
        """check two Rectangle objects id"""
        r1 = Rectangle(13, 3)
        r2 = Rectangle(15, 5)
        self.assertEqual(r1.id, r2.id - 1)

    def test_RectZeroArg(self):
        """testing Rectangle one arg"""
        with self.assertRaises(TypeError):
            r1 = Rectangle()

    def test_RectOneArg(self):
        """testing Rectangle one arg"""
        with self.assertRaises(TypeError):
            r1 = Rectangle(3)
# ---width---------------------------------------------

    def test_RectWidth(self):
        """testing getter of the Rectangle's width"""
        r1 = Rectangle(13, 3)
        self.assertEqual(r1.width, 13)

    def test_RectFloatWidth(self):
        """testing float width"""
        with self.assertRaises(TypeError):
            r1 = Rectangle(13.5, 3)

    def test_RectNegativeWidth(self):
        """testing negative width"""
        with self.assertRaises(ValueError):
            r1 = Rectangle(-13, 3)

    def test_RectZeroWidth(self):
        """testing 0 width"""
        with self.assertRaises(ValueError):
            r1 = Rectangle(0, 3)

    def test_RectNoneWidth(self):
        """testing None width"""
        with self.assertRaises(TypeError):
            r1 = Rectangle(None, 3)
# ---height-----------------------------------------

    def test_RectHeight(self):
        """testing getter of the Rectangle's height"""
        r1 = Rectangle(13, 3)
        self.assertEqual(r1.height, 3)

    def test_RectFloatHeight(self):
        """testing float height"""
        with self.assertRaises(TypeError):
            r1 = Rectangle(13, 3.5)

    def test_RectNegativeHeight(self):
        """testing negative height"""
        with self.assertRaises(ValueError):
            r1 = Rectangle(13, -3)

    def test_RectZeroHeight(self):
        """testing 0 height"""
        with self.assertRaises(ValueError):
            r1 = Rectangle(13, 0)

    def test_RectNoneHeight(self):
        """testing None height"""
        with self.assertRaises(TypeError):
            r1 = Rectangle(3, None)
# ---x----------------------------------------------

    def test_RectXpos(self):
        """testing getter of the Rectangle's x"""
        r1 = Rectangle(13, 3, 2, 2)
        self.assertEqual(r1.x, 2)

    def test_RectFloatXpos(self):
        """testing float x"""
        with self.assertRaises(TypeError):
            r1 = Rectangle(13, 3, 2.5, 2)

    def test_RectNegativeXpos(self):
        """testing negative x"""
        with self.assertRaises(ValueError):
            r1 = Rectangle(13, 3, -2, 2)

    def test_RectZeroXpos(self):
        """testing 0 x"""
        r1 = Rectangle(13, 3, 0, 2)
        self.assertEqual(r1.x, 0)

    def test_RectNoneXpos(self):
        """testing None x"""
        with self.assertRaises(TypeError):
            r1 = Rectangle(13, 3, None, 2)
# ---y--------------------------------------------

    def test_RectYpos(self):
        """testing getter of the Rectangle's y"""
        r1 = Rectangle(13, 3, 2, 2)
        self.assertEqual(r1.y, 2)

    def test_RectFloatYpos(self):
        """testing float y"""
        with self.assertRaises(TypeError):
            r1 = Rectangle(13, 3, 2, 2.5)

    def test_RectNegativeYpos(self):
        """testing negative y"""
        with self.assertRaises(ValueError):
            r1 = Rectangle(13, 3, 2, -2)

    def test_RectZeroYpos(self):
        """testing 0 y"""
        r1 = Rectangle(13, 3, 2, 0)
        self.assertEqual(r1.y, 0)

    def test_RectNoneYpos(self):
        """testing None y"""
        with self.assertRaises(TypeError):
            r1 = Rectangle(13, 3, 2, None)
# ---area--------------------------------

    def test_areaPosZero(self):
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

    def test_areaPosNotZero(self):
        r1 = Rectangle(13, 2, 5, 10)
        self.assertEqual(r1.area(), 26)
# ---display-----------------------------

    def test_displayRect1(self):
        r1 = Rectangle(1, 1)
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            r1.display()
        self.assertEqual(fakeOutput.getvalue().strip(), '#')

    def test_displayRect2(self):
        r1 = Rectangle(2, 2)
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            r1.display()
        self.assertEqual(fakeOutput.getvalue().strip(), '##\n##')
# ---str----------------------------------

    def test_str(self):
        r1 = Rectangle(4, 6, 2, 1, 12)
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            print(r1)
        self.assertEqual(fakeOutput.getvalue(), '[Rectangle] (12) 2/1 - 4/6\n')

# ---update--------------------------------

    def test_updateWidth(self):
        r1 = Rectangle(4, 6, 2, 1, 12)
        r1.update(width=1)
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            print(r1)
        self.assertEqual(fakeOutput.getvalue(), '[Rectangle] (12) 2/1 - 1/6\n')

    def test_updateHeight(self):
        r1 = Rectangle(4, 6, 2, 1, 12)
        r1.update(height=1)
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            print(r1)
        self.assertEqual(fakeOutput.getvalue(), '[Rectangle] (12) 2/1 - 4/1\n')

    def test_updateX(self):
        r1 = Rectangle(4, 6, 2, 1, 12)
        r1.update(x=1)
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            print(r1)
        self.assertEqual(fakeOutput.getvalue(), '[Rectangle] (12) 1/1 - 4/6\n')

    def test_updateY(self):
        r1 = Rectangle(4, 6, 2, 1, 12)
        r1.update(y=2)
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            print(r1)
        self.assertEqual(fakeOutput.getvalue(), '[Rectangle] (12) 2/2 - 4/6\n')

    def test_updateID(self):
        r1 = Rectangle(4, 6, 2, 1, 12)
        r1.update(id=13)
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            print(r1)
        self.assertEqual(fakeOutput.getvalue(), '[Rectangle] (13) 2/1 - 4/6\n')


if __name__ == "__main__":
    unittest.main()
