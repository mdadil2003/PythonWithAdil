# Create a class “Programmer” for storing information of few programmers working at Microsoft.

class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin

p =  Programmer("Adil", 100000, 1234)
print(p.name, p.salary, p.pin, p.company)
q = Programmer("Rohan", 120000, 5678)
print(q.name, q.salary, q.pin, q.company)