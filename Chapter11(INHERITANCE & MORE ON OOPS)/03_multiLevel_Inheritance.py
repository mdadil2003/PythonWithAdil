class Employee:
    a = 1
    
class Programmer(Employee):
    b = 2
    
class Manager(Programmer):
    c = 3
    
o = Employee()
print(o.a) # Print the a attribtue
#print(o.b) # show an error as there  is no b atribute in employee class

o = Programmer()
print(o.a, o.b)

o = Manager()
print(o.a, o.b, o.c)

o = Programmer()
print(o.a, o.b)

o = Employee()
print(o.a)
