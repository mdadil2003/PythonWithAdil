# 5. Write a program to find the sum of first n natural numbers using while loop.

n = int(input("Enter a number: "))
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1
print("The sum of first", n, "natural numbers is:", sum) 
  