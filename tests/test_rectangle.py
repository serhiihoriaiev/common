import unittest
from tests.homework import *


class TestRectangle(unittest.TestCase):

    def test_rectangle_perimeter_int(self):
        test_obj = Rectangle(5, 3)
        expected_result = 16
        self.assertEqual(test_obj.get_rectangle_perimeter(), expected_result)

    def test_rectangle_perimeter_float(self):
        test_obj = Rectangle(1.6, 3.0)
        expected_result = 9.2
        self.assertEqual(test_obj.get_rectangle_perimeter(), expected_result)

    def test_rectangle_perimeter_with_wrong_data(self):
        test_obj = Rectangle(5, 0)
        self.assertIsNone(test_obj.get_rectangle_perimeter())

    def test_rectangle_square(self):
        test_obj = Rectangle(4, 6)
        expected_result = 24
        self.assertEqual(test_obj.get_rectangle_square(), expected_result)

    def test_rectangle_square_wrong_data(self):
        test_obj = Rectangle(4, -6)
        self.assertIsNone(test_obj.get_rectangle_square())

    def test_rectangle_square_not_str(self):
        test_obj = Rectangle(4, 6)
        self.assertNotIsInstance(test_obj.get_rectangle_square(), str)

    def test_sum_of_corners(self):
        test_obj = Rectangle(1, 43)
        self.assertEqual(test_obj.get_sum_of_corners(3), 270)

    def test_sum_of_corners_exception(self):
        test_obj = Rectangle(1, 43)
        with self.assertRaises(ValueError):
            test_obj.get_sum_of_corners(23)

    def test_rectangle_diagonal(self):
        test_obj = Rectangle(13, 6)
        self.assertEqual(test_obj.get_rectangle_diagonal(), 14.32)

    def test_rectangle_diagonal_wrong_data(self):
        test_obj = Rectangle(13, "6")
        with self.assertRaises(TypeError):
            test_obj.get_rectangle_diagonal()

    def test_circumscribed_circle(self):
        test_obj = Rectangle(13, 6)
        self.assertEqual(test_obj.get_radius_of_circumscribed_circle(), 7.16)

    def test_circumscribed_circle_wrong_data(self):
        test_obj = Rectangle([13, ], 6)
        with self.assertRaises(TypeError):
            test_obj.get_radius_of_circumscribed_circle()

    def test_inscribed_circle(self):
        test_obj = Rectangle(6, 6)
        self.assertEqual(test_obj.get_radius_of_inscribed_circle(), 3)

    def test_iscribed_circle(self):
        test_obj = Rectangle(6, 16)
        with self.assertRaises(ValueError):
            test_obj.get_radius_of_inscribed_circle()

if __name__ == "__main__":
    unittest.main()