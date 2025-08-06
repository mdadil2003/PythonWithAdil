# Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.

marks1 = int(input("Enter marks for subject 1: "))
marks2 = int(input("Enter marks for subject 2: "))
marks3 = int(input("Enter marks for subject 3: "))

total_marks = marks1 + marks2 + marks3 
total_percentage = (total_marks / 300) * 100  

if total_percentage >= 40 and marks1 >= 33 and marks2 >= 33 and marks3 >= 33:
    print("The student has passed:", total_percentage,"%")
    print("Congratulations!")   

else:
    print("The student has failed:", total_percentage,"%")
    print("Please try again.")