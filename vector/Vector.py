from math import sqrt, acos, degrees, pi

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError("The coordinates must be nonempty")

        except TypeError:
            raise TypeError("The coordinates must be an iterable")

    def __str__(self):
        return "Vector: {}".format(self.coordinates)

    def __eq__(self, other):
        return self.coordinates == other.coordinates

    def add(self, other):
        new_coordinates = [x + y for x, y in zip(self.coordinates, other.coordinates)]
        return Vector(new_coordinates)

    def subtract(self, other):
        new_coordinates = [x - y for x, y in zip(self.coordinates, other.coordinates)]
        return Vector(new_coordinates)

    def scalar_multiply(self, scalar):
        new_coordinates = [scalar * coordinate for coordinate in self.coordinates]
        return Vector(new_coordinates)

    def magnitude(self):
        return sqrt(sum([coordinate**2 for coordinate in self.coordinates]))

    # Base unit
    def normalize(self):
        return self.scalar_multiply(1.00 / self.magnitude())

    def dot_product(self, other):
        return sum([x * y for x, y in zip(self.coordinates, other.coordinates)])

    # Returns the arc cosine of the dot product between self and other, in radians
    def angle_in_radian(self, other):
        v1 = self.normalize()
        v2 = other.normalize()
        return acos(v1.dot_product(v2))

    # Returns the the arc cosine of the angle between vector (self) and vector (other)
    def angle_in_degrees(self, other):
        return degrees(self.angle_in_radian(other))

    def is_parallel_to(self, other, tolerance=1e-10):
        return (
            self.is_zero() or
            other.is_zero() or
            self.angle_in_radian(other) == pi or
            self.angle_in_degrees(other) < tolerance
        )

    def is_zero(self, tolerance=1e-10):
        return self.magnitude() < tolerance
