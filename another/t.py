"""This practice module shows how arguments are passed to the respective superclasses using **kwargs in Multiple
Inheritance """


class Triangle:
    def __init__(self, base, height, **kwargs):
        self.base = base
        self.height = height
        super().__init__(**kwargs)

    def tri_area(self):
        return .5 * self.base * self.height


class Rect:
    def __init__(self, length, width, **kwargs):
        self.length = length
        self.width = width
        super().__init__(**kwargs)  # call to Triangle's __init__()

    def perimeter(self):
        return 2 * (self.length + self.width)

    def area(self):
        return self.length * self.width


class Square(Rect):

    def __init__(self, length, **kwargs):
        super().__init__(length, length, **kwargs)  # call to Rect's __init__()


class Cube(Square):

    def __init__(self, length):
        super().__init__(length)

    def surface_a(self):
        face_area = super(Square, self).area()
        return face_area * 6

    def vol(self):
        face_area = super().area()
        return face_area * self.length


class Pyramid(Square, Triangle):
    """The Pyramid class modifies **kwargs so that any instance of Pyramid is called with only the appropriate
    methods """

    def __init__(self, base, slant_height, **kwargs):
        self.base = base
        self.slant_height = slant_height
        kwargs['height'] = slant_height
        kwargs['base'] = base
        super().__init__(self.base, **kwargs)  # call to Square's __init__()

    def surf_area(self):
        base_area = super().area()
        tri_area = super().tri_area()
        return tri_area * 4 + base_area


rp = Pyramid(4, 2)
sq = Square(8)
print(sq.area())
print(rp.tri_area())
print(rp.surf_area())
