import unittest
from square import area, perimeter


class SquareTestCase(unittest.TestCase):
    def test_area_string_side(self):
        with self.assertRaises(TypeError):
            area("asd")

    def test_perimeter_string_side(self):
        with self.assertRaises(TypeError):
            perimeter("asd")

    def test_area_numeric_string_side(self):
        with self.assertRaises(TypeError):
            area("123")

    def test_perimeter_numeric_string_side(self):
        with self.assertRaises(TypeError):
            perimeter("123")


    def test_area_unit_side(self):
        self.assertEqual(area(1), 1)

    def test_area_standart_side(self):
        self.assertEqual(area(5), 25)

    def test_area_float_side(self):
        self.assertAlmostEqual(area(2.5), 6.25)

    def test_area_big_side(self):
        self.assertEqual(area(100000), 10000000000)

    def test_area_zero_side(self):
        self.assertEqual(area(0), 0)

    def test_area_small_float_side(self):
        self.assertAlmostEqual(area(0.1), 0.01)

    def test_area_integer_side_ten(self):
        self.assertEqual(area(10), 100)

    def test_area_non_integer_side(self):
        self.assertAlmostEqual(area(3.7), 13.69)



    def test_perimeter_unit_side(self):
        self.assertEqual(perimeter(1), 4)

    def test_perimeter_standart_side(self):
        self.assertEqual(perimeter(5), 20)

    def test_perimeter_float_side(self):
        self.assertEqual(perimeter(2.5), 10)

    def test_perimeter_big_side(self):
        self.assertEqual(perimeter(100000), 400000)

    def test_perimeter_zero_side(self):
        self.assertEqual(perimeter(0), 0)

    def test_perimeter_small_float_side(self):
        self.assertAlmostEqual(perimeter(0.1), 0.4)

    def test_perimeter_integer_side_ten(self):
        self.assertEqual(perimeter(10), 40)

    def test_perimeter_non_integer_side(self):
        self.assertAlmostEqual(perimeter(3.7), 14.8)



    def test_area_negative_side(self):
        self.assertEqual(area(-3), 9)

    def test_area_negative_float_side(self):
        self.assertAlmostEqual(area(-0.5), 0.25)

    def test_perimeter_negative_side(self):
        self.assertEqual(perimeter(-3), -12)

    def test_perimeter_negative_float_side(self):
        self.assertAlmostEqual(perimeter(-0.5), -2.0)



    def test_area_huge_side(self):
        self.assertEqual(area(1e50), 1e100)

    def test_area_huge_side_times_one(self):
        self.assertEqual(area(1), 1)

    def test_perimeter_huge_side(self):
        self.assertEqual(perimeter(1e50), 4e50)
        

    def test_area_huge_negative_side(self):
        self.assertEqual(area(-1e50), 1e100)

    def test_perimeter_huge_negative_side(self):
        self.assertEqual(perimeter(-1e50), -4e50)



