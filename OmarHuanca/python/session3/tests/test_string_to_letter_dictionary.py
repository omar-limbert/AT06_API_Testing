import unittest

from OmarHuanca.python.session3.StringToLetterDictionary import StringToLetterDictionary


class TestStringToLetterDictionary(unittest.TestCase):
    """
    Test to StringToLetterDictionary class.
    """

    def setUp(self):
        self.string_to_dictionary = StringToLetterDictionary

    def test_convert_string_to_letter_dictionary_sorted(self):
        self.assertEqual(self.string_to_dictionary.convert_to_dictionary("THIS IS A TEST"),
                         [('a', 1),
                          ('e', 1),
                          ('h', 1),
                          ('i', 2),
                          ('s', 3),
                          ('t', 3)])
        self.assertEqual(self.string_to_dictionary.convert_to_dictionary("ThiS is String with Upper and lower case"),
                         [('a', 2),
                          ('c', 1),
                          ('d', 1),
                          ('e', 3),
                          ('g', 1),
                          ('h', 2),
                          ('i', 4),
                          ('l', 1),
                          ('n', 2),
                          ('o', 1),
                          ('p', 2),
                          ('r', 3),
                          ('s', 2),
                          ('t', 2),
                          ('u', 1),
                          ('w', 2)])
