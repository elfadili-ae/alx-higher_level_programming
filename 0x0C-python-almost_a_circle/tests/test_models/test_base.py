#!/usr/bin/python3
"""This Module test the Base class
"""

import unittest
from models.base import Base


class BaseTest(unittest.TestCase):
    """BaseTest"""

    def setUp(self):
        pass

    def checkDoc(self):
        """check class doc"""
        doc = Base.__doc__
        self.assertTrue(len(doc) > 1)

    def checkInitDoc(self):
        """init doc"""
        doc = Base.__init__.__doc__
        self.assertTrue(len(doc) > 1)

    def checkCorrectIdOneObjNoId(self):
        """check if we get the correct id when no
        id is given"""
        b1 = Base()
        self.assertEqual(1, b1.id)

    def checkCorrectIdTwoObjNoId(self):
        """check if we get the correct id for a second obj
        with no id given"""
        b1 = Base()
        b2 = Base()
        self.assertEqual(1, b2.id)

    def checkCorrectIdThreeObjWithId(self):
        """check if we get the correct id for a third obj
        with a given id"""
        b1 = Base()
        b2 = Base()
        b3 = Base(13)
        self.assertEqual(13, b3.id)


if __name__ == "__main__":
    unittest.main()
