# A list contains the multiplication table of 7. write a program to convert it to vertical string of same numbers.

table_of_7 = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]

vertical_string = '\n'.join(str(num) for num in table_of_7)

print(vertical_string)
