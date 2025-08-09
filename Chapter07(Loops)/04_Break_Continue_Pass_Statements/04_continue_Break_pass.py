numbers = [12, 7, -5, 0, 23, 8, -2, 15, 99]

# Using for loop with continue, break, and pass statements

# Using continue statement
print("Using continue (skip negative numbers):")
for num in numbers:
    if num < 0:
        continue
    print(num)

# Using break statement    
print("\nUsing break (stop at first zero):")
for num in numbers:
    if num == 0:
        break
    print(num)

# Using pass statement
print("\nUsing pass (placeholder for negative numbers):")
for num in numbers:
    if num < 0:
        pass  # Does nothing, just a placeholder
    else:
        print(num)
        
        