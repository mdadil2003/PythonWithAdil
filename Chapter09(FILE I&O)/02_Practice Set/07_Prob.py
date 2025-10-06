# 7. Write a program to find out the line number where python is present from ques 6.

with open("log.txt", "r") as f:
    lines = f.readlines()
    for index, line in enumerate(lines):
        if "python" in line:
            print(f"'python' found on line {index + 1}")
            break
    else:  
        print("'python' not found in the file")
        