# Write a program to display a/b where a and b are integers. If b=0, display infinite by handling the ‘ZeroDivisionError’.

try:
    a = int(input("Enter a number: "))
    b = int(input("Enter second number: "))
    result = a / b
    print(f"The division a/b is {result}")
except ZeroDivisionError:
    print("infinite")
except ValueError:
    print("Invalid input! Please enter valid integers.")
except Exception as e:
    print(e)
finally:
    print("Thank you for using the division program.")
    