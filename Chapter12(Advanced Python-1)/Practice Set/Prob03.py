# Write a list comprehension to print a list which contains the multiplication table of a user entered number.

num = int(input("Enter a number to generate its multiplication table: "))

multiplication_table = [num * i for i in range(1, 11)]
print(f"Multiplication table of {num}: {multiplication_table}")
