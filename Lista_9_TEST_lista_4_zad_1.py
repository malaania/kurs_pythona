#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from lista4_zad3 import *


class TestLista4Zad1(unittest.TestCase):
    def setUp(self):
        self.stream = PrzetwarzajStrumien(
            "/home/malaania/Documents/text")

        self.poprawne = [
            "Książka leży na stole.",
            "Program nie działa.",
            "Ania je zupę."
        ]

        self.bledne = [
            "  książka leży na stole  ",
            "  program nie działa.",
            "Ania je zupę."
        ]

    def test_iterable(self):
        correct_stream = koryguj_strumien(self.stream)
        correct_stream.next()
        self.assertEqual(correct_stream.next(),
                         "Happily for readers, vinciguerra widened his lens.")

    def test_korekta(self):
        paryZdan = zip(self.bledne, self.poprawne)
        for bad, correct in paryZdan:
            result = korekta(bad)
            self.assertEqual(result, correct)

    def test_non_existing_file_exception(self):
        self.assertRaises(
            IOError,
            self.stream.open_file("/home/malaania/Documents/text1111")
        )

    def test_koryguj_strumien(self):
        self.assertItemsEqual(koryguj_strumien(self.bledne), self.poprawne)


if __name__ == "__main__":
    unittest.main()
