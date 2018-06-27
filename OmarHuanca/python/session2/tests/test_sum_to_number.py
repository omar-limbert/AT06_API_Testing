import unittest

from OmarHuanca.python.session2.SumToNumber import SumToNumber


class TestSumToNumber(unittest.TestCase):
    """
    Test to SumToNumber class.
    """

    def setUp(self):
        self.sum = SumToNumber

    def test_sum_to_number_greater_that_35(self):
        self.assertEqual(self.sum.sum_to_number(36), 630)
        self.assertEqual(self.sum.sum_to_number(40), 630)
        self.assertEqual(self.sum.sum_to_number(50), 630)
        self.assertEqual(self.sum.sum_to_number(60), 630)

    def test_sum_to_number_not_greater_that_35(self):
        self.assertEqual(self.sum.sum_to_number(10), 55)
        self.assertEqual(self.sum.sum_to_number(20), 210)
        self.assertEqual(self.sum.sum_to_number(30), 465)

