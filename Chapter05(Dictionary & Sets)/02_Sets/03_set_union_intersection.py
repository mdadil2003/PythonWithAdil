s1 = {12, 34, 2, 8}
s2 = {9, 6, 34, 5}

print(s1.union(s2)) # returns a new set with all elements from both sets

print(s1.intersection(s2)) # returns a new set with elements common to both sets

print(s1.difference(s2)) # returns a new set with elements in s1 but not in s2

print(s2.issubset(s1)) # returns True if s2 is a subset of s1
