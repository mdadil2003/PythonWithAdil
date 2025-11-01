# List Comprehension is an elegant way to create lists based on existing lists.

myList = [1, 4, 5, 7, 9, 12]

# squaredList =  []
# for item in myList:
#     squaredList.append(item ** 2)

squaredList = [i*i for i in myList] # List comprehension to create a list of squares
print(squaredList)
