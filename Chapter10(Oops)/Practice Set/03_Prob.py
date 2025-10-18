# Create a class with a class attribute a; create an object from it and set ‘a’directly using ‘object.a = 0’. Does this change the class attribute?

class Demo:
    a = 10  # class attribute

    def display(self):
        print("Value of a:", Demo.a)

obj = Demo()  # create an object of Demo class
obj.a = 0
obj.display()