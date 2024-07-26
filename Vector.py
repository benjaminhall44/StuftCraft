
class Vector:
    def __init__(self, x: int|list = 0, y=0):
        if type(x) in (int, float):
            self.x = x
            self.y = y
        elif type(x) in (list, tuple):
            self.x = x[0]
            self.y = x[1]

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __neg__(self):
        return Vector(-self.x, -self.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vector(self.x / other, self.y / other)

    def __truediv__(self, other):
        return Vector(self.x / other, self.y / other)

    def __getitem__(self, item):
        if item == 0:
            return self.x
        else:
            return self.y

    def get_list(self):
        return [self.x, self.y]

    def magnitude(self):
        return (self.x ** 2 + self.y ** 2) ** .5

    def unit(self):
        return self / self.magnitude()

