f = open("read.txt")
print(f.read())
f.close()


# the same code using with statement like this we don't need to close the file manually

with open("read.txt") as f:
    print(f.read())
    
# when we use with statement it automatically closes the file after the use
