# The ‘enumerate’ function adds counter to an iterable and returns it as an enumerate object. This is useful when you need both the index and the value while iterating over a list or any other iterable.

from tracemalloc import start


l = [3,45,342, 23, 5]

for index, item in enumerate(l):
    print(f"At index {index} the value is {item}")
    # index += 1 # Manually incrementing index
