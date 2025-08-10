# Check the type of variable assigned using input () function

a = input("Enter number 1: ") # input function always return string
print(type(a))

b = int(input("Enter number 2: "))  # input function always return string, so we have to typecast it to integer
print(type(b))
