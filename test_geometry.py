import unittest
from geometry import Circle, Triangle, calculate_area


class TestGeometryLibrary(unittest.TestCase):
    def test_circle_area(self):
        circle = Circle(3)
        self.assertAlmostEqual(circle.area(), 28.274333882308138, places=5)

    def test_triangle_area(self):
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(triangle.area(), 6, places=5)

    def test_right_angle_triangle(self):
        triangle = Triangle(3, 4, 5)
        self.assertTrue(triangle.is_right_angle())

    def test_not_right_angle_triangle(self):
        triangle = Triangle(3, 4, 6)
        self.assertFalse(triangle.is_right_angle())

    def test_calculate_area_circle(self):
        circle = Circle(3)
        self.assertAlmostEqual(calculate_area(circle), 28.274333882308138, places=5)

    def test_calculate_area_triangle(self):
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(calculate_area(triangle), 6, places=5)


if __name__ == '__main__':
    unittest.main()


