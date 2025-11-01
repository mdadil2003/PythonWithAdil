try:
    a = int(input("Hey, Enter a number: "))

except ValueError as v: # Handleing specific exception
    print("Invalid input! Please enter a valid number.")
    print(v)
    
except Exception as e: # Handling any other exception
    print(e)
        
print("Thanks You")
