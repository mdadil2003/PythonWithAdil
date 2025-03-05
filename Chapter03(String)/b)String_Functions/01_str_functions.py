name = 'harry'
print(len(name)) # length of the string
print(name.endswith('rrya')) # returns False if the string ends with 'rrya'

print(name.startswith('ha')) # returns True if the string starts with 'ha'

print(name.capitalize()) # returns the string with first letter capitalized


str = "Adil Raza"
print(str.lower()) # returns the string in lower case
print(str.upper()) # returns the string in upper case
print(str.replace('Raza', 'Khan')) # replaces the character 'Raza' with 'Khan'
print(str.split(' ')) # splits the string into a list
print(str.find('R')) # returns the index of the character 'R'