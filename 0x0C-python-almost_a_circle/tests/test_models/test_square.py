#!/usr/bin/python3
"""This Module test the Square class
"""

import unittest
import sys
from io import StringIO
from unittest.mock import patch
from models.base import Base
from models.square import Square


class SquareTest(unittest.TestCase):
    """BaseTest"""

    def test_RectInhertsBase(self):
        """check Square inherits Base"""
        self.assertTrue(issubclass(Square, Base))

    def test_TwoRectID(self):
        """check two Square objects id"""
        r1 = Square(13)
        r2 = Square(15)
        self.assertEqual(r1.id, r2.id - 1)

    def test_RectZeroArg(self):
        with self.assertRaises(TypeError):
            r1 = Square()

    def test_RectFiveArg(self):
        with self.assertRaises(TypeError):
            r1 = Square(3, 23, 3, 5, 5)

# ---attributes---------------------------------------

    def test_privateWidth(self):
        with self.assertRaises(AttributeError):
            r2 = Square(15, 2, 3)
            print(r2.__width)

    def test_privateHeight(self):
        with self.assertRaises(AttributeError):
            r2 = Square(1, 2, 3)
            print(r2.__height)

    def test_privateX(self):
        with self.assertRaises(AttributeError):
            r2 = Square(15, 2, 3)
            print(r2.__x)

    def test_privateY(self):
        with self.assertRaises(AttributeError):
            r2 = Square(15, 2, 3)
            print(r2.__y)

    def test_privateID(self):
        with self.assertRaises(AttributeError):
            r2 = Square(15, 2, 3, 15)
            print(r2.__id)

# ---width---------------------------------------------

    def test_RectWidth(self):
        """testing getter of the Square's width"""
        r1 = Square(13, 3)
        self.assertEqual(r1.width, 13)

    def test_RectFloatWidth(self):
        """testing float width"""
        with self.assertRaises(TypeError):
            r1 = Square(13.5, 3)

    def test_RectNegativeWidth(self):
        """testing negative width"""
        with self.assertRaises(ValueError):
            r1 = Square(-13, 3)

    def test_RectZeroWidth(self):
        """testing 0 width"""
        with self.assertRaises(ValueError):
            r1 = Square(0, 3)

    def test_RectNoneWidth(self):
        """testing None width"""
        with self.assertRaises(TypeError):
            r1 = Square(None, 3)

    def test_RectSetWidth(self):
        r1 = Square(5, 3)
        r1.width = 13
        self.assertEqual(r1.width, 13)

    def test_RectSetNegativeWidth(self):
        r1 = Square(2, 3)
        with self.assertRaises(ValueError):
            r1.width = -13

    def test_RectSetNoneWidth(self):
        r1 = Square(2, 3)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1.width = None

    def test_RectSetFloatWidth(self):
        r1 = Square(2, 3)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1.width = 13.5

# ---height-----------------------------------------

    def test_RectHeight(self):
        """testing getter of the Square's height"""
        r1 = Square(13, 3)
        self.assertEqual(r1.height, 13)

    def test_RectSetHeight(self):
            r1 = Square(5, 3)
            r1.height = 13
            self.assertEqual(r1.height, 13)

    def test_RectSetNegativeHeight(self):
        r1 = Square(2, 3)
        with self.assertRaises(ValueError):
            r1.height = -13

    def test_RectSetNoneHeight(self):
        r1 = Square(2, 3)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1.height = None

    def test_RectSetFloatHeight(self):
        r1 = Square(2, 3)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1.height = 13.5

