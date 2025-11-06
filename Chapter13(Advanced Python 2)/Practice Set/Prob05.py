# Write a program to find the maximum of the numbers in a list using the reduce function.

from functools import reduce

numbers = [12, 45, 2, 67, 34, 89, 23, 90, 11]

max_number = reduce(lambda a, b: a if a > b else b, numbers) # Using reduce and lambda function

print("The maximum number in the list is:", max_number)
