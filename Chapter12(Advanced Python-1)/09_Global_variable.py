a = 89

def func(): # Define a function
    global a # Using global keyword to modify the global variable
    a = 4
    print(a)

func()
print(a)
