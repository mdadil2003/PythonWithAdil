# 5. Store the multiplication tables generated in problem 3 in a file named Tables.txt.

num = int(input("Enter a number to generate its multiplication table: "))

multiplication_table = [num * i for i in range(1, 11)]

with open("Tables.txt", "w") as file:
    file.write(f"Multiplication table of {num}:\n")
    
    for i in range(1, 11):
        file.write(f"{num} x {i} = {multiplication_table[i-1]}\n")
        
print(f"Multiplication table of {num} has been written to Tables.txt")
