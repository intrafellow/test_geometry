import math
from abc import ABC, abstractmethod


# Интерфейс для геометрических фигур
class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def type(self) -> str:
        pass


# Класс для круга
class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2

    def type(self) -> str:
        return "Circle"


# Класс для треугольника
class Triangle(Shape):
    def __init__(self, side1: float, side2: float, side3: float):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self) -> float:
        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

    def is_right_angle(self) -> bool:
        sides = sorted([self.side1, self.side2, self.side3])
        return math.isclose(sides[0] ** 2 + sides[1] ** 2, sides[2] ** 2)

    def type(self) -> str:
        return "Triangle"


def calculate_area(shape: Shape) -> float:
    return shape.area()
