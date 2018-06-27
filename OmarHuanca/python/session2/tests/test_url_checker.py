import unittest

from OmarHuanca.python.session2.URLChecker import URLChecker


class TestCircle(unittest.TestCase):
    """
    Test to Circle class.
    """

    def setUp(self):
        self.url_checker = URLChecker

    def test_is_valid_url_with_lower_case(self):
        self.assertTrue(self.url_checker.is_valid_url("http://www.google.com "), "Is Not Valid URL")
        self.assertTrue(self.url_checker.is_valid_url("http://www.facebook.com "), "Is Not Valid URL")
        self.assertTrue(self.url_checker.is_valid_url("http://www.github.com "), "Is Not Valid URL")

    def test_is_valid_url_with_upper_case(self):
        self.assertTrue(self.url_checker.is_valid_url("HTTP://WWW.GOOGLE.COM "), "Is Not Valid URL")
        self.assertTrue(self.url_checker.is_valid_url("HTTP://WWW.FACEBOOK.COM "), "Is Not Valid URL")
        self.assertTrue(self.url_checker.is_valid_url("HTTP://WWW.GITHUB.COM "), "Is Not Valid URL")

    def test_is_not_valid_url_with_lower_case(self):
        self.assertFalse(self.url_checker.is_valid_url("htt://www.google.com"), "Is Valid URL")
        self.assertFalse(self.url_checker.is_valid_url("http://www.facebook.com"), "Is Valid URL")
        self.assertFalse(self.url_checker.is_valid_url("http1://www.github.com "), "Is Valid URL")

    def test_is_not_valid_url_with_upper_case(self):
        self.assertFalse(self.url_checker.is_valid_url("HTTP1://WWW.GOOGLE.COM "), "Is Not Valid URL")
        self.assertFalse(self.url_checker.is_valid_url("HTTP://WWW.FACEBOOK.COM"), "Is Not Valid URL")
        self.assertFalse(self.url_checker.is_valid_url("HP://WWW.GITHUB.COM "), "Is Not Valid URL")
