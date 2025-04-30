marks = {
    "Adil": 78,
    "Zeesdhan": 97,
    "Ali": 75,
    0: "Harry"
    
}

# DICTIONARY METHODS

# print(marks.items()) 
# print(marks.keys())   
# print(marks.values())

# print(marks.update({"Zeesdhan": 100, "Ali": 70}))
# print(marks)


# print(marks.get("Adil2"))  # returns None if key not found
# print(marks["Adil2"])   # raises KeyError if key not found

print(marks.pop("Adil"))  
print(marks)  