# Palindrome check using recursion.

def is_palindrome(s):
    # Base case
    if len(s) <= 1:
        return True
    
    # If first and last characters don't match, not a palindrome
    if s[0] != s[-1]:
        return False
    
    # Recursive case: check the substring inside
    return is_palindrome(s[1:-1])

print(is_palindrome("madam"))   # True
print(is_palindrome("racecar")) # True
print(is_palindrome("hello"))   # False
