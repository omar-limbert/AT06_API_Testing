import unittest

from OmarHuanca.python.session3.Replace import Replace


class TestReplace(unittest.TestCase):
    """
    Test to Replace class.
    """

    def setUp(self):
        self.replace = Replace

    def test_replace_a_letter_on_string(self):
        self.assertEqual(self.replace.replace_in_string("Mississippi", "i", "I"), "MIssIssIppI")
        self.assertEqual(self.replace.replace_in_string("Mississippi", "p", "P"), "MississiPPi")
