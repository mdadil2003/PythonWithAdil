# Multiple Inheritance occurs when the child class inherits from more than one parent classes.

class Employee:
    company = "ITC"
    def show(self):
        print(f"The name is {self.language} and the salary is {self.company}")

class Coder:
    language = "Python"
    def printLanguage(self):
        print(f"The language is {self.language}")



class Programmer(Employee, Coder): # Inheritance
    company = "ITC InfoTech" 
    def showLanguage(self): # New method in derived class
        print(f"The name is {self.company} and he is good with {self.language} language")


a = Employee()
b = Programmer()

b.show()
b.printLanguage()
b.showLanguage()
