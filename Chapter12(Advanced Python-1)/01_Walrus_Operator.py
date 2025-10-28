# Walrus Operator Example
# The walrus operator (:=) allows assignment within an expression.


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
if (n := len(numbers)) > 5:
    print(f"List is too long ({n} elements, expected <= 5)") 
    