# Can we have a set with 18 (int) and '18' (str) as a value in it? 


s = set()
s.add(18)
s.add("18")

print(s) # returns a new set with all elements from both sets

# Yes, we can have a set with both 18 (int) and '18' (str) as values in it.