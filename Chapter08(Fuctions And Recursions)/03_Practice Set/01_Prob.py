# 1. Write a program using functions to find greatest of three numbers.

# a = 1 
# b = 2
# c = 3

def greatest(a, b, c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>b and c>a):
        return c
    
    a = 1
    b = 2
    c = 3
    
    print(f"The greatest number is: {greatest(a, b, c)}")
    
    
    