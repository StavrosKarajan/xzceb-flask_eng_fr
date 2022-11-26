import unittest

from translator import english_to_french, french_to_english

class TestEnglish2French(unittest.TestCase): 
    def test1(self): 
        self.assertNotEqual(english_to_french("None"), '')
        self.assertNotEqual(english_to_french(0), 0)
        self.assertEqual(english_to_french('Thank you!'), 'Je vous remercie !')
        self.assertEqual(english_to_french('Goodbye'), 'Au revoir')     
        self.assertEqual(english_to_french('Hello'), 'Bonjour')    

class TestDouble(unittest.TestCase): 
    def test1(self): 
        self.assertNotEqual(french_to_english("None"), '')
        self.assertNotEqual(french_to_english(0), 0)
        self.assertEqual(french_to_english('Je vous remercie'), 'Thank you.')
        self.assertEqual(french_to_english('Au revoir'), 'Goodbye')
        self.assertEqual(french_to_english('Bonjour'), 'Hello')   
        
unittest.main()