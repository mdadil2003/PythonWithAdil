class Employee:  # defining a class
    
    language = "Python" # this is a class attribute
    company = "ZOHO"
    salary = 100000
    location = "Delhi"
    role = "SDE"
    
adil = Employee() 
adil.name = "Adil" # this is an instance attribute
print(adil.name, adil.company, adil.salary, adil.location, adil.role, adil.language)

