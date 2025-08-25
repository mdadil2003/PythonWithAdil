# 2. Write a python program using function to convert Celsius to Fahrenheit.

'''
# convert Celsius to Fahrenheit.

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = celsius_to_fahrenheit(celsius)
print(f"{celsius} Celsius is equal to {fahrenheit} Fahrenheit.")

'''

# convert Fahrenheit to Celsius.

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = fahrenheit_to_celsius(fahrenheit)
print(f"{fahrenheit} Fahrenheit is equal to {celsius} Celsius.")


