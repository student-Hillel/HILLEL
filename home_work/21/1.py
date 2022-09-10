import math

class Point():

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

    def __str__(self):
        return f'({self.x}, {self.y})'

    def distance_from_origin(self):
        return math.hypot(self.x, self.y)


class Circle(Point):

    def __init__(self, radius, x=0, y=0):
        super().__init__(x, y)
        self.radius = radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __str__(self):
        return super().__str__()[:-1] + f', radius={self.radius})'

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        radius = abs(self.radius - other.radius)
        if self.radius == other.radius:
            return Point(x, y)
        else:
            return Circle(radius, x, y)

    def edge_distance_from_origin(self):
        return abs(self.distance_from_origin() - self.radius)

    def area(self):
        return math.pi * (self.radius**2)



circle_1 = Circle(7, 9, 3)
print(circle_1)

circle_2 = Circle(10, 6, 2)
print(circle_2)

print('-'*50)

circle_3 = circle_1 - circle_2
print(circle_3)

