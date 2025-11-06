# Write a program to input name, marks and phone number of a student and format itusing the format function like below:- “The name of the student is Harry, his marks are 72 and phone number is 99999888”

name = input("Enter the name of the student: ")
marks = input("Enter the marks of the student: ")

phone_number = input("Enter the phone number of the student: ")

formatted_string = "The name of the student is {}, his marks are {} and phone number is {}".format(name, marks, phone_number)
print(formatted_string)
