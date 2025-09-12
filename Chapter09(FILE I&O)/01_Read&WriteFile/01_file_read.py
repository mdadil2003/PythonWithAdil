# Reading a file

f = open("read.txt") # by default it opens in read mode
data = f.read() # reads the entire file
print(data)

f.close() # always close the file after use

# if you don't close the file it can lead to memory leaks and data loss
