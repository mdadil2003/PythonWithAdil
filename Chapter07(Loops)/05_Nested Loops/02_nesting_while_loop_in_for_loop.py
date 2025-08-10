# Nested loops: for loop containing a while loop


for i in range(1, 4):
    k = 1
    while (k <= 3):
        print(i, "*", k, "=", (i * k))
        k = k + 1
    print()