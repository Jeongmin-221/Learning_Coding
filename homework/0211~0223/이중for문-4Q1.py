for i in range(5):
    for j in range(5):
        if(i<j):
            print(" ", end = "")
    for j in range(i*2+1):
        print("*", end = "")
    print()
