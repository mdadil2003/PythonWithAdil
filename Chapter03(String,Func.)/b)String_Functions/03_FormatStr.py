str4 = "Captain" 
str5 = "America"  
str6 = str4 + " " + str5  # Concatenation of two strings 
print(str6) 


name = "Adil Raza"
age = 22
statement = "My name is {} and my age is {}." # {} is a placeholder for the variables
print(statement.format(name, age)) # format() function is used to format the string


quantity = 2
fruit = "Apples"
cost = 120.0 
statement = "I want to buy {2} dozen {0} for {1}$" # {} is a placeholder for the variables 
print(statement.format(fruit,cost,quantity)) # format() function is used to format the string