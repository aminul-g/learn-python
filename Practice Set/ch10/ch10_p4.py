'''
Add a static method in problem 2, to greet the user with hello.
'''
from math import sqrt

class Calculator:
    def __init__(self, number):
        self.number = number

    def display(self):
        print(self.number)

    def square(self):
        return self.number ** 2

    def cube(self):
        return self.number ** 3

    def sqroot(self):
        return sqrt(self.number)
    @staticmethod
    def hello():
        print("Hello World!\n")

calc = Calculator(10)

calc.hello()
square_result = calc.square()
cube_result = calc.cube()
sqroot_result = calc.sqroot()

print("Square:", square_result)
print("Cube:", cube_result)
print("Square Root:", sqroot_result)
