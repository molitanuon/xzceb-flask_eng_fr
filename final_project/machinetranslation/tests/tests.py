import unittest

from translator import english_to_french, french_to_english

class TestEn2Fr(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french(None), None)
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        self.assertEqual(english_to_french("Have a good day"), "Bonne journée")
        self.assertEqual(english_to_french("This was very tasty"), "C'était très savoureux.")

class TestFr2En(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english(None), None)
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertEqual(french_to_english("Passe une bonne journée"), "Have a good day")
        self.assertEqual(french_to_english("Où est un bon restaurant?"), "Where is a good restaurant?")
unittest.main()
