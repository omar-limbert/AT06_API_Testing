import unittest

from OmarHuanca.python.session2.EvenOrODDNumber import EvenOrODDNumber


class TestCircle(unittest.TestCase):
    """
    Test to EvenOrODDNumber class.
    """

    def setUp(self):
        self.even_odd_number = EvenOrODDNumber

    def test_number_is_even(self):
        self.assertEqual(self.even_odd_number.is_odd_or_even(2), "even")
        self.assertEqual(self.even_odd_number.is_odd_or_even(4), "even")
        self.assertEqual(self.even_odd_number.is_odd_or_even(6), "even")
        self.assertEqual(self.even_odd_number.is_odd_or_even(8), "even")

    def test_number_is_odd(self):
        self.assertEqual(self.even_odd_number.is_odd_or_even(1), "odd")
        self.assertEqual(self.even_odd_number.is_odd_or_even(3), "odd")
        self.assertEqual(self.even_odd_number.is_odd_or_even(5), "odd")
        self.assertEqual(self.even_odd_number.is_odd_or_even(7), "odd")

    def test_prime_numbers_on_range(self):
        expect = ['1 : is odd',
                  '2 : is even',
                  '3 : is odd',
                  '4 : is even',
                  '5 : is odd',
                  '6 : is even',
                  '7 : is odd',
                  '8 : is even',
                  '9 : is odd',
                  '10 : is even',
                  '11 : is odd',
                  '12 : is even']

        result = self.even_odd_number.check_even_or_odd_numbers_on_range(1, 12)
        self.assertEqual(result, expect)
