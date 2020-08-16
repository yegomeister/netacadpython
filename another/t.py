"""This practice module shows how arguments are passed to the respective superclasses using **kwargs in Multiple Inheritance"""


class Rect:
    """Rectangle Class"""

    def __init__(self, length, width, **kwargs):
        self.length = length
        self.width = width
        super().__init__(**kwargs)

    def perimeter(self):
        return 2 * (self.length + self.width)

    def area(self):
        return self.length * self.width


class Square(Rect):

    def __init__(self, length, **kwargs):
        super().__init__(length, length, **kwargs)


class Cube(Square):

    def __init__(self, length, name):
        super().__init__(length)
        self.name = name

    def surface_a(self):
        face_area = super(Square, self).area()
        return face_area * 6

    def vol(self):
        face_area = super().area()
        return face_area * self.length

    def say_name(self):
        print(self.name)


class Triangle:
    def __init__(self, base, height, **kwargs):
        self.base = base
        self.height = height
        super().__init__(**kwargs)

    def tri_area(self):
        return .5 * self.base * self.height


class Pyramid(Square, Triangle):
    def __init__(self, base, slant_height, **kwargs):
        self.base = base
        self.slant_height = slant_height
        kwargs['height'] = slant_height
        kwargs['base'] = base
        super().__init__(self.base, **kwargs)

    def surf_area(self):
        base_area = super().area()
        tri_area = super().tri_area()
        return tri_area * 4 + base_area


rp = Pyramid(4, 2)
print(rp.tri_area())
