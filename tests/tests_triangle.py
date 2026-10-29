import unittest
from triangle import area, perimeter

class TriangleTestCase(unittest.TestCase):
    def test_area_base_ten_height_five(self):
        self.assertEqual(area(10, 5), 25)
        
    def test_area_base_five_height_ten(self):
        self.assertEqual(area(5, 10), 25)
        
    def test_area_float_base_and_height(self):
        self.assertAlmostEqual(area(2.5, 2.5), 3.125)
        
    def test_perimeter_right_triangle(self):
        self.assertEqual(perimeter(3, 4, 5), 12)
        
    def test_perimeter_all_equal(self):
        self.assertEqual(perimeter(10, 10, 10), 30)
        
    def test_perimeter_float_sides(self):
        self.assertEqual(perimeter(1.5, 2, 2.5), 6)
 

