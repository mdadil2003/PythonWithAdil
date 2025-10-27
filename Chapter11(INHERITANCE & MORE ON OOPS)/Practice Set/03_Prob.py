# Create a class ‘Employee’ and add salary and increment properties to it. Write a method ‘salaryAfterIncrement’ method with a @property decorator with a setter which changes the value of increment based on the salary.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.increment = 0.2  # default increment of 20%

    @property
    def salaryAfterIncrement(self):
        return self.salary + (self.salary * self.increment)

    @salaryAfterIncrement.setter # Setter to change increment value
    def salaryAfterIncrement(self, new_increment):
        self.increment = new_increment

emp = Employee("John", 50000)
print(f"Salary after increment: {emp.salaryAfterIncrement}")

emp.salaryAfterIncrement = 0.2  # changing increment to 20%
print(f"Salary after increment: {emp.salaryAfterIncrement}")
