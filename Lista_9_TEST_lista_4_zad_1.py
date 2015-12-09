#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import pydoc
from lista4_zad3 import *

class TestLista4Zad1(unittest.TestCase):

    def setUp(self):

        self.stream = PrzetwarzajStrumien(
            "/home/malaania/Documents/text")

        self.paryZdan = [
            ("  książka leży na stole  ","Książka leży na stole."),
            ("  program nie działa.","Program nie działa."),
            ("Ania je zupę.","Ania je zupę."),
        ]

    def test_korekta(self):
        for bad, correct in self.paryZdan:
            result =  korekta(bad)
            self.assertEqual(result, correct)

    def test_non_existing_file_exception(self):
        self.assertRaises(
            IOError,
            self.stream.open_file("/home/malaania/Documents/text1111")
        )
        


if __name__ == "__main__":
    unittest.main()