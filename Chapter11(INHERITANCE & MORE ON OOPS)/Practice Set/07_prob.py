# Override the __len__() method on vector of problem 5 to display the dimension of the vector.

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

    def __len__(self):
        return len(self.components)

v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

print("Addition:", v1 + v2)
print("Dot Product:", v1 * v2)
print("Dimension of v1:", len(v1))
print("Dimension of v2:", len(v2))
