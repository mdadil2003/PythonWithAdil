# Create a class (2-D vector) and use it to create another class representing a 3-D vector.

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def show(self):
        print(f"Vector2D: ({self.x}x + {self.y}y)")    

class Vector3D(Vector2D):  # Inheriting from Vector2D
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def show(self):
        print(f"Vector3D: ({self.x}x + {self.y}y + {self.z}z)")

a = Vector2D(6, 2) # Creating an object of Vector2D
a.show()
b = Vector3D(4, 5, 6) # Creating an object of Vector3D
b.show()
