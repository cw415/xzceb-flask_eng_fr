"""
 tests.py version 1
"""
import unittest
from translator import englishToFrench,frenchToEnglish


class TestEF(unittest.TestCase):
    """Test english to french"""
    def test1(self):
        """start assertion"""
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')


class TestFE(unittest.TestCase):
    """Test french to english"""
    def test1(self):
        """start assertion"""
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')

unittest.main()
