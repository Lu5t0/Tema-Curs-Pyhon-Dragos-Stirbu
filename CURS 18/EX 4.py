import math

class Shape:
    def area(self):
        raise NotImplementedError

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return 0.5 * self.base * self.height


if __name__ == '__main__':
    shapes = [Rectangle(5,10),
              Circle(5),
              Triangle(5,10),
              Rectangle(2,7),
              Circle(1.3)]
    total_area = sum(shape.area() for shape in shapes)

    print(f"Aria totala a tuturor formelor este:{total_area:.2f    }")