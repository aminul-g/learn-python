''' 
 Write a class ‘Complex’ to represent complex numbers, along with overloaded 
operators ‘+’ and ‘*’ which adds and multiplies them.
'''
class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        if isinstance(other, Complex):
            return Complex(self.real + other.real, self.imaginary + other.imaginary)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Complex):
            real_part = self.real * other.real - self.imaginary * other.imaginary
            imaginary_part = self.real * other.imaginary + self.imaginary * other.real
            return Complex(real_part, imaginary_part)
        return NotImplemented

    def __str__(self):
        if self.imaginary < 0:
            return f"{self.real} - {-self.imaginary}i"
        return f"{self.real} + {self.imaginary}i"

# Example usage
c1 = Complex(2, 3)
c2 = Complex(1, 4)

c3 = c1 + c2
c4 = c1 * c2

print(f"({c1}) + ({c2}) = ({c3})")
print(f"({c1}) * ({c2}) = ({c4})")
