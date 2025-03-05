# Write a program to fill in a letter template given below with name and date.
letter =  '''Dear <|Name|>, 
            You are selected! 
            <|Date|>  ''' # This is a letter template
            
print(letter.replace("<|Name|>", "Adil Raza") .replace("<|Date|>", "04th March 2025.")) # .replace() function is used to replace the placeholders with the actual values
