# Check that a tuple type cannot be changed in python.

a = ("23, 234, Adil") # This is a tuple with three elements.

a[2] = "Ali" # This should raise an error because tuples are immutable.