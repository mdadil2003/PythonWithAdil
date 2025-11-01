try: # Try block to test code for errors
    a = int(input("Enter a number: "))
    print(a)
    
except Exception as e:
    print(e)
    
else: # Else block runs if no exception occurs
    print("The number entered is:", a)
    print("Thank you!")
    