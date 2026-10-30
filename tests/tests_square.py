import unittest 
from square import area, perimeter

class SquareTestCase(unittest.TestCase):
    def test_area_side_five(self):
        self.assertEqual(area(5), 25)
        
    def test_area_side_ten(self):
        self.assertEqual(area(10), 100)
        
    def test_area_float_side(self):
        self.assertEqual(area(2.5), 6.25)
    
    def test_area_big_side(self):
        self.assertEqual(area(100000), 10000000000)
    
    
    def test_perimeter_side_five(self):
        self.assertEqual(perimeter(5), 20)
        
    def test_perimeter_side_ten(self):
        self.assertEqual(perimeter(10), 40)
        
    def test_perimeter_float_side(self):
        self.assertEqual(perimeter(2.5), 10)
    
    def test_perimeter_big_side(self):
        self.assertEqual(perimeter(100000), 400000)
