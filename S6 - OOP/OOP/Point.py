# lesson 16: operators overloading
class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y, self.z + other.z)

    def __str__(self):
        return f'x: {self.x}, y: {self.y}. z: {self.z}'


p1 = Point(10, 40, -50)
p2 = Point(-60, 100, 60)
p3 = p1 + p2
print(p3)
