#!/usr/bin/python3
"""This Module test the Rectangle class
"""

import unittest
from models.base import Base
from models.rectangle import Rectangle

class RectangleTest(unittest.TestCase):
    """BaseTest"""
    def checkDoc(self):
        """check class doc"""
        doc = Rectangle.__doc__
        assertTrue(len(doc) > 1)

    def checkInitDoc(self):
        """init doc"""
        doc = Rectangle.__init__.__doc__
        assertTrue(len(doc) > 1)

    def checkRectInhertsBase(self):
        """check Rectangle inherits Base"""
        assertTrue(issubclass(Rectangle, Base))


if __name__ == "__main__":
    unittest.main()
