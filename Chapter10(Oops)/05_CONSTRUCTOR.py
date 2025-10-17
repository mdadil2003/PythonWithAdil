class Employee:
    language = "Python" # this is a class attribute
    salary = 1200000


    def __init__(self): # dunder method which is automatically called when an object is created
        print("I am creating an object")
    
    
    def getInfo(self):
        print(f"Language is {self.language} and salary is {self.salary}")
               
        
harry = Employee()
harry.name = "Harry"
print(harry.name, harry.language, harry.salary)
