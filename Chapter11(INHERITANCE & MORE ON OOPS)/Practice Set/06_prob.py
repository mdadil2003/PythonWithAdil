# Write __str__() method to print the vector as follows: 7i + 8j +10k Assume vector of dimension 3 for this problem.

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
        return " + ".join(f"{c}i" for c in self.components)

v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

print("Addition:", v1 + v2)
print("Dot Product:", v1 * v2)
