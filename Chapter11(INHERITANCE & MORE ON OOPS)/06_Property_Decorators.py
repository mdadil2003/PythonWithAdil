class Employee:
    a = 1
    @classmethod
    def show(cls):    
        print(f"The value of a is {cls.a}")
    
    @property
    def name(self):
        return f"{self.name} {self.lname}"
    
    @name.setter
    def name(self, value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]
        
e = Employee()
e.a = 34

e.name = "Adil Raza"
print(e.fname, e.lname)

e.show()
        