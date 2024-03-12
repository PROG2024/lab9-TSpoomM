"""
Unit tests of the Circle class using unittest or pytest (your choice).

Write unit tests as described in README.md.

1. Unit test for add_area using typical values.
2. Unit test for add_area for an "edge case" where one circle has radius 0.
3. Unit test that circle constructor raises exception of radius is negative.


"""
import unittest
from circle import Circle


class CircleTest(unittest.TestCase):

    def setUp(self):
        """ Create an auction before each test. """

        self.circle1 = Circle(3)  # Circle with radius 3
        self.circle2 = Circle(4)  # Circle with radius 4
        self.circle3 = Circle(0)  # circle with radius 0

    def test_add_area_typical_values(self):
        """ Test add_area with typical values. """

        combined_circle = self.circle1.add_area(self.circle2)
        expected_radius = 5  # The radius of the combined circle (3^2 + 4^2 = 5^2)

        self.assertAlmostEquals(combined_circle.get_radius(), expected_radius)
        self.assertTrue(combined_circle.get_area() >= self.circle1.get_area())
        self.assertTrue(combined_circle.get_area() >= self.circle2.get_area())

    def test_add_area_edge_case(self):
        """ Test add_area with an edge case where one circle has radius 0. """

        combined_circle = self.circle3.add_area(self.circle2)
        combined_circle2 = self.circle3.add_area(self.circle3)

        self.assertAlmostEquals(combined_circle2.get_radius(), self.circle3.get_radius())
        self.assertAlmostEquals(combined_circle.get_radius(), self.circle2.get_radius())

    def test_circle_constructor_negative_radius(self):
        """ Test that circle constructor raises exception if radius is negative. """

        with self.assertRaises(ValueError):
            Circle(-2)

        with self.assertRaises(ValueError):
            Circle(-5)
