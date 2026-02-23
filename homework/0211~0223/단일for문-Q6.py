N3 = 3
N5 = 5
isN3turn = True
isPrint = False
a=1
printn = 1

while True:
    
    if a%3 == 0 and isN3turn:
        printn = a
        isN3turn = False
        isPrint = True
    elif a%5 == 0 and not isN3turn:
        printn = a
        isN3turn = True
        isPrint = True

        
    if printn %15 == 0:
        isN3turn = not isN3turn
        isPrint = False
        a+=1
        continue
    
    if isPrint:
        print(printn, end = " ")
        isPrint = False
        
    if printn >= 100:
        break
    a+=1
    
