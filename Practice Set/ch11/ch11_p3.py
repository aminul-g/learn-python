'''
Create a class 'Employee' and add salary and increment properties to it.

Write a method ‘salaryAfterIncrement’ method with a @property decorator with a setter 
which changes the value of increment based on the salary.
'''
class Employee:
    def __init__(self, salary, increment):
        self._salary = salary
        self._increment = increment

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        self._salary = value

    @property
    def increment(self):
        return self._increment

    @increment.setter
    def increment(self, value):
        self._increment = value

    @property
    def salaryAfterIncrement(self):
        return self._salary + (self._salary * self._increment / 100)

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, value):
        self._increment = ((value - self._salary) / self._salary) * 100

# Example usage
employee = Employee(50000, 10)

print("Initial Salary:", employee.salary)
print("Initial Increment:", employee.increment)
print("Salary After Increment:", employee.salaryAfterIncrement)

# Changing the increment
employee.increment = 20
print("\nUpdated Increment:", employee.increment)
print("Salary After Increment:", employee.salaryAfterIncrement)

# Setting a new salary after increment
employee.salaryAfterIncrement = 65000
print("\nNew Increment:", employee.increment)
print("Salary After Increment:", employee.salaryAfterIncrement)
