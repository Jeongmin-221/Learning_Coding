a = 64
for i in range(1,6):
    aa = a+i
    for j in range(i):
        print(chr(aa), end = " ")
        aa+=1
    print()
