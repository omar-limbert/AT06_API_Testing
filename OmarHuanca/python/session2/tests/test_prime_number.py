import unittest

from OmarHuanca.python.session2.PrimeNumber import PrimeNumber


class TestPrimeNumber(unittest.TestCase):
    """
    Test to PrimeNumber Class.
    """

    def setUp(self):
        self.prime_number = PrimeNumber

    def test_number_is_prime(self):
        self.assertTrue(self.prime_number.is_prime(7), "Is Not Prime")
        self.assertTrue(self.prime_number.is_prime(1), "Is Not Prime")
        self.assertTrue(self.prime_number.is_prime(2), "Is Not Prime")
        self.assertTrue(self.prime_number.is_prime(3), "Is Not Prime")

    def test_number_is_not_prime(self):
        self.assertFalse(self.prime_number.is_prime(4), "Is Prime")
        self.assertFalse(self.prime_number.is_prime(6), "Is Prime")
        self.assertFalse(self.prime_number.is_prime(8), "Is Prime")
        self.assertFalse(self.prime_number.is_prime(9), "Is Prime")

    def test_prime_numbers_on_range(self):
        expect = ['1 : is prime? True ',
                  '2 : is prime? True ',
                  '3 : is prime? True ',
                  '4 : is prime? False ',
                  '5 : is prime? True ',
                  '6 : is prime? False ',
                  '7 : is prime? True ',
                  '8 : is prime? False ',
                  '9 : is prime? False ',
                  '10 : is prime? False ']

        result = self.prime_number.check_prime_numbers_on_range(1, 10)
        self.assertEqual(result, expect)
