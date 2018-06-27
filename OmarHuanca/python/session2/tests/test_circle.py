import unittest

from OmarHuanca.python.session2.Circle import Circle


class TestCircle(unittest.TestCase):
    """
    Test to Circle class.
    """

    def setUp(self):
        self.circle = Circle

    def test_circle_area_with_radius_greater_that_10(self):
        self.assertEqual(self.circle.circle_area(11), 380.132711084365)
        self.assertEqual(self.circle.circle_area(24), 1809.5573684677208)

    def test_circle_area_with_radius_not_greater_that_10(self):
        self.assertEqual(self.circle.circle_area(4), "radius is not greater that 10")
        self.assertEqual(self.circle.circle_area(10), "radius is not greater that 10")
