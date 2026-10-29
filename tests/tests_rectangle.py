import unittest
from rectangle import area, perimeter

class RectangleTestCase(unittest.TestCase):
    def test_area_square_like(self):
        self.assertEqual(area(10, 10), 100)
        
    def test_area_standart_rectangle(self):
        self.assertEqual(area(5, 10), 50)
        
    def test_area_float_sides(self):
        self.assertAlmostEqual(area(2.5, 5), 12.5)
        
        
    def test_perimeter_square_like(self):
        self.assertEqual(perimeter(10, 10), 40)
        
    def test_perimeter_standart_rectangle(self):
        self.assertEqual(perimeter(5, 10), 30)
    
    def test_perimeter_float_sides(self):
        self.assertEqual(perimeter(2.5, 5), 15)
