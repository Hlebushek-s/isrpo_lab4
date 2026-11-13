import math
import unittest
from circle import area, perimeter


class CircleTestCase(unittest.TestCase):
    def test_area_string_radius(self):
        with self.assertRaises(TypeError):
            area("asd")

    def test_perimeter_string_radius(self):
        with self.assertRaises(TypeError):
            perimeter("asd")

    def test_area_numeric_string_radius(self):
        with self.assertRaises(TypeError):
            area("123")

    def test_perimeter_numeric_string_radius(self):
        with self.assertRaises(TypeError):
            perimeter("123")


    def test_area_unit_radius(self):
        self.assertAlmostEqual(area(1), 3.141592653589793)
 
    def test_area_standart_radius(self):
        self.assertAlmostEqual(area(5), 78.53981633974483)
 
    def test_area_float_radius(self):
        self.assertAlmostEqual(area(2.5), 19.634954084936208)
 
    def test_area_big_radius(self):
        self.assertAlmostEqual(area(100000), 31415926535.89793)
 
    def test_area_zero_radius(self):
        self.assertEqual(area(0), 0)
 
    def test_area_small_float_radius(self):
        self.assertAlmostEqual(area(0.1), 0.031415926535897934)
 
    def test_area_integer_radius_ten(self):
        self.assertAlmostEqual(area(10), 314.1592653589793)
 
    def test_area_non_integer_radius(self):
        self.assertAlmostEqual(area(3.7), 43.00840342764427)
 
 
 
    def test_perimeter_unit_radius(self):
        self.assertAlmostEqual(perimeter(1), 6.283185307179586)
 
    def test_perimeter_standart_radius(self):
        self.assertAlmostEqual(perimeter(5), 31.41592653589793)
 
    def test_perimeter_float_radius(self):
        self.assertAlmostEqual(perimeter(2.5), 15.707963267948966)
 
    def test_perimeter_big_radius(self):
        self.assertAlmostEqual(perimeter(100000), 628318.5307179586)
 
    def test_perimeter_zero_radius(self):
        self.assertEqual(perimeter(0), 0)
 
    def test_perimeter_small_float_radius(self):
        self.assertAlmostEqual(perimeter(0.1), 0.6283185307179586)
 
    def test_perimeter_integer_radius_ten(self):
        self.assertAlmostEqual(perimeter(10), 62.83185307179586)
 
    def test_perimeter_non_integer_radius(self):
        self.assertAlmostEqual(perimeter(3.7), 23.24778563656447)
 
 
 
    def test_area_negative_radius(self):
        self.assertAlmostEqual(area(-2), 12.566370614359172)
 
    def test_area_negative_float_radius(self):
        self.assertAlmostEqual(area(-0.5), 0.7853981633974483)
 
    def test_perimeter_negative_radius(self):
        self.assertAlmostEqual(perimeter(-2), -12.566370614359172)
 
    def test_perimeter_negative_float_radius(self):
        self.assertAlmostEqual(perimeter(-0.5), -3.141592653589793)



