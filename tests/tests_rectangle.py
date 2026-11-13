import unittest
from rectangle import area, perimeter


class RectangleTestCase(unittest.TestCase):
    def test_area_string_first_side(self):
        with self.assertRaises(TypeError):
            area("asd", 2)

    def test_area_string_second_side(self):
        with self.assertRaises(TypeError):
            area(2, "asd")

    def test_perimeter_string_first_side(self):
        with self.assertRaises(TypeError):
            perimeter("asd", 2)

    def test_perimeter_string_second_side(self):
        with self.assertRaises(TypeError):
            perimeter(10, "asd")

    def test_area_numeric_string_first_side(self):
        with self.assertRaises(TypeError):
            area("123", 2)

    def test_area_numeric_string_second_side(self):
        with self.assertRaises(TypeError):
            area(2, "123")

    def test_perimeter_numeric_string_first_side(self):
        with self.assertRaises(TypeError):
            perimeter("123", 2)

    def test_perimeter_numeric_string_second_side(self):
        with self.assertRaises(TypeError):
            perimeter(2, "123")


    def test_area_square_like(self):
        self.assertEqual(area(10, 10), 100)

    def test_area_standart_rectangle(self):
        self.assertEqual(area(5, 10), 50)

    def test_area_float_sides(self):
        self.assertAlmostEqual(area(2.5, 5), 12.5)

    def test_area_big_side(self):
        self.assertEqual(area(100000, 10), 1000000)

    def test_area_unit_sides(self):
        self.assertEqual(area(1, 1), 1)

    def test_area_zero_side(self):
        self.assertEqual(area(0, 5), 0)

    def test_area_small_float_sides(self):
        self.assertAlmostEqual(area(0.1, 0.2), 0.02)

    def test_area_mixed_int_and_float(self):
        self.assertAlmostEqual(area(7, 2.5), 17.5)

    def test_area_non_square_integers(self):
        self.assertEqual(area(3, 7), 21)

    def test_area_very_big_sides(self):
        self.assertEqual(area(100000, 100000), 1e10)




    def test_perimeter_square_like(self):
        self.assertEqual(perimeter(10, 10), 40)

    def test_perimeter_standart_rectangle(self):
        self.assertEqual(perimeter(5, 10), 30)

    def test_perimeter_float_sides(self):
        self.assertEqual(perimeter(2.5, 5), 15)

    def test_perimeter_big_side(self):
        self.assertEqual(perimeter(100000, 10), 200020)

    def test_perimeter_unit_sides(self):
        self.assertEqual(perimeter(1, 1), 4)

    def test_perimeter_zero_side(self):
        self.assertEqual(perimeter(0, 5), 10)

    def test_perimeter_small_float_sides(self):
        self.assertAlmostEqual(perimeter(0.1, 0.2), 0.6)

    def test_perimeter_mixed_int_and_float(self):
        self.assertAlmostEqual(perimeter(7, 2.5), 19)

    def test_perimeter_non_square_integers(self):
        self.assertEqual(perimeter(3, 7), 20)

    def test_perimeter_very_big_sides(self):
        self.assertEqual(perimeter(100000, 100000), 400000)



    def test_area_negative_first_side(self):
        self.assertEqual(area(-2, 3), -6)

    def test_area_negative_second_side(self):
        self.assertEqual(area(2, -3), -6)

    def test_area_both_sides_negative(self):
        self.assertEqual(area(-2, -3), 6)

    def test_area_negative_float_side(self):
        self.assertAlmostEqual(area(-0.5, 4), -2.0)

    def test_perimeter_negative_first_side(self):
        self.assertEqual(perimeter(-2, 3), 2)

    def test_perimeter_negative_second_side(self):
        self.assertEqual(perimeter(2, -3), -2)

    def test_perimeter_both_sides_negative(self):
        self.assertEqual(perimeter(-2, -3), -10)

    def test_perimeter_negative_float_side(self):
        self.assertAlmostEqual(perimeter(-0.5, 4), 7.0)



    def test_area_huge_positive_sides(self):
        self.assertEqual(area(1e50, 1e50), 1e100)

    def test_area_huge_side_times_one(self):
        self.assertEqual(area(1e50, 1), 1e50)

    def test_perimeter_huge_positive_sides(self):
        self.assertEqual(perimeter(1e50, 1e50), 4e50)

    def test_perimeter_huge_side_and_one(self):
        self.assertEqual(perimeter(1e50, 1),  200000000000000000000000000000000000000000000000002)

    def test_area_huge_negative_first_side(self):
        self.assertEqual(area(-1e50, 1e50), -1e100)

    def test_area_huge_negative_second_side(self):
        self.assertEqual(area(1e50, -1e50), -1e100)

    def test_area_huge_both_negative(self):
        self.assertEqual(area(-1e50, -1e50), 1e100)

    def test_perimeter_huge_negative_first_side(self):
        self.assertEqual(perimeter(-1e50, 1e50), 0)

    def test_perimeter_huge_negative_second_side(self):
        self.assertEqual(perimeter(1e50, -1e50), 0)

    def test_perimeter_huge_both_negative(self):
        self.assertEqual(perimeter(-1e50, -1e50), -4e50)