# ---x----------------------------------------------

    def test_RectXpos(self):
        """testing getter of the Square's x"""
        r1 = Square(13, 2, 2)
        self.assertEqual(r1.x, 2)

    def test_RectFloatXpos(self):
        """testing float x"""
        with self.assertRaises(TypeError):
            r1 = Square(13, 2.5, 2)

    def test_RectNegativeXpos(self):
        """testing negative x"""
        with self.assertRaises(ValueError):
            r1 = Square(13, -2, 2)

    def test_RectZeroXpos(self):
        """testing 0 x"""
        r1 = Square(13, 0, 2)
        self.assertEqual(r1.x, 0)

    def test_RectNoneXpos(self):
        """testing None x"""
        with self.assertRaises(TypeError):
            r1 = Square(13, None, 2)

    def test_RectSetX(self):
            r1 = Square(5, 2, 2)
            r1.x = 4
            self.assertEqual(r1.x, 4)

    def test_RectSetNegativeX(self):
        r1 = Square(2, 2, 2)
        with self.assertRaises(ValueError):
            r1.height = -4

    def test_RectSetNoneX(self):
        r1 = Square(2, 2, 2)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1.x = None

    def test_RectSetFloatHeight(self):
        r1 = Square(2, 2, 2)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1.x = 13.5
# ---y--------------------------------------------

    def test_RectYpos(self):
        """testing getter of the Square's y"""
        r1 = Square(13, 3, 2)
        self.assertEqual(r1.y, 2)

    def test_RectFloatYpos(self):
        """testing float y"""
        with self.assertRaises(TypeError):
            r1 = Square(13, 2, 2.5)

    def test_RectNegativeYpos(self):
        """testing negative y"""
        with self.assertRaises(ValueError):
            r1 = Square(13, 3, -2)

    def test_RectZeroYpos(self):
        """testing 0 y"""
        r1 = Square(13, 3, 0)
        self.assertEqual(r1.y, 0)

    def test_RectNoneYpos(self):
        """testing None y"""
        with self.assertRaises(TypeError):
            r1 = Square(13, 3, None)

    def test_RectSetHeight(self):
            r1 = Square(5, 3, 2)
            r1.y = 13
            self.assertEqual(r1.y, 13)

    def test_RectSetNegativeY(self):
        r1 = Square(2, 3, 2)
        with self.assertRaises(ValueError):
            r1.y = -13

    def test_RectSetNoneY(self):
        r1 = Square(2, 3, 2)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1.y = None

    def test_RectSetFloatY(self):
        r1 = Square(2, 3, 2)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1.y = 13.5

# ---area--------------------------------

    def test_areaPosZero(self):
        r1 = Square(3)
        self.assertEqual(r1.area(), 9)

    def test_areaPosNotZero(self):
        r1 = Square(5, 5, 10)
        self.assertEqual(r1.area(), 25)
# ---display-----------------------------

    def test_displayRect1(self):
        r1 = Square(1)
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            r1.display()
        self.assertEqual(fakeOutput.getvalue().strip(), '#')

    def test_displayRect2(self):
        r1 = Square(2)
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            r1.display()
        self.assertEqual(fakeOutput.getvalue().strip(), '##\n##')
# ---str----------------------------------

    def test_str(self):
        r1 = Square(4, 2, 1, 12)
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            print(r1)
        self.assertEqual(fakeOutput.getvalue(), '[Square] (12) 2/1 - 4\n')

# ---update--------------------------------

    def test_updateSize(self):
        r1 = Square(4, 2, 1, 12)
        r1.update(size=1)
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            print(r1)
        self.assertEqual(fakeOutput.getvalue(), '[Square] (12) 2/1 - 1\n')

    def test_updateX(self):
        r1 = Square(4, 6, 2, 12)
        r1.update(x=5)
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            print(r1)
        self.assertEqual(fakeOutput.getvalue(), '[Square] (12) 5/2 - 4\n')

    def test_updateY(self):
        r1 = Square(4, 6, 2, 12)
        r1.update(y=3)
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            print(r1)
        self.assertEqual(fakeOutput.getvalue(), '[Square] (12) 6/3 - 4\n')

    def test_updateID(self):
        r1 = Square(8, 2, 1, 12)
        r1.update(id=13)
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            print(r1)
        self.assertEqual(fakeOutput.getvalue(), '[Square] (13) 2/1 - 8\n')


if __name__ == "__main__":
    unittest.main()
