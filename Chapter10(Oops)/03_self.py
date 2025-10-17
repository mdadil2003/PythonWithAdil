class Employee:
    language = "Python" # this is a class attribute
    salary = 1200000
    
    def getInfo(self):
        print(f"Language is {self.language} and salary is {self.salary}")
    def greet(self): # another method
        print("Hello!")
        
        
harry = Employee()
harry.language = "Java" # this creates an instance attribute

harry.greet() # calling another method

harry.getInfo() # calling the method using the instance

Employee.getInfo(harry) # another way of calling the method
