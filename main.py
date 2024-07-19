from geometry import Circle, Triangle

if __name__ == '__main__':
    circle = Circle(5)
    triangle = Triangle(3, 4, 5)

    print(f"Площадь круга с радиусом 5: {circle.area()}")
    print(f"Площадь треугольника со сторонами 3, 4, 5: {triangle.area()}")
    print(f"Является ли треугольник со сторонами 3, 4, 5 прямоугольным? {triangle.is_right_angle()}")
