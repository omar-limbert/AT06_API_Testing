import unittest

from OmarHuanca.python.session2.DaysInMonth import DaysInMonth


class TestDaysInMonth(unittest.TestCase):
    """
    Test to DaysInMonth Class.
    """

    def setUp(self):
        self.days_in_month = DaysInMonth

    def test_get_days_in_month_with_lower_case(self):
        self.assertEqual(self.days_in_month.get_days_in_month("june"), 30)
        self.assertEqual(self.days_in_month.get_days_in_month("july"), 31)
        self.assertEqual(self.days_in_month.get_days_in_month("august"), 31)
        self.assertEqual(self.days_in_month.get_days_in_month("february"), 28)

    def test_get_days_in_month_with_upper_case(self):
        self.assertEqual(self.days_in_month.get_days_in_month("JUNE"), 30)
        self.assertEqual(self.days_in_month.get_days_in_month("JULY"), 31)
        self.assertEqual(self.days_in_month.get_days_in_month("AUGUST"), 31)
        self.assertEqual(self.days_in_month.get_days_in_month("FEBRUARY"), 28)

    def test_get_days_with_invalid_month(self):
        self.assertEqual(self.days_in_month.get_days_in_month("JUN"), "Month not found.")
        self.assertEqual(self.days_in_month.get_days_in_month("Jul"), "Month not found.")
