class Employee:
    language = "Python" # this is a class attribute
    salary = 100000
    
harry = Employee()
harry.language = "Java" # this creates an instance attribute
print(harry.language, harry.salary) # prints Java 100000 