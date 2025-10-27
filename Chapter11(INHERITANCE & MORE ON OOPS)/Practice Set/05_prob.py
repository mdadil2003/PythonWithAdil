# Write a class vector representing a vector of n dimensions. Overload the + and * operator which calculates the sum and the dot(.) product of them.

class Vector:
    def __init__(self, *components):
        self.components = components

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(*(a + b for a, b in zip(self.components, other.components)))
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Vector):
            return sum(a * b for a, b in zip(self.components, other.components))
        return NotImplemented

    def __str__(self):
        return f"Vector{self.components}"

v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

print("Addition:", v1 + v2)
print("Dot Product:", v1 * v2)
