a=int(input("수 입력>"))
result=a
while True:
    result*=a
    if result >= 10000:
        break
    print(result, end=" ")
