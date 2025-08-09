# Write a program to greet all the person names stored in a list ‘l’ and which starts with S.

l = ["Harry", "Siddiquei", "Soham", "Sachin", "Rahul", "Sagar", "Adil"]
for name in l:
    
    if(name.startswith("S")):  # Check if the name starts with 'S'
        print(f"Hello {name}")