# Write a program to print the following star pattern.
# * * *
# *   *     for n = 3
# * * *

n = int(input("Entern the number: "))
for i in range(1, n + 1):
    if(i==1 or i == n):
        print("*" * n)
    else:
        print("*" + " " * (n - 2) + "*")