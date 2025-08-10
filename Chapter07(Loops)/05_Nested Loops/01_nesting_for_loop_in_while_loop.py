  # Nested loops: while loop containing a for loop

i = 1
while (i <= 3):
    for k in range(1, 4):
        print(i, "*", k, "=", (i * k))
    i = i + 1
    print()
    