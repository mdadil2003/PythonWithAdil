f = open("read.txt")

lines = f.readlines() # reads all the lines and returns a list of lines

print(lines, type(lines)) # list of lines

f.close()