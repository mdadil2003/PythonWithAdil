# New operators | and |= allow for merging and updating dictionaries.


dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

merged = dict1 | dict2  # Merging dictionaries
print(merged)

dict1 |= dict2  # Updating dict1 with dict2
print(dict1)
