friends = ["Apple", "Orange", 5, 234.23, False, "Adil"]
print(friends)

friends.append("Raza") # Append an element at the end of the list
print(friends)
l1 = [1, 23, 4 , 43, 11]
#      |  |   |   |   |
#      0  1   2   3   4  Indexes of the list elements 

l1.sort() # Sort the list
print(l1)

l1.reverse() # Reverse the list
print(l1)

l1.insert(2, 3333) # Insert 3333 at index 3
print(l1)

l1.pop(3) # Remove the element at index 3
print(l1)

print(l1.pop(3)) # Return the index of the element 3333

l1.remove(43) # Remove the element 43
print(l1)