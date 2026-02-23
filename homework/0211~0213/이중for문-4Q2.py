for i in range(6):
    for j in range(6):
        if(i<j):
            print(" ", end = "")
    for j in range(i*2+1):
        print("*", end = "")
    print()
for i in range(4, -1, -1):
    for j in range(4-i+1):
        print(" ", end = "")
    for j in range(i*2+1):
        print("*", end = "")
    print()
