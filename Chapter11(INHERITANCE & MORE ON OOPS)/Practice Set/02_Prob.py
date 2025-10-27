# Create a class ‘Pets’ from a class ‘Animals’ and further create a class ‘Dog’ from ‘Pets’. Add a method ‘bark’ to class ‘Dog’.  

class Animals:
    def __init__(self, name):
        self.name = name

class Pets(Animals):
    def __init__(self, name, owner):
        super().__init__(name)
        self.owner = owner

class Dog(Pets):
    def __init__(self, name, owner, breed):
        super().__init__(name, owner)
        self.breed = breed

    def bark(self):
        print(f"{self.name} says Woof!")
d = Dog("Buddy", "Alice", "Golden Retriever")
d.bark()
print(f"Dog Name: {d.name}, Owner: {d.owner}, Breed: {d.breed}")