# function definition : The part containing the exact set of instructions which are executed during the function call.

def avg():
    a = int(input("Enter your number:"))
    b = int(input("Enter your number:"))
    c = int(input("Enter your number:"))
    
    average = (a + b + c)/3
    print(average)
    
avg()  # Call the function once
print("Function successfully executed.")
