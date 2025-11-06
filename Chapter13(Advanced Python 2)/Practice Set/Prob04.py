# 4. Write a program to filter a list of numbers which are divisible by 5.

numbers = [10, 15, 23, 42, 55, 60, 73, 80, 91, 660]

filtered_numbers = list(filter(lambda x: x % 5 == 0, numbers)) # Using filter and lambda function

print(filtered_numbers)
