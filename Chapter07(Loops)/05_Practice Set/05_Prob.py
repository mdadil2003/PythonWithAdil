# 6. Write a program to find the factorial of a number using while loop.

n = int(input("Enter a number: "))
factorial = 1
i = 1
while i <= n:
    factorial *= i
    i += 1
print("The factorial of", n, "is:", factorial)
