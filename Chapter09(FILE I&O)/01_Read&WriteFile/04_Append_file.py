
# a - open for appending (adds to the end of the file if it exists)

st = "(hey Adil you are an amazing coder......keep it up for future data analytics :)"

f = open("write.txt", "a") # opens the file in append(a) mode

f.write(st) # writes the string to the file

f.close()
