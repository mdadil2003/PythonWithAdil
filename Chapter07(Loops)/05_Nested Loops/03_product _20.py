# Nested loops: for loop containing a while loop

stop = False
for i in range(1, 6):
    for j in range(1, 6):
        product = i * j
        print(i, j, product) 
        if product > 20:
            stop = True
            break
    if stop:
        break

