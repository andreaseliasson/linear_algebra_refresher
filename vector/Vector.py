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
