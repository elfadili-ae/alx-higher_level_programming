#!/usr/bin/python3
"""This Module test the Base class
"""

import unittest
from models.base import Base


class BaseTest(unittest.TestCase):
    """BaseTest"""

    def test_CorrectIdOneObjNoId(self):
        """check if we get the correct id when no
        id is given"""
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_CorrectIdTwoObjNoId(self):
        """check if we get the correct id for a second obj
        with no id given"""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_CorrectIdThreeObjWithId(self):
        """check if we get the correct id for a third obj
        with a given id"""
        b1 = Base()
        b2 = Base()
        b3 = Base(13)
        self.assertEqual(13, b3.id)


if __name__ == "__main__":
    unittest.main()
