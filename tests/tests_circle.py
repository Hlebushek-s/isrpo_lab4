import math
import unittest
from circle import area, perimeter

class CircleTestCase(unittest.TestCase):
    def test_area_radius_one(self):
        self.assertAlmostEqual(area(1), math.pi)
        
    def test_area_radius_two(self):
        self.assertAlmostEqual(area(2), 4 * math.pi)
        
    def test_area_zero_radius(self):
        self.assertEqual(area(0), 0)
        
    def test_area_float_radius(self):
        self.assertAlmostEqual(area(0.5), math.pi / 4)
        
    def test_perimeter_radius_one(self):
        self.assertAlmostEqual(perimeter(1), 2 * math.pi)
        
    def test_perimeter_radius_two(self):
        self.assertAlmostEqual(perimeter(2), 4 * math.pi)
        
    def test_perimeter_zero_radius(self):
        self.assertEqual(perimeter(0), 0)
        
    def test_perimeter_float_radius(self):
        self.assertAlmostEqual(perimeter(0.5), math.pi)
 

