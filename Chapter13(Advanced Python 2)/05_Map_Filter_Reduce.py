from functools import reduce

# Map Example 

l = [1, 2, 3, 4, 5]
square = lambda x: x * x

sqList = list(map(square, l))  # Applying square function to each item in list l
print(sqList)


# Filter Example

def even(n):
    if (n % 2 == 0):
        return True
    return False

onlyEven = list(filter(even, l))  # Filtering only even numbers from list l
print(list(onlyEven))


# Reduce Example

def sum(a, b):
    return a + b

print(reduce(sum, l))  # Reducing list l to a single sum value by applying sum function cumulatively
