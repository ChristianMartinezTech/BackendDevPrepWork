# /usr/bin/env python3
"""Test function"""

from app import repeaded_char
import unittest

class TestStringMethods(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(repeaded_char(""), ('', -1))

    def test_empty_string(self):
        self.assertEqual(repeaded_char("abcdefg"), ('', -1))

    def test_empty_string(self):
        self.assertEqual(repeaded_char("abcdefga"), ('a', 1))

    def test_empty_string(self):
        self.assertEqual(repeaded_char("abcdefgijklmnñopqrstuwxyz1234567890.,!#$%&/¡?"), ('', -1))
    
    def test_empty_string(self):
        self.assertEqual(repeaded_char("bcdefgijklmnñopqrstuwxyz1234567890.,!#$%&/¡?aa"), ('a', 45))