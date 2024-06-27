'''
Write a class vector representing a vector of n dimensions. Overload the + and * 
operator which calculates the sum and the dot(.) product of them.
'''
class Vector:
    def __init__(self, *components):
        self.components = list(components)

    def __add__(self, other):
        if isinstance(other, Vector) and len(self.components) == len(other.components):
            added_components = [a + b for a, b in zip(self.components, other.components)]
            return Vector(*added_components)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Vector) and len(self.components) == len(other.components):
            dot_product = sum(a * b for a, b in zip(self.components, other.components))
            return dot_product
        return NotImplemented

    def __str__(self):
        return f"Vector({', '.join(map(str, self.components))})"

# Example usage
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

v3 = v1 + v2
dot_product = v1 * v2

print(f"({v1}) + ({v2}) = ({v3})")
print(f"({v1}) . ({v2}) = {dot_product}")
