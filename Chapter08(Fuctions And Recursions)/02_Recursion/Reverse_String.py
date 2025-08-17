# Reverse a String 

def reverse_string(s):
    # Base case
    if len(s) <= 1:
        return s
    # Recursive case
    return reverse_string(s[1:]) + s[0]

print(reverse_string("Adil Raza"))
print(reverse_string("python"))
