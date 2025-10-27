# Write a class ‘Complex’ to represent complex numbers, along with overloaded operators ‘+’ and ‘*’ which adds and multiplies them.

class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        if isinstance(other, Complex): # Overloading the + operator
            return Complex(self.real + other.real, self.imag + other.imag)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Complex):
            return Complex(self.real * other.real - self.imag * other.imag,
                           self.real * other.imag + self.imag * other.real)
        return NotImplemented # Overloading the * operator

    def __str__(self):
        return f"({self.real} + {self.imag}i)"

c1 = Complex(2, 3)
c2 = Complex(4, 5)

print("Addition:", c1 + c2)
print("Multiplication:", c1 * c2)
