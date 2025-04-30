# Q2. Write a program to accept marks of 6 students and display them in a sorted manner.

marks = [] # empty list to store Marks
m1 = int(input("Enter Marks: "))
marks.append(m1)
m2 = int(input("Enter Marks: "))
marks.append(m2)
m3 = int(input("Enter Marks: "))
marks.append(m3)
m4 = int(input("Enter Marks: "))
marks.append(m4)
m5 = int(input("Enter Marks: "))
marks.append(m5)
m6 = int(input("Enter Marks: "))
marks.append(m6)

marks.sort()  # sort the list in ascending order

print(marks)