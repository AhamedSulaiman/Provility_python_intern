import math

class Shape:
    def s(self):
        print("Area of circle and square are")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

circle = Circle(5)
square = Square(4)
circle.s()
print(f"Circle Area: {circle.area():.2f}")
print(f"Square Area: {square.area()}")
