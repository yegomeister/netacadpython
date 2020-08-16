from math import pi

class Circle:
    def area(self, radius):
        return round(pi, 2) * radius**2

class Square:
    def area(self, length):
        return length**2

class Shape:
    def __init__(self, shape):
        self.shape = shape

    def my_area(self, value):
        area = self.shape.area(value)
        return area


circ = Shape(Circle())
sq = Shape(Square())
print(circ.my_area(12))
print(sq.my_area(12))