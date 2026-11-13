import unittest
from triangle import area, perimeter


class TriangleTestCase(unittest.TestCase):
    def test_area_string_base(self):
        with self.assertRaises(TypeError):
            area("asd", 2)

    def test_area_string_height(self):
        with self.assertRaises(TypeError):
            area(2, "asd")

    def test_perimeter_string_first_side(self):
        with self.assertRaises(TypeError):
            perimeter("asd", 2, 3)

    def test_perimeter_string_second_side(self):
        with self.assertRaises(TypeError):
            perimeter(2, "asd", 3)

    def test_perimeter_string_third_side(self):
        with self.assertRaises(TypeError):
            perimeter(2, 3, "x")

    def test_area_numeric_string_base(self):
        with self.assertRaises(TypeError):
            area("123", 2)

    def test_area_numeric_string_height(self):
        with self.assertRaises(TypeError):
            area(2, "123")

    def test_perimeter_numeric_string_first_side(self):
        with self.assertRaises(TypeError):
            perimeter("123", 2, 3)

    def test_perimeter_numeric_string_third_side(self):
        with self.assertRaises(TypeError):
            perimeter(2, 3, "123")


    def test_area_square_like(self):
        self.assertEqual(area(10, 10), 50)

    def test_area_standart_triangle(self):
        self.assertEqual(area(5, 10), 25)

    def test_area_float_sides(self):
        self.assertAlmostEqual(area(2.5, 4), 5.0)

    def test_area_big_side(self):
        self.assertEqual(area(100000, 10), 500000)

    def test_area_unit_sides(self):
        self.assertEqual(area(1, 1), 0.5)

    def test_area_zero_side(self):
        self.assertEqual(area(0, 5), 0)

    def test_area_small_float_sides(self):
        self.assertAlmostEqual(area(0.1, 0.2), 0.01)

    def test_area_mixed_int_and_float(self):
        self.assertAlmostEqual(area(7, 2.5), 8.75)

    def test_area_non_square_integers(self):
        self.assertEqual(area(3, 7), 10.5)



    def test_perimeter_equilateral(self):
        self.assertEqual(perimeter(5, 5, 5), 15)

    def test_perimeter_standart_triangle(self):
        self.assertEqual(perimeter(3, 4, 5), 12)

    def test_perimeter_float_sides(self):
        self.assertEqual(perimeter(2.5, 5, 2.5), 10)

    def test_perimeter_big_side(self):
        self.assertEqual(perimeter(100000, 10, 10), 100020)

    def test_perimeter_unit_sides(self):
        self.assertEqual(perimeter(1, 1, 1), 3)

    def test_perimeter_zero_side(self):
        self.assertEqual(perimeter(0, 5, 5), 10)

    def test_perimeter_small_float_sides(self):
        self.assertAlmostEqual(perimeter(0.1, 0.2, 0.3), 0.6)

    def test_perimeter_mixed_int_and_float(self):
        self.assertAlmostEqual(perimeter(7, 2.5, 1), 10.5)

    def test_perimeter_very_big_sides(self):
        self.assertEqual(perimeter(100000, 100000, 100000), 300000)



    def test_area_negative_base(self):
        self.assertEqual(area(-2, 3), -3)

    def test_area_negative_height(self):
        self.assertEqual(area(2, -3), -3)

    def test_area_both_sides_negative(self):
        self.assertEqual(area(-2, -3), 3)

    def test_area_negative_float_side(self):
        self.assertAlmostEqual(area(-0.5, 4), -1.0)

    def test_perimeter_negative_first_side(self):
        self.assertEqual(perimeter(-2, 3, 4), 5)

    def test_perimeter_negative_second_side(self):
        self.assertEqual(perimeter(2, -3, 4), 3)

    def test_perimeter_all_sides_negative(self):
        self.assertEqual(perimeter(-2, -3, -4), -9)

    def test_perimeter_negative_float_side(self):
        self.assertAlmostEqual(perimeter(-0.5, 4, 4), 7.5)



    def test_area_huge_base_times_one(self):
        self.assertEqual(area(1e50, 0), 0)

    def test_perimeter_huge_positive_sides(self):
        self.assertEqual(perimeter(1e50, 1e50, 1e50), 3e50)

    def test_perimeter_huge_side_and_one(self):
        self.assertEqual(perimeter(1e50, 1, 1), 100000000000000000000000000000000000000000000000002)

    def test_perimeter_huge_negative_first_side(self):
        self.assertEqual(perimeter(-1e50, 1e50, 0), 0)

    def test_perimeter_huge_both_negative(self):
        self.assertEqual(perimeter(-1e50, -1e50, -1e50), -3e50)


if __name__ == "__main__":
    unittest.main()
