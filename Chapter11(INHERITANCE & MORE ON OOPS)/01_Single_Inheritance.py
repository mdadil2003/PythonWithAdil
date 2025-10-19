class Employee:
    company = "ITC"
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")


#class Programmer(Employee): # Inheritance
#     def show(self):
#         print(f"The name is {self.name}, the salary is {self.salary}, and the programming language is {self.language}")
        
#         def showLanguage(self): # New method in derived class
#             print(f"The name is {self.name} and the programming language is {self.language}")


class Programmer(Employee): # Inheritance
    company = "ITC InfoTech" 
    def showLanguage(self): # New method in derived class
        print(f"The name is {self.name} and he is good with {self.language} language")


a = Employee()
b = Programmer()

print(a.company, b.company)
