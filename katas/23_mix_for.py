#######################################
rows = 5
for i in range(0, rows):
    for j in range(0, i + 1):
        print(" * ", end=' ')
    print(" \r ")
#######################################
rows = 5
for j in range(1, rows + 1):
    print(" * " * j)
    
#######################################
rows = 5
for i in range(rows + 1, 0, -1):
    for j in range(0, i-1):
        print("*", end = ' ')
    print(" ")
#######################################
rows = 5
k = 2 * rows - 2
for i in range(rows, -1, -1):
    for j in range(k,i-1):
        print(end=" ")
    k = k + 1
    for j in range(0,i +1):
        print("*",end=" ")
    print("")